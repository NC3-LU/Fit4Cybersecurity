# -*- coding: utf-8 -*-

import json
from stats.forms import DatesLimitForm, DEFAULT_DATE_FORMAT
from survey.models import (
    SurveyQuestion,
    SurveyUserFeedback,
    SurveyUser,
    SurveyUserAnswer,
    SURVEY_STATUS_FINISHED,
)

from survey.globals import COMPANY_SIZE


def get_finished_surveys_list(request):
    if request.method == "POST":
        dates_limit_form = DatesLimitForm(data=request.POST)
        if not dates_limit_form.is_valid():
            return None
        start_date = dates_limit_form.cleaned_data["start_date"]
        end_date = dates_limit_form.cleaned_data["end_date"]
    else:
        dates_limit_form = DatesLimitForm()
        start_date = dates_limit_form.fields["start_date"].initial
        end_date = dates_limit_form.fields["end_date"].initial

    completed_surveys_users = SurveyUser.objects.filter(
        status=SURVEY_STATUS_FINISHED,
        updated_at__gte=start_date.strftime(DEFAULT_DATE_FORMAT),
        updated_at__lte=end_date.strftime(DEFAULT_DATE_FORMAT),
    )

    total_questions_score = 0
    max_evaluations_per_section = {}
    for question in SurveyQuestion.objects.all():
        total_questions_score += question.maxPoints
        if question.section.id not in max_evaluations_per_section:
            max_evaluations_per_section[question.section.id] = 0
        max_evaluations_per_section[question.section.id] += question.maxPoints

    surveys_users_results = {
        "surveys_total_number": completed_surveys_users.count(),
        "survey_users": {},
    }
    for completed_survey_user in completed_surveys_users:
        survey_user_feedbacks = SurveyUserFeedback.objects.filter(
            user=completed_survey_user
        )
        feedbacks_per_question = []
        has_general_feedback = 0
        for survey_user_feedback in survey_user_feedbacks:
            if survey_user_feedback.question is None:
                has_general_feedback = 1
            else:
                feedbacks_per_question.append(survey_user_feedback.question.id)

        user_id = str(completed_survey_user.user_id)
        surveys_users_results["survey_users"][user_id] = {
            "details": {
                "sector": completed_survey_user.sector,
                "employees_number": [
                    item[1]
                    for item in COMPANY_SIZE
                    if item[0] == completed_survey_user.e_count
                ][0],
                "country_code": completed_survey_user.country_code,
                "language": completed_survey_user.choosen_lang,
                "survey_finish_date": completed_survey_user.updated_at.strftime(
                    DEFAULT_DATE_FORMAT
                ),
                "has_general_feedback": has_general_feedback,
                "total_score": 0,
            },
            "sections": {},
        }

        total_points_number = 0

        user_answers = SurveyUserAnswer.objects.filter(
            user=completed_survey_user
        ).order_by("answer__question__qindex", "answer__aindex")
        for user_answer in user_answers:
            section_id = user_answer.answer.question.section.id
            if (
                section_id
                not in surveys_users_results["survey_users"][user_id]["sections"]
            ):
                surveys_users_results["survey_users"][user_id]["sections"][
                    section_id
                ] = {
                    "score": 0,
                    "questions": {},
                }

            question = user_answer.answer.question
            if (
                question.id
                not in surveys_users_results["survey_users"][user_id]["sections"][
                    section_id
                ]["questions"]
            ):
                has_feedback = 0
                if question.id in feedbacks_per_question:
                    has_feedback = 1
                surveys_users_results["survey_users"][user_id]["sections"][section_id][
                    "questions"
                ][question.id] = {
                    "score": 0,
                    "answers": [],
                    "has_feedback": has_feedback,
                }

            surveys_users_results["survey_users"][user_id]["sections"][section_id][
                "questions"
            ][question.id]["answers"].append(
                {
                    user_answer.answer.id: {
                        "value": user_answer.uvalue,
                        "score": user_answer.answer.score,
                    }
                }
            )

            if user_answer.uvalue > 0:
                answer_score = user_answer.answer.score
                total_points_number += answer_score
                surveys_users_results["survey_users"][user_id]["sections"][section_id][
                    "questions"
                ][question.id]["score"] += round(
                    answer_score * 100 / user_answer.answer.question.maxPoints
                )
                surveys_users_results["survey_users"][user_id]["sections"][section_id][
                    "score"
                ] += round(answer_score * 100 / max_evaluations_per_section[section_id])

        surveys_users_results["survey_users"][user_id]["details"][
            "total_score"
        ] = round(total_points_number * 100 / total_questions_score)

    return {
        "dates_limit_form": dates_limit_form,
        "surveys_users_results": json.dumps(surveys_users_results),
    }
