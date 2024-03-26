from stats.views import DEFAULT_DATE_FORMAT
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import SURVEY_STATUS_FINISHED
from survey.models import SurveyQuestion
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.models import SurveyUserFeedback
from survey.reporthelper import get_answer_score


def get_finished_surveys_list(start_date, end_date):
    completed_surveys_users = SurveyUser.objects.filter(
        status=SURVEY_STATUS_FINISHED,
        updated_at__gte=start_date.strftime(DEFAULT_DATE_FORMAT),
        updated_at__lte=end_date.strftime(DEFAULT_DATE_FORMAT),
    ).order_by("updated_at")

    total_questions_score = 1
    total_overall_score = 0
    max_evaluations_per_section = {}
    for question in SurveyQuestion.objects.exclude(
        section__label__contains=CONTEXT_SECTION_LABEL
    ).all():
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
                "language": completed_survey_user.chosen_lang,
                "survey_finish_date": completed_survey_user.updated_at.strftime(
                    DEFAULT_DATE_FORMAT
                ),
                "has_general_feedback": has_general_feedback,
                "total_score": 0,
            },
            "sections": {},
        }
        # Add information about the context
        surveys_users_results["survey_users"][user_id]["details"].update(
            {
                str(key): str(value)
                for key, value in completed_survey_user.get_all_context_answers().items()
            }
        )

        total_points_number = 0

        user_answers = (
            SurveyUserAnswer.objects.filter(user=completed_survey_user)
            .exclude(answer__question__section__label=CONTEXT_SECTION_LABEL)
            .order_by("answer__question__qindex", "answer__aindex")
        )
        for user_answer in user_answers:
            section_id = user_answer.answer.question.section.id
            if (
                section_id
                not in surveys_users_results["survey_users"][user_id]["sections"]
            ):
                surveys_users_results["survey_users"][user_id]["sections"][
                    section_id
                ] = {
                    "label": user_answer.answer.question.section.label,
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
                    "label": question.label,
                    "answers": [],
                    "has_feedback": has_feedback,
                }

            if user_answer.uvalue != "0":
                surveys_users_results["survey_users"][user_id]["sections"][section_id][
                    "questions"
                ][question.id]["answers"].append(
                    {
                        user_answer.answer.id: {
                            "label": user_answer.answer.label,
                            "value": user_answer.uvalue,
                            "score": user_answer.answer.score,
                            "content": user_answer.content,
                        }
                    }
                )

            if question.maxPoints == 0:
                continue

            if user_answer.uvalue == "1":
                answer_score = get_answer_score(completed_survey_user, user_answer)
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
        total_overall_score += surveys_users_results["survey_users"][user_id][
            "details"
        ]["total_score"]

    return {
        "start_date": str(start_date),
        "end_date": str(end_date),
        "total_average_score": round(
            total_overall_score / surveys_users_results["surveys_total_number"]
        ),
        "surveys_users_results": surveys_users_results,
    }
