import base64
import io
import logging
import os
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import numpy as np
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from matplotlib.figure import Figure

from csskp.settings import CUSTOM
from csskp.settings import PICTURE_DIR
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import Recommendations
from survey.models import SurveyQuestion
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.models import SurveyUserQuestionSequence
from utils.radarFactory import radar_factory

# Get an instance of a logger
logger = logging.getLogger(__name__)


def getRecommendations(user: SurveyUser, lang: str) -> Dict[str, List[str]]:
    employees_number_code = user.get_employees_number_code()

    user_answers = SurveyUserAnswer.objects.filter(user=user)

    final_report_recs: Dict[str, List[str]] = {}
    for user_answer in user_answers:
        recommendations = Recommendations.objects.filter(forAnswer=user_answer.answer)
        if not recommendations.exists():
            continue

        for rec in recommendations:
            if employees_number_code and (
                rec.min_e_count > employees_number_code
                or rec.max_e_count < employees_number_code
            ):
                continue

            if (user_answer.uvalue == "1" and rec.answerChosen) or (
                user_answer.uvalue == "0" and not rec.answerChosen
            ):
                # If categories are set, we use them otherwise question service category.
                category_name = ""
                if rec.categories:
                    rec_categories = rec.categories.all()
                    for index, rec_category in enumerate(rec_categories):
                        category_name += _(rec_category.label)
                        if len(rec_categories) > (index + 1):
                            category_name += " & "
                if category_name == "":
                    category_name = _(rec.forAnswer.question.service_category.label)

                translated_recommendation = _(rec.label)
                if is_recommendation_already_added(
                    translated_recommendation, final_report_recs
                ):
                    continue

                if category_name not in final_report_recs:
                    final_report_recs[category_name] = []
                final_report_recs[category_name].append(translated_recommendation)

    return {key: value for key, value in sorted(final_report_recs.items())}


def is_recommendation_already_added(recommendation: str, recommendations: dict) -> bool:
    if recommendations:
        for _category, recommendations_per_category in recommendations.items():
            if recommendation in recommendations_per_category:
                return True
    return False


def calculateResult(
    user: SurveyUser,
) -> Tuple[int, int, List[int], List[str], List[int], List[str]]:
    user_bonus_points_percent = 0

    chart_exclude_sections = [CONTEXT_SECTION_LABEL]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

    answered_questions_ids = [
        q.question.id
        for q in SurveyUserQuestionSequence.objects.filter(user=user, is_active=True)
    ]

    questions_by_section = (
        SurveyQuestion.objects.filter(id__in=answered_questions_ids)
        .exclude(section__label__in=chart_exclude_sections)
        .order_by("section_id")
    )

    sections: Dict[int, str] = {}
    categories: Dict[int, str] = {}
    max_evaluations_per_section: Dict[int, int] = {}
    max_evaluations_per_category: Dict[int, int] = {}
    total_questions_score = 0
    for question in questions_by_section.all():
        question_max_score = question.maxPoints
        # Taking max points from the dependency on answers' table if defined.
        for max_score in question.surveyquestionmaxscore_set.all():
            user_answer = SurveyUserAnswer.objects.filter(
                user=user, answer=max_score.selected_answer
            )[:1]
            if user_answer and user_answer[0].uvalue != "0":
                question_max_score = max_score.max_score
                break

        total_questions_score += question_max_score

        if question.section_id not in max_evaluations_per_section:
            max_evaluations_per_section[question.section_id] = 0
        max_evaluations_per_section[question.section_id] += question_max_score

        if question.service_category_id not in max_evaluations_per_category:
            max_evaluations_per_category[question.service_category_id] = 0
        max_evaluations_per_category[question.service_category_id] += question_max_score

        sections[question.section_id] = _(question.section.label)
        categories[question.service_category_id] = _(question.service_category.label)

    # There is no sections exclude, as score or bonus points can be set for the answers.
    user_answers = SurveyUserAnswer.objects.filter(user=user).order_by(
        "answer__question__qindex", "answer__aindex"
    )

    total_user_score = 0
    total_bonus_points = 0
    user_given_bonus_points = 0
    user_evaluations_per_section: Dict[int, int] = {}
    user_evaluations_per_category: Dict[int, int] = {}
    for user_answer in user_answers.all():
        total_bonus_points += user_answer.answer.bonus_points
        if user_answer.uvalue == "1":
            user_given_bonus_points += user_answer.answer.bonus_points
            answer_score = user_answer.answer.score
            # If the scores dependencies are set, then get from the table.
            for answer_score in user_answer.answer.answer_scores.all():
                dependant_user_answer = SurveyUserAnswer.objects.filter(
                    user=user, answer=answer_score.selected_answer
                )[:1]
                if dependant_user_answer and dependant_user_answer[0].uvalue != "0":
                    answer_score = answer_score.score
                    break
            total_user_score += answer_score

            section = user_answer.answer.question.section
            if section.label in chart_exclude_sections:
                continue

            if section.id not in user_evaluations_per_section:
                user_evaluations_per_section[section.id] = 0
            user_evaluations_per_section[section.id] += user_answer.answer.score

            category = user_answer.answer.question.service_category
            if category.id not in user_evaluations_per_category:
                user_evaluations_per_category[category.id] = 0
            user_evaluations_per_category[category.id] += user_answer.answer.score

    # Get the score & bonus pts in percent, with then 100 being total_questions_score.
    if total_user_score > 0:
        total_user_score = round(total_user_score * 100 / total_questions_score)
    if total_bonus_points > 0:
        user_bonus_points_percent = round(
            user_given_bonus_points * 100 / total_bonus_points
        )

    return (
        total_user_score,
        user_bonus_points_percent,
        prepare_evaluations(user_evaluations_per_section, max_evaluations_per_section),
        list(sections.values()),
        prepare_evaluations(
            user_evaluations_per_category, max_evaluations_per_category
        ),
        [i for k, i in sorted(categories.items())],
    )


def prepare_evaluations(
    user_evaluations: Dict[int, int], max_evaluations: Dict[int, int]
) -> List[int]:
    evaluations: List[int] = []
    for item_id, user_evaluation in sorted(user_evaluations.items()):
        evaluations.append(
            round(user_evaluation * 100 / max_evaluations[item_id])
        ) if max_evaluations[item_id] > 0 else evaluations.append(0)

    return evaluations


def generate_chart_png(
    user: SurveyUser, evaluation, sections_list, output_type="file"
) -> Optional[str]:
    """Generates the chart with Matplotlib and returns the path of the generated
    graph which will be included in the report.
    Returns a graph in base 64 as a string or writes the graph in a file on the disk.
    """
    n = len(sections_list)
    assert len(evaluation) == n, "'evaluation' and 'sections_list' must have same size."
    theta = radar_factory(n, frame="polygon")

    fig = Figure(figsize=(15, 15), dpi=150)
    ax = fig.subplots(nrows=1, ncols=1, subplot_kw=dict(projection="radar"))
    fig.subplots_adjust(left=0.15, right=0.85)

    ax.set_rgrids([0, 20, 40, 60, 80, 100], angle=0)
    ax.set_ylim(0, 100)

    ax.plot(theta, evaluation, color="r")
    ax.fill(theta, evaluation, facecolor="r", alpha=0.25)
    ax.set_varlabels(sections_list)
    ax.set_xticklabels(sections_list, wrap=True, multialignment="center")

    for label, angle in zip(ax.get_xticklabels(), theta):
        if angle in (0, np.pi):
            label.set_horizontalalignment("center")
        elif 0 < angle < np.pi:
            label.set_horizontalalignment("left")
        else:
            label.set_horizontalalignment("right")

    if output_type == "base64":
        stringIObytes = io.BytesIO()
        try:
            fig.savefig(stringIObytes, format="svg")
        except Exception as e:
            raise Exception(f"{e}")
        stringIObytes.seek(0)
        return base64.b64encode(stringIObytes.read()).decode()
    else:
        if not os.path.isdir(PICTURE_DIR):
            os.makedirs(PICTURE_DIR)
        file_name = os.path.join(PICTURE_DIR, f"survey-{user.user_id}.svg")
        try:
            fig.savefig(file_name)
        except Exception as e:
            raise Exception(f"{e}")
        return file_name


def get_answered_questions_list(user: SurveyUser):
    return [i.question for i in get_answered_questions_sequences(user)]


def get_answered_questions_sequences(user: SurveyUser):
    return SurveyUserQuestionSequence.objects.filter(
        user=user, has_been_answered=True
    ).order_by("branch", "level", "index")
