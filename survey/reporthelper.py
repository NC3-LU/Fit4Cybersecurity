# -*- coding: utf-8 -*-

from typing import Dict, List, Union
import io
import os
import base64
import logging
from django.utils.translation import gettext_lazy as _

from csskp.settings import PICTURE_DIR
from survey.models import (
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
    TranslationKey,
)
from utils.radarFactory import radar_factory
import matplotlib.pyplot as plt

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_formatted_translations(lang: str, type: str) -> Dict:
    translations = TranslationKey.objects.filter(lang=lang, ttype=type)
    translation_key_values = {}
    for translation in translations:
        translation_key_values[translation.key] = translation.text

    return translation_key_values


def getRecommendations(user: SurveyUser, lang: str):
    allAnswers = SurveyQuestionAnswer.objects.all().order_by(
        "question__qindex", "aindex"
    )
    recommendations_translations = get_formatted_translations(lang, "R")
    categories_translations = get_formatted_translations(lang, "C")

    finalReportRecs: Dict[str, List[str]] = {}

    for a in allAnswers:
        userAnswer = SurveyUserAnswer.objects.filter(user=user).filter(answer=a)[0]
        recommendations = Recommendations.objects.filter(forAnswer=a)

        if not recommendations.exists():
            continue

        for rec in recommendations:
            if rec.min_e_count > user.e_count or rec.max_e_count < user.e_count:
                continue
            if (userAnswer.uvalue > 0 and rec.answerChosen) or (
                userAnswer.uvalue <= 0 and not rec.answerChosen
            ):
                category_name = categories_translations[
                    rec.forAnswer.question.service_category.titleKey
                ]

                translated_recommendation = recommendations_translations[rec.textKey]
                if is_recommendation_already_added(
                    translated_recommendation, finalReportRecs
                ):
                    continue

                if category_name not in finalReportRecs:
                    finalReportRecs[category_name] = []
                finalReportRecs[category_name].append(
                    recommendations_translations[rec.textKey]
                )
    return finalReportRecs


def is_recommendation_already_added(recommendation: str, recommendations: dict):
    if recommendations:
        for category, recommendations_per_category in recommendations.items():
            if recommendation in recommendations_per_category:
                return True

    return False


def calculateResult(user: SurveyUser, lang: str):
    total_questions_score = 0
    total_user_score = 0
    user_evaluations_per_section: Dict[int, int] = {}  # noqa
    max_evaluations_per_section: Dict[int, int] = {}
    sections_list = []

    translation_key_values = get_formatted_translations(lang, "S")

    for question in SurveyQuestion.objects.all():
        total_questions_score += question.maxPoints

        if question.section.id not in max_evaluations_per_section:
            max_evaluations_per_section[question.section.id] = 0
        max_evaluations_per_section[question.section.id] += question.maxPoints

        section_title = translation_key_values[question.section.sectionTitleKey]
        if section_title not in sections_list:
            sections_list.append(section_title)

    user_selected_answers = SurveyUserAnswer.objects.filter(
        user=user, uvalue__gt=0
    ).order_by("answer__question__qindex", "answer__aindex")
    for user_selected_answer in user_selected_answers:
        section_id = user_selected_answer.answer.question.section.id

        total_user_score += user_selected_answer.answer.score

        if section_id not in user_evaluations_per_section:
            user_evaluations_per_section[section_id] = 0
        user_evaluations_per_section[section_id] += user_selected_answer.answer.score

    # get the score in percent! with then 100 being total_questions_score
    total_user_score = round(total_user_score * 100 / total_questions_score)

    user_evaluations: List[int] = []
    for section_id, user_evaluation_per_section in user_evaluations_per_section.items():
        user_evaluations.append(
            round(
                user_evaluation_per_section
                * 100
                / max_evaluations_per_section[section_id]
            )
        )

    return total_user_score, user_evaluations, sections_list


def generate_chart_png(
    user: SurveyUser, evaluation, sections_list, lang, output_type="file"
) -> Union[str, bytes, None]:
    """Generates the chart with Matplotlib and returns the path of the generated
    graph which will be included in the report.
    """
    n = len(sections_list)
    theta = radar_factory(n, frame="polygon")

    spoke_labels = []
    for section in sections_list:
        spoke_labels.append(section)

    fig, ax = plt.subplots(
        figsize=(7, 5), dpi=150, nrows=1, ncols=1, subplot_kw=dict(projection="radar")
    )
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    ax.set_rgrids([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax.set_ylim(0, 100)

    ax.plot(theta, evaluation, color="r")
    ax.fill(theta, evaluation, facecolor="r", alpha=0.25)

    ax.set_varlabels(spoke_labels)

    ax.legend(
        _("Your results"),
        loc=(0.9, 0.95),
        labelspacing=0.1,
        fontsize="small",
    )

    fig.text(
        1.0,
        1.0,
        _("Your results chart"),
        horizontalalignment="center",
        color="black",
        weight="bold",
        size="large",
    )

    if not os.path.isdir(PICTURE_DIR):
        os.makedirs(PICTURE_DIR)
    file_name = os.path.join(PICTURE_DIR, "survey-{}.png".format(user.user_id))
    try:
        if output_type == "base64":
            stringIObytes = io.BytesIO()
            plt.savefig(stringIObytes, format="png")
            stringIObytes.seek(0)
            return base64.b64encode(stringIObytes.read())

        plt.savefig(file_name)
    except Exception as e:
        raise Exception("{}".format(e))
    finally:
        plt.close()

    return file_name
