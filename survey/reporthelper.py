# -*- coding: utf-8 -*-

from typing import Optional, Dict, List, Tuple
import io
import os
import base64
import logging

from csskp.settings import PICTURE_DIR, CUSTOM
from survey.models import (
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
)
from utils.radarFactory import radar_factory
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from matplotlib.figure import Figure

# Get an instance of a logger
logger = logging.getLogger(__name__)


def getRecommendations(user: SurveyUser, lang: str) -> Dict[str, List[str]]:
    allAnswers = SurveyQuestionAnswer.objects.exclude(
        question__section__label__contains="__context"
    ).order_by("question__qindex", "aindex")
    employees_number_code = user.get_employees_number_code()

    finalReportRecs: Dict[str, List[str]] = {}
    for a in allAnswers:
        try:
            userAnswer = SurveyUserAnswer.objects.filter(user=user).filter(answer=a)[0]
        except IndexError:
            continue
        recommendations = Recommendations.objects.filter(forAnswer=a)

        if not recommendations.exists():
            continue

        for rec in recommendations:
            if employees_number_code and (
                rec.min_e_count > employees_number_code
                or rec.max_e_count < employees_number_code
            ):
                continue

            if (userAnswer.uvalue == "1" and rec.answerChosen) or (
                userAnswer.uvalue == "0" and not rec.answerChosen
            ):
                category_name = _(rec.forAnswer.question.service_category.label)

                translated_recommendation = _(rec.label)
                if is_recommendation_already_added(
                    translated_recommendation, finalReportRecs
                ):
                    continue

                if category_name not in finalReportRecs:
                    finalReportRecs[category_name] = []
                finalReportRecs[category_name].append(translated_recommendation)

    return finalReportRecs


def is_recommendation_already_added(recommendation: str, recommendations: dict) -> bool:
    if recommendations:
        for category, recommendations_per_category in recommendations.items():
            if recommendation in recommendations_per_category:
                return True
    return False


def calculateResult(user: SurveyUser) -> Tuple[int, int, List[int], List[str]]:
    total_questions_score = 0
    total_user_score = 0
    total_bonus_points = 0
    user_given_bonus_points = 0
    user_bonus_points_percent = 0
    max_evaluations_per_section: Dict[int, int] = {}
    sections: Dict[int, str] = {}
    user_evaluations: List[int] = []

    chart_exclude_sections = ["__context"]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

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

    user_evaluations = user.get_evaluations_by_section(max_evaluations_per_section)

    # get the score in percent, with then 100 being total_questions_score
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
