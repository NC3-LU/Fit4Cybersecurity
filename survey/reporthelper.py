# -*- coding: utf-8 -*-

from typing import Optional, Dict, List, Tuple
import io
import os
import base64
import logging

from csskp.settings import PICTURE_DIR, CUSTOM
from survey.models import (
    SurveyQuestion,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
    SurveyUserQuestionSequence,
    CONTEXT_SECTION_LABEL,
)
from utils.radarFactory import radar_factory
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from matplotlib.figure import Figure

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
                            category_name += ' & '
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
        for category, recommendations_per_category in recommendations.items():
            if recommendation in recommendations_per_category:
                return True
    return False


def calculateResult(user: SurveyUser) -> Tuple[int, int, List[int], List[str]]:
    user_bonus_points_percent = 0
    user_evaluations: List[int] = []

    chart_exclude_sections = [CONTEXT_SECTION_LABEL]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

    # TODO: go through the sequence instead.
    questions = (
        SurveyQuestion.objects.exclude(section__label__in=chart_exclude_sections)
        .values_list("section_id")
        .order_by("section_id")
        .annotate(total=Sum("maxPoints"))
    )

    max_evaluations_per_section = {q[0]: q[1] for q in questions}
    total_questions_score = questions.aggregate(total=Sum("maxPoints"))["total"]
    sections = list(questions.values_list("section__label", flat=True).distinct())

    # There are no exclude sections, because score or bonus points can be set to some answers.
    user_answers = SurveyUserAnswer.objects.filter(user=user).order_by(
        "answer__question__qindex", "answer__aindex"
    )

    total_bonus_points = user_answers.aggregate(total=Sum("answer__bonus_points"))[
        "total"
    ]
    user_given_bonus_points = user_answers.filter(uvalue=1).aggregate(
        total=Sum("answer__bonus_points")
    )["total"]
    total_user_score = user_answers.filter(uvalue=1).aggregate(
        total=Sum("answer__score")
    )["total"]

    user_answers_excluded = user_answers.exclude(
        answer__question__section__label__in=chart_exclude_sections
    ).filter(uvalue=1)

    user_answers_by_section = (
        user_answers_excluded.values("answer__question__section_id")
        .order_by("answer__question__section_id")
        .annotate(score=Sum("answer__score"))
    )
    for answer in user_answers_by_section:
        if max_evaluations_per_section[answer["answer__question__section_id"]] > 0:
            user_evaluations.append(
                round(
                    answer["score"]
                    * 100
                    / max_evaluations_per_section[
                        answer["answer__question__section_id"]
                    ]
                )
            )
        else:
            user_evaluations.append(0)

    # Get the score in percent, with then 100 being total_questions_score.
    if total_user_score > 0:
        total_user_score = round(total_user_score * 100 / total_questions_score)
    if total_bonus_points > 0:
        user_bonus_points_percent = round(
            user_given_bonus_points * 100 / total_bonus_points
        )

    return (
        total_user_score,
        user_bonus_points_percent,
        user_evaluations,
        sections,
    )


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

    fig = Figure(figsize=(11, 11), dpi=150)
    ax = fig.subplots(nrows=1, ncols=1, subplot_kw=dict(projection="radar"))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    ax.set_rgrids([0, 20, 40, 60, 80, 100], angle=0)
    ax.set_ylim(0, 100)

    ax.plot(theta, evaluation, color="r")
    ax.fill(theta, evaluation, facecolor="r", alpha=0.25)

    ax.set_varlabels(sections_list)

    if output_type == "base64":
        stringIObytes = io.BytesIO()
        try:
            fig.savefig(stringIObytes, format="svg")
        except Exception as e:
            raise Exception("{}".format(e))
        stringIObytes.seek(0)
        return base64.b64encode(stringIObytes.read()).decode()
    else:
        if not os.path.isdir(PICTURE_DIR):
            os.makedirs(PICTURE_DIR)
        file_name = os.path.join(PICTURE_DIR, "survey-{}.svg".format(user.user_id))
        try:
            fig.savefig(file_name)
        except Exception as e:
            raise Exception("{}".format(e))
        return file_name


def get_answered_questions_list(user: SurveyUser):
    return [i.question for i in get_answered_questions_sequences(user)]


def get_answered_questions_sequences(user: SurveyUser):
    return SurveyUserQuestionSequence.objects.filter(
        user=user, has_been_answered=True
    ).order_by("branch", "level", "index")
