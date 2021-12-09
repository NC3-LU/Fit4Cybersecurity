# -*- coding: utf-8 -*-

from typing import Union, List, Dict, Tuple, Any
from typing_extensions import TypedDict
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
        user.choosen_lang = lang
    else:
        user.choosen_lang = LOCAL_DEFAULT_LANG
    user.save()
    return user


def handle_start_survey(request: HttpRequest, lang: str) -> Union[Dict, SurveyUser]:
    """Handles the start of the survey."""
    action = "/survey/start/" + lang
    title = CUSTOM["tool_name"] + " - " + _("Let's start")

    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    forms = {}
    questions = SurveyQuestion.objects.filter(
        section__label__contains="__context"
    ).all()
    for question in questions:
        try:
            question_answers = SurveyQuestionAnswer.objects.order_by("aindex").filter(
                question=question
            )
            tuple_answers = get_answer_choices(question_answers, lang)
        except Exception as e:
            raise e
        forms[question.id] = AnswerMChoice(
            tuple_answers,
            data=request.POST,
            lang=lang,
            answers_field_type=question.qtype,
            question_answers=question_answers,
            prefix="form" + str(question.id),
        )

    if request.method == "POST":
        res_forms = {}
        for question in questions:
            try:
                question_answers = SurveyQuestionAnswer.objects.order_by(
                    "aindex"
                ).filter(question=question)
                tuple_answers = get_answer_choices(question_answers, lang)
            except Exception as e:
                raise e

            res_forms[question.id] = AnswerMChoice(
                tuple_answers,
                data=request.POST,
                lang=lang,
                answers_field_type=question.qtype,
                question_answers=question_answers,
                prefix="form" + str(question.id),
            )

        if all([form.is_valid() for question_id, form in res_forms.items()]):
            # create the user
            user = create_user(lang)
            request.session["user_id"] = str(user.user_id)

        for question in questions:
            form = res_forms[question.id]
            answers = form.cleaned_data["answers"]
            answer_content = ""
            if "answer_content" in form.cleaned_data:
                answer_content = form.cleaned_data["answer_content"]

            try:
                question_answers = SurveyQuestionAnswer.objects.order_by(
                    "aindex"
                ).filter(question=question)
                tuple_answers = get_answer_choices(question_answers, lang)
            except Exception as e:
                raise e

            # create the answers
            save_answers(user, question, question_answers, answers, answer_content)

        return user

    return {
        "title": title,
        "forms": forms,
        "action": action,
        "choosen_lang": lang,
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

    nb_context_question = SurveyQuestion.objects.filter(
        section__label__contains="__context"
    ).count()

    try:
        question_answers = SurveyQuestionAnswer.objects.order_by("aindex").filter(
            question=current_question
        )
        tuple_answers = get_answer_choices(question_answers, user.choosen_lang)
    except Exception as e:
        raise e

    free_text_answer_id = 0
    for question_answer in question_answers:
        if question_answer.atype == "T":
            free_text_answer_id = question_answer.id

    translation.activate(user.choosen_lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = user.choosen_lang

    if request.method == "POST":
        form = AnswerMChoice(
            tuple_answers,
            data=request.POST,
            lang=user.choosen_lang,
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

            save_answers(
                user, current_question, question_answers, answers, answer_content
            )

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
            lang=user.choosen_lang,
            answers_field_type=current_question.qtype,
            question_answers=question_answers,
        )

        user_answers = SurveyUserAnswer.objects.filter(
            user=user, answer__question=current_question
        )
        selected_answers = []
        for user_answer in user_answers:
            if user_answer.uvalue > 0:
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
    uniqueAnswers = ",".join(str(uniqueAnswer.id) for uniqueAnswer in uniqueAnswers)
    form.set_unique_answers(uniqueAnswers)
    form.set_free_text_answer_id(free_text_answer_id)

    if current_question.qindex - nb_context_question > 0:
        current_question_qindex = current_question.qindex - nb_context_question
    else:
        current_question_qindex = current_question.qindex

    return {
        "title": CUSTOM["tool_name"]
        + " - "
        + _("Question")
        + " "
        + str(current_question.qindex),
        "question": _(current_question.label),
        "question_tooltip": _(current_question.tooltip),
        "form": form,
        "action": "/survey/question/" + str(current_question.qindex),
        "user": user,
        "current_question_index": current_question_qindex,
        "previous_question_index": previous_question.qindex,
        "total_questions_num": total_questions_num,
    }


def save_answers(
    user: SurveyUser,
    current_question: SurveyQuestion,
    question_answers: List[SurveyQuestionAnswer],
    posted_answers: List[SurveyQuestionAnswer],
    answer_content: str,
) -> None:
    posted_answers_ids = [int(i) for i in posted_answers]
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

        if question_answer.atype == "T":
            user_answer.content = answer_content

        user_answer.uvalue = 0
        if question_answer.id in posted_answers_ids:
            user_answer.uvalue = 1

        user_answer.save()


def find_user_by_id(user_id: UUID) -> SurveyUser:
    return SurveyUser.objects.filter(user_id=user_id)[0]


def get_answer_choices(
    question_answers: List[SurveyQuestionAnswer], user_lang: str
) -> List[Tuple[int, str]]:
    tuple_answers = []
    translation.activate(user_lang)

    for question_answer in question_answers:
        answer = _(question_answer.label)
        tooltip = _(question_answer.tooltip)

        tuple_answers.append(
            (
                question_answer.id,
                format_html(
                    "{}{}",
                    mark_safe('<span class="checkmark"></span>'),
                    mark_safe(
                        '<span data-bs-toggle="tooltip" title="'
                        + tooltip
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
        if survey_user_answer.answer.atype == "T" and survey_user_answer.uvalue == 1:
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
            data=request.POST, lang=user.choosen_lang
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
        general_feedback_form = GeneralFeedback(lang=user.choosen_lang)

    if user_feedback:
        general_feedback_form.set_general_feedback(user_feedback[0].feedback)

    return general_feedback_form
