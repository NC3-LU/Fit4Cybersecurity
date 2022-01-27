# -*- coding: utf-8 -*-

from typing import Union, List, Dict, Tuple, Any
from typing_extensions import TypedDict
import logging
from uuid import UUID
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, mark_safe
from django.db import transaction
from django.utils import translation

from survey.models import (
    SurveyUser,
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUserAnswer,
    SurveyUserFeedback,
    SURVEY_STATUS_UNDER_REVIEW,
)
from survey.forms import AnswerMChoice, GeneralFeedback
from csskp.settings import CUSTOM, LANGUAGES, LANGUAGE_CODE

LOCAL_DEFAULT_LANG = LANGUAGE_CODE

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionWithUserAnswers(TypedDict):
    """Defines a type for a question with user answers"""

    question_title: str
    feedback: str
    user_answers: list[Any]


def create_user(lang: str) -> SurveyUser:
    """Creates a new SurveyUser object.
    This function is called by the function handle_start_surveyonce, once the user has
    answered the first questions before the start of the survey."""
    user = SurveyUser()
    # defines the next question (exclude the context questions)
    survey_question = SurveyQuestion.objects.exclude(
        section__label__contains="__context"
    ).order_by("qindex")[:1]
    user.current_qindex = survey_question[0].qindex
    # Ensures the submitted languages is accepted
    langs, _ = zip(*LANGUAGES)
    if lang in langs:
        user.chosen_lang = lang
    else:
        user.chosen_lang = LOCAL_DEFAULT_LANG
    user.save()

    return user


def handle_start_survey(request: HttpRequest, lang: str) -> Union[Dict, SurveyUser]:
    """Handles the start of the survey."""
    action = "/survey/start"
    title = CUSTOM["tool_name"] + " - " + _("Let's start")

    forms = {}
    questions = (
        SurveyQuestion.objects.filter(section__label__contains="__context")
        .order_by("-qindex")
        .all()
    )

    # if no context questions: create the user without the form
    if not questions.count() and request.method == "GET":
        user = create_user(lang)
        request.session["user_id"] = str(user.user_id)

        return user

    for question in questions:
        try:
            tuple_answers = get_answer_choices(question, lang)
        except Exception as e:
            logger.error(e)
            raise e

        forms[question.id] = AnswerMChoice(
            tuple_answers,
            lang=lang,
            data=request.POST if request.method == "POST" else None,
            answers_field_type=question.qtype,
            question_answers=question.surveyquestionanswer_set.filter(is_active=True),
            prefix="form" + str(question.id),
        )

    if request.method == "POST":
        if all([form.is_valid() for question_id, form in forms.items()]):
            # create the user
            user = create_user(lang)
            request.session["user_id"] = str(user.user_id)

        for question in questions:
            form = forms[question.id]
            answers = form.cleaned_data["answers"]
            answer_content = ""
            if "answer_content" in form.cleaned_data:
                answer_content = form.cleaned_data["answer_content"]

            # create the answers
            save_answers(user, question, answers, answer_content)

        return user

    return {
        "title": title,
        "forms": forms,
        "questions_per_id": {question.id: _(question.label) for question in questions},
        "action": action,
        "chosen_lang": lang,
    }


@transaction.atomic
def handle_question_answers_request(
    request: HttpRequest, user: SurveyUser, question_index: int
) -> Union[Dict, SurveyUser]:
    (
        previous_question,
        current_question,
        next_question,
        total_questions_num,
    ) = get_questions_slice(question_index)

    try:
        question_answers = current_question.surveyquestionanswer_set.filter(
            is_active=True
        )
        tuple_answers = get_answer_choices(current_question, user.chosen_lang)
    except Exception as e:
        logger.error(e)
        raise e

    free_text_answer_id = 0
    for question_answer in question_answers:
        if question_answer.atype == "T":
            free_text_answer_id = question_answer.id

    translation.activate(user.chosen_lang)

    if request.method == "POST":
        form = AnswerMChoice(
            tuple_answers,
            data=request.POST,
            lang=user.chosen_lang,
            answers_field_type=current_question.qtype,
            question_answers=question_answers,
        )
        if form.is_valid():
            user = SurveyUser.objects.select_for_update(nowait=True).filter(id=user.id)[
                0
            ]
            answers = form.cleaned_data["answers"]
            answer_content = ""
            if "answer_content" in form.cleaned_data:
                answer_content = form.cleaned_data["answer_content"]

            save_answers(user, current_question, answers, answer_content)

            feedback = form.cleaned_data["feedback"]
            if feedback:
                user_feedback = SurveyUserFeedback.objects.filter(
                    user=user, question=current_question
                )[:1]
                if not user_feedback:
                    user_feedback = SurveyUserFeedback()
                    user_feedback.user = user
                    user_feedback.question = current_question
                else:
                    user_feedback = user_feedback[0]
                user_feedback.feedback = feedback
                user_feedback.save()

            if next_question is not None:
                user.current_qindex = next_question.qindex
            else:
                user.status = SURVEY_STATUS_UNDER_REVIEW

            user.save()

            return user
    else:
        form = AnswerMChoice(
            tuple_answers,
            lang=user.chosen_lang,
            answers_field_type=current_question.qtype,
            question_answers=question_answers,
        )

        user_answers = SurveyUserAnswer.objects.filter(
            user=user, answer__question=current_question
        )
        selected_answers = []
        for user_answer in user_answers:
            if user_answer.uvalue == "1":
                selected_answers.append(user_answer.answer.id)
            if user_answer.content:
                form.set_answer_content(user_answer.content)

        user_feedback = SurveyUserFeedback.objects.filter(
            user=user, question=current_question
        )[:1]

        form.set_answers(selected_answers)
        if user_feedback:
            form.set_feedback(user_feedback[0].feedback)

    uniqueAnswers = SurveyQuestionAnswer.objects.filter(
        question=current_question, uniqueAnswer=True
    )
    form.set_unique_answers(
        ",".join(str(uniqueAnswer.id) for uniqueAnswer in uniqueAnswers)
    )
    form.set_free_text_answer_id(free_text_answer_id)

    return {
        "title": CUSTOM["tool_name"] + " - " + _("Question") + " " + str(current_question.qindex),
        "question": _(current_question.label),
        "question_tooltip": _(current_question.tooltip),
        "form": form,
        "action": "/survey/question/" + str(current_question.qindex),
        "user": user,
        "current_question_index": current_question.qindex,
        "previous_question_index": previous_question.qindex,
        "total_questions_num": total_questions_num,
    }


def save_answers(
    user: SurveyUser,
    current_question: SurveyQuestion,
    posted_answers: List[Union[int, str]],
    answer_content: str,
) -> None:
    match current_question.qtype:
        case "SO":
            selected_value = posted_answers[0]
            question_answers = [
                current_question.surveyquestionanswer_set.get(
                    is_active=True,
                    value=selected_value
                )
            ]
        case "CL":
            selected_value = posted_answers[0]
            question_answers = [
                current_question.surveyquestionanswer_set.all()[0]
            ]
        case _:
            question_answers = current_question.surveyquestionanswer_set.filter(
                is_active=True
            )

    for question_answer in question_answers:
        user_answers = SurveyUserAnswer.objects.filter(
            user=user, answer=question_answer
        )[:1]
        if not user_answers:
            user_answer = SurveyUserAnswer()
            user_answer.user = user
            user_answer.answer = question_answer
        else:
            user_answer = user_answers[0]

        if current_question.qtype in ["SO", "CL"]:
            user_answer.uvalue = posted_answers[0]
        else:
            if question_answer.atype == "T":
                user_answer.content = answer_content
            user_answer.uvalue = "0"
            if str(question_answer.id) in posted_answers:
                user_answer.uvalue = "1"

        user_answer.save()


def find_user_by_id(user_id: UUID) -> SurveyUser:
    """Get a user by its UUID."""
    try:
        return SurveyUser.objects.get(user_id=user_id)
    except SurveyUser.DoesNotExist as e:
        logger.error("SurveyUser does not exist.")
        raise e


def get_answer_choices(
    question: SurveyQuestion, lang: str
) -> List[Tuple[int, str]]:
    tuple_answers = []
    translation.activate(lang)

    question_answers = list(
        sorted(
            question.surveyquestionanswer_set.filter(is_active=True),
            key=lambda obj: getattr(obj, question.answers_order)
            if isinstance(getattr(obj, question.answers_order), int)
            else _(str(getattr(obj, question.answers_order))),
        )
    )

    for question_answer in question_answers:
        answer = _(question_answer.label)
        tooltip = _(question_answer.tooltip)

        tuple_answers.append(
            (
                question_answer.value if question.qtype == "SO" else question_answer.id,
                format_html(
                    "{}{}",
                    mark_safe('<span class="checkmark"></span>'),
                    mark_safe(
                        '<span data-bs-toggle="tooltip" title="'
                        + tooltip.replace('"', "&quot;")
                        + '">'
                        + answer
                        + "</span>"
                    ),
                ),
            )
        )

    return tuple_answers


def get_questions_slice(question_index: int):
    survey_questions = SurveyQuestion.objects.exclude(
        section__label__contains="__context"
    ).order_by("qindex")
    total_questions_num = survey_questions.count()
    previous_question = survey_questions[0]
    next_question = None
    current_element_index = 0
    for survey_question in survey_questions:
        if question_index == survey_question.qindex:
            current_question = survey_question
            if current_element_index + 1 < total_questions_num:
                next_question = survey_questions[current_element_index + 1]
            break
        previous_question = survey_question
        current_element_index += 1

    return previous_question, current_question, next_question, total_questions_num


def get_questions_with_user_answers(user: SurveyUser):
    survey_user_answers = (
        SurveyUserAnswer.objects.filter(user=user)
        .exclude(answer__question__section__label="__context")
        .order_by("answer__question__qindex", "answer__aindex")
    )

    user_feedbacks = SurveyUserFeedback.objects.filter(
        user=user, question__isnull=False
    )
    feedbacks_per_question = {}
    for user_feedback in user_feedbacks:
        feedbacks_per_question[user_feedback.question.qindex] = user_feedback.feedback

    questions_with_user_answers: Dict[int, QuestionWithUserAnswers] = {}
    for survey_user_answer in survey_user_answers:
        question_title = _(survey_user_answer.answer.question.label)
        question_index = survey_user_answer.answer.question.qindex
        if question_index not in questions_with_user_answers:
            feedback = ""
            if question_index in feedbacks_per_question:
                feedback = feedbacks_per_question[question_index]
            questions_with_user_answers[question_index] = {
                "question_title": question_title,
                "feedback": feedback,
                "user_answers": [],
            }

        user_answer_content = ""
        if survey_user_answer.answer.atype == "T" and survey_user_answer.uvalue == "1":
            user_answer_content = survey_user_answer.content

        questions_with_user_answers[question_index]["user_answers"].append(
            {
                "value": survey_user_answer.uvalue,
                "content": user_answer_content,
                "title": _(survey_user_answer.answer.label),
            }
        )

    return questions_with_user_answers


def handle_general_feedback(user: SurveyUser, request: HttpRequest) -> GeneralFeedback:
    user_feedback = SurveyUserFeedback.objects.filter(user=user, question__isnull=True)[
        :1
    ]
    if request.method == "POST":
        general_feedback_form = GeneralFeedback(
            data=request.POST, lang=user.chosen_lang
        )

        if general_feedback_form.is_valid():
            if user_feedback:
                user_feedback = user_feedback[0]
            else:
                user_feedback = SurveyUserFeedback()
                user_feedback.user = user

            user_feedback.feedback = general_feedback_form.cleaned_data[
                "general_feedback"
            ]
            user_feedback.save()

            return general_feedback_form
    else:
        general_feedback_form = GeneralFeedback(lang=user.chosen_lang)

    if user_feedback:
        general_feedback_form.set_general_feedback(user_feedback[0].feedback)

    return general_feedback_form
