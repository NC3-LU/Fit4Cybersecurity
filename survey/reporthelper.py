# -*- coding: utf-8 -*-

from typing import Dict, List, Optional, Tuple
import io
import os
import base64
import logging

from csskp.settings import PICTURE_DIR
from survey.models import (
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUser,
    SurveyUserAnswer,
    Recommendations,
    Translation,
)
from utils.radarFactory import radar_factory
import matplotlib.pyplot as plt

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_translation(original: str, lang: str) -> str:
    """Look for the translation of a string.
    Returns the original string if the translation is not found."""
    translation = Translation.objects.filter(original=original, lang=lang)
    if translation.exists():
        return translation[0].translated
    else:
        return original


def getRecommendations(user: SurveyUser, lang: str) -> Dict[str, List[str]]:
    allAnswers = SurveyQuestionAnswer.objects.all().order_by(
        "question__qindex", "aindex"
    )
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
                category_name = get_translation(
                    rec.forAnswer.question.service_category.label, lang
                )

                translated_recommendation = get_translation(rec.label, lang)
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


def calculateResult(user: SurveyUser, lang: str) -> Tuple[int, List[int], List[str]]:
    total_questions_score = 0
    total_user_score = 0
    total_bonus_points = 0
    user_given_bonus_points = 0
    user_evaluations_per_section: Dict[int, int] = {}
    max_evaluations_per_section: Dict[int, int] = {}
    sections_list: List[str] = []

    for question in SurveyQuestion.objects.all():
        total_questions_score += question.maxPoints

        if question.section.id not in max_evaluations_per_section:
            max_evaluations_per_section[question.section.id] = 0
        max_evaluations_per_section[question.section.id] += question.maxPoints

        section_title = get_translation(question.section.label, lang)
        if section_title not in sections_list:
            sections_list.append(section_title)

    user_answers = SurveyUserAnswer.objects.filter(
        user=user
    ).order_by("answer__question__qindex", "answer__aindex")
    for user_answer in user_answers:

        total_bonus_points += user_answer.answer.bonus_points

        if user_answer.uvalue > 0:
            section_id = user_answer.answer.question.section.id

            total_user_score += user_answer.answer.score

            user_given_bonus_points += user_answer.answer.bonus_points

            if section_id not in user_evaluations_per_section:
                user_evaluations_per_section[section_id] = 0
            user_evaluations_per_section[section_id] += user_answer.answer.score

    # get the score in percent! with then 100 being total_questions_score
    total_user_score = round(total_user_score * 100 / total_questions_score)
    user_bonus_points_percent = 0
    if total_bonus_points != 0:
        user_bonus_points_percent = round(user_given_bonus_points * 100 / total_bonus_points)

    user_evaluations: List[int] = []
    for section_id, user_evaluation_per_section in user_evaluations_per_section.items():
        user_evaluations.append(
            round(
                user_evaluation_per_section
                * 100
                / max_evaluations_per_section[section_id]
            )
        )

    return total_user_score, user_bonus_points_percent, user_evaluations, sections_list


def generate_chart_png(
    user: SurveyUser, evaluation, sections_list, lang, output_type="file"
) -> Optional[str]:
    """Generates the chart with Matplotlib and returns the path of the generated
    graph which will be included in the report.
    Returns a graph in base 64 as a string or writes the graph in a file on the disk.
    """
    n = len(sections_list)
    theta = radar_factory(n, frame="polygon")

    fig, ax = plt.subplots(
        figsize=(7, 7), dpi=300, nrows=1, ncols=1, subplot_kw=dict(projection="radar")
    )
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    ax.set_rgrids([0, 20, 40, 60, 80, 100], angle=0)
    ax.set_ylim(0, 100)

    ax.plot(theta, evaluation, color="r")
    ax.fill(theta, evaluation, facecolor="r", alpha=0.25)

    ax.set_varlabels(sections_list)

    if output_type == "base64":
        stringIObytes = io.BytesIO()
        try:
            plt.savefig(stringIObytes, format="png")
        except Exception as e:
            raise Exception("{}".format(e))
        finally:
            plt.close()
        stringIObytes.seek(0)
        return base64.b64encode(stringIObytes.read()).decode()
    else:
        if not os.path.isdir(PICTURE_DIR):
            os.makedirs(PICTURE_DIR)
        file_name = os.path.join(PICTURE_DIR, "survey-{}.png".format(user.user_id))
        try:
            plt.savefig(file_name)
        except Exception as e:
            raise Exception("{}".format(e))
        finally:
            plt.close()
        return file_name
