import logging
import math
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from uuid import UUID

from django.db import transaction
from django.db.models import Max
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils import translation
from django.utils.html import format_html
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from typing_extensions import TypedDict

from csskp.settings import CUSTOM
from csskp.settings import LANGUAGE_CODE
from csskp.settings import LANGUAGES
from survey.forms import AnswerMChoice
from survey.forms import GeneralFeedback
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import SURVEY_STATUS_IN_PROGRESS
from survey.models import SURVEY_STATUS_UNDER_REVIEW
from survey.models import SurveyAnswerQuestionMap
from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.models import SurveyUserFeedback
from survey.models import SurveyUserQuestionSequence

LOCAL_DEFAULT_LANG = LANGUAGE_CODE

# Get an instance of a logger
logger = logging.getLogger(__name__)


class QuestionWithUserAnswers(TypedDict):
    """Defines a type for a question with user answers"""

    question_title: str
    feedback: str
    user_answers: list[Any]


def create_user_and_sequence(lang: str) -> SurveyUser:
    """Creates a new SurveyUser object.
    This function is called by the function handle_start_surveyonce, once the user has
    answered the first questions before the start of the survey."""
    user = SurveyUser()
    # defines the next question (exclude the context questions)
    survey_question = SurveyQuestion.objects.exclude(
        section__label__contains=CONTEXT_SECTION_LABEL
    ).order_by("qindex")[:1]
    user.current_question = survey_question[0]
    # Ensures the submitted languages is accepted
    langs, _ = zip(*LANGUAGES)
    if lang in langs:
        user.chosen_lang = lang
    else:
        user.chosen_lang = LOCAL_DEFAULT_LANG
    user.save()

    # We recreate the entire questions sequence in case if the map is not defined.
    if not does_answers_questions_map_exist():
        for question in (
            SurveyQuestion.objects.filter(is_active=True)
            .exclude(section__label=CONTEXT_SECTION_LABEL)
            .order_by("qindex")
        ):
            create_questions_sequence_object(user, question, question.qindex)
    else:
        create_questions_sequence_object(user, user.current_question, 1)

    return user


def create_questions_sequence_object(
    user: SurveyUser, question: SurveyQuestion, index: int
) -> None:
    user_question_sequence = SurveyUserQuestionSequence()
    user_question_sequence.user = user
    user_question_sequence.question = question
    user_question_sequence.index = index
    user_question_sequence.save()


@transaction.atomic
def handle_start_survey(request: HttpRequest, lang: str) -> Union[Dict, SurveyUser]:
    """Handles the start of the survey."""
    title = CUSTOM["tool_name"] + " - " + _("Let's start")

    forms = {}
    questions = (
        SurveyQuestion.objects.filter(section__label__contains=CONTEXT_SECTION_LABEL)
        .order_by("-qindex")
        .all()
    )

    # if no context questions: create the user without the form
    if not questions.count() and request.method == "GET":
        user = create_user_and_sequence(lang)
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
            user = create_user_and_sequence(lang)
            request.session["user_id"] = str(user.user_id)

            for question in questions:
                form = forms[question.id]
                answers = form.cleaned_data["answers"]
                answer_content = ""
                if "answer_content" in form.cleaned_data:
                    answer_content = form.cleaned_data["answer_content"]

                save_answers(
                    user, question, None, question.qindex, answers, answer_content
                )

            return user

    return {
        "title": title,
        "forms": forms,
        "questions_per_id": {question.id: _(question.label) for question in questions},
        "action": "/survey/start",
        "chosen_lang": lang,
    }


@transaction.atomic
def handle_question_answers_request(
    request: HttpRequest, user: SurveyUser, question_index: int
) -> Union[Dict, SurveyUser]:
    current_sequence = get_sequence_by_user_and_index(user, question_index)
    current_question = current_sequence.question
    does_map_exist = does_answers_questions_map_exist()

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

            save_answers(
                user,
                current_question,
                current_sequence,
                question_index,
                answers,
                answer_content,
            )

            feedback = form.cleaned_data["feedback"]
            if feedback:
                save_feedback(user, current_question, feedback)

            was_sequence_question_answered = current_sequence.has_been_answered
            mark_sequence_as_answered(current_sequence)
            next_sequence = get_next_sequence_with_not_answered_question(
                user, question_index, current_sequence
            )

            if next_sequence is not None:
                if (
                    does_map_exist
                    and not was_sequence_question_answered
                    and next_sequence.index != question_index + 1
                ):
                    increment_questions_sequence_order_from(user, question_index, 0, 1)

                user.current_question = next_sequence.question
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
        "title": CUSTOM["tool_name"]
        + " - "
        + _("Question")
        + " "
        + str(question_index),
        "question": _(current_question.label),
        "question_tooltip": _(current_question.tooltip),
        "form": form,
        "action": "/survey/question/" + str(question_index),
        "user": user,
        "current_question_index": question_index,
        "previous_question_index": question_index - 1 if question_index > 1 else 1,
        "total_questions_num": get_total_questions_number(user, question_index),
        "show_warning_dialog": current_sequence.has_been_answered and does_map_exist,
    }


def save_answers(
    user: SurveyUser,
    current_question: SurveyQuestion,
    current_sequence: Optional[SurveyUserQuestionSequence],
    question_index: int,
    posted_answers: List[Union[int, str]],
    answer_content: str,
) -> None:
    does_map_exist = does_answers_questions_map_exist()
    if current_sequence is not None:
        current_branch = current_sequence.branch

    match current_question.qtype:
        case "SO":
            selected_value = posted_answers[0]
            question_answers = [
                current_question.surveyquestionanswer_set.get(
                    is_active=True, value=selected_value
                )
            ]
        case "CL":
            question_answers = [current_question.surveyquestionanswer_set.all()[0]]
        case _:
            question_answers = current_question.surveyquestionanswer_set.filter(
                is_active=True
            ).order_by(current_question.answers_order)

    for index, question_answer in enumerate(question_answers):
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
            posted_answers = [int(i) for i in posted_answers]
            # for the first question we take branch from the question number.
            if does_map_exist and current_sequence is not None and question_index == 1:
                # The first question defines branch(es) number(s) to proceed with.
                if (
                    "is_single_branch_tree" in CUSTOM
                    and CUSTOM["is_single_branch_tree"]
                ):
                    current_branch = 0
                else:
                    current_branch = index + 1

            is_answer_selected = question_answer.id in posted_answers
            is_answer_changed = (user_answer.uvalue == "0" and is_answer_selected) or (
                user_answer.uvalue == "1" and not is_answer_selected
            )
            # if we modify the question and answer is unselected.
            if (
                does_map_exist
                and current_sequence is not None
                and current_sequence.has_been_answered
                and not is_answer_selected
                and is_answer_changed
            ):
                remove_questions_sequences(
                    user,
                    user_answer.answer,
                    question_index,
                    current_sequence,
                    posted_answers,
                )

            if question_answer.atype == "T":
                user_answer.content = answer_content
            user_answer.uvalue = "0"
            if is_answer_selected:
                user_answer.uvalue = "1"
                if (
                    does_map_exist
                    and current_sequence is not None
                    and is_answer_changed
                ):
                    create_questions_sequence(
                        user,
                        user_answer.answer,
                        current_branch,
                        question_index,
                        posted_answers,
                    )

        user_answer.save()


def save_feedback(user: SurveyUser, question: SurveyQuestion, feedback: str) -> None:
    user_feedback = SurveyUserFeedback.objects.filter(user=user, question=question)[:1]
    if not user_feedback:
        user_feedback = SurveyUserFeedback()
        user_feedback.user = user
        user_feedback.question = question
    else:
        user_feedback = user_feedback[0]
    user_feedback.feedback = feedback
    user_feedback.save()


def create_questions_sequence(
    user: SurveyUser,
    question_answer: SurveyQuestionAnswer,
    current_branch: int,
    question_index: int,
    posted_answers: List[Union[int, str]],
):
    answer_questions_map = SurveyAnswerQuestionMap.objects.filter(
        answer=question_answer
    ).order_by("branch", "order")
    for answer_question_map in answer_questions_map:
        sequence = get_active_sequence_by_user_and_question(
            user, answer_question_map.question
        )
        number_of_questions_in_user_sequence = get_number_of_questions_in_user_sequence(
            user
        )

        """In case if the question is already added in one of the further branches.
        We need to deactivate the other sequence and create another one in the next position."""
        if (
            sequence is not None
            and not sequence.has_been_answered
            and sequence.branch > current_branch
            and (
                not answer_question_map.branch
                or current_branch == answer_question_map.branch
            )
        ):
            increment_questions_sequence_order_from(
                user, question_index, sequence.index, 2
            )
            save_question_sequence_and_validate_user_status(
                user,
                sequence.question,
                question_index + 1,
                current_branch,
                sequence.level,
            )
            # inactivate the sequence in the future branch
            # to be able to validate its answers later.
            sequence.is_active = False
            sequence.index = 0
            sequence.save()

            continue

        """Normal scenario of adding questions to the sequence.
        if map.branch == current_branch or if the map is general (branch = 0)."""
        if sequence is None and (
            not answer_question_map.branch
            or current_branch == answer_question_map.branch
        ):
            save_question_sequence_and_validate_user_status(
                user,
                answer_question_map.question,
                number_of_questions_in_user_sequence + 1,
                current_branch,
                answer_question_map.level,
            )

            continue

        """In case if the answer leads to another branch (the map is related to another branch)."""
        if sequence is None and answer_question_map.branch:
            if answer_question_map.branch in get_list_of_available_branches(
                user, posted_answers, question_index
            ):
                save_question_sequence_and_validate_user_status(
                    user,
                    answer_question_map.question,
                    number_of_questions_in_user_sequence + 1,
                    answer_question_map.branch,
                    answer_question_map.level,
                )
                continue

        """In case if we modify a question answer from 0 to 1 and related questions
        are already answered, but not in this branch, -> we go deeper through the answers."""
        if sequence and sequence.branch != current_branch:
            answers = SurveyUserAnswer.objects.filter(
                user=user, answer__question=sequence.question
            )
            for answer in answers:
                if answer.uvalue == "1":
                    create_questions_sequence(
                        user,
                        answer.answer,
                        current_branch,
                        number_of_questions_in_user_sequence,
                        posted_answers,
                    )


def remove_questions_sequences(
    user: SurveyUser,
    question_answer: SurveyQuestionAnswer,
    question_index: int,
    current_sequence: SurveyUserQuestionSequence,
    posted_answers: List[Union[int, str]],
) -> None:
    sequences_to_remove = []
    """Validates all the sequences starting from the first index,
    because there is no reference on it."""
    sequences_to_validate = SurveyUserQuestionSequence.objects.filter(
        user=user, index__gt=1, is_active=True
    )
    for sequence_to_validate in sequences_to_validate:
        """Fetch the other answers to validate if they are referenced to the sequence,
        or currently selected answers as they are not saved yet."""
        other_user_answers = (
            SurveyUserAnswer.objects.filter(user=user, uvalue="1")
            .exclude(
                answer=question_answer,
                answer__question__section__label=CONTEXT_SECTION_LABEL,
            )
            .order_by("id")
        )
        if not is_question_referenced_to_user_answers(
            user,
            other_user_answers,
            current_sequence.question,
            sequence_to_validate.question,
            posted_answers,
            question_index,
        ):
            sequences_to_remove.append(sequence_to_validate)

    for num, sequence_to_remove in enumerate(sequences_to_remove):
        """The index is shifted, so we need to subtract the iteration number."""
        index_to_adjust_from = sequence_to_remove.index - num
        SurveyUserAnswer.objects.filter(
            user=user, answer__question=sequence_to_remove.question
        ).delete()
        should_user_question_be_reset = (
            user.current_question.id == sequence_to_remove.question.id
        )
        increment_questions_sequence_order_from(user, index_to_adjust_from, 0, 0)
        sequence_to_remove.delete()
        if should_user_question_be_reset:
            next_sequence = get_next_sequence_with_not_answered_question(
                user, question_index, current_sequence
            )
            if next_sequence is None:
                next_sequence = get_last_user_sequence(user)
            user.current_question = next_sequence.question


def is_question_referenced_to_user_answers(
    user: SurveyUser,
    user_answers: QuerySet,
    current_question: SurveyQuestion,
    question: SurveyQuestion,
    posted_answers: List[Union[int, str]],
    question_index: int,
) -> bool:
    list_of_available_branches = get_list_of_available_branches(
        user, posted_answers, question_index, question
    )
    """We need to take into account the currently modifying question's answers."""
    answers = [user_answer.answer for user_answer in user_answers] + list(
        SurveyQuestionAnswer.objects.filter(id__in=posted_answers)
    )
    for answer in answers:
        answer_questions_map = SurveyAnswerQuestionMap.objects.filter(
            answer=answer, question=question
        )
        for answer_question_map in answer_questions_map:
            """Validates the posted_answers, because they are not saved yet."""
            if (
                current_question.id == answer.question.id
                and answer_question_map.answer.question.id == answer.question.id
                and answer.id not in posted_answers
            ):
                continue

            if not answer_question_map.branch:
                return True

            if answer_question_map.branch in list_of_available_branches:
                return True

    return False


def save_question_sequence_and_validate_user_status(
    user: SurveyUser, question: SurveyQuestion, index: int, branch: int, level: int
) -> None:
    user_question_sequence = SurveyUserQuestionSequence.objects.filter(
        user=user, question=question, branch=branch
    )[:1]
    if not user_question_sequence:
        user_question_sequence = SurveyUserQuestionSequence()
        user_question_sequence.user = user
        user_question_sequence.question = question
        user_question_sequence.index = index
        user_question_sequence.branch = branch
        user_question_sequence.level = level
        user_question_sequence.save()
    else:
        user_question_sequence = user_question_sequence[0]
        user_question_sequence.is_active = True
        user_question_sequence.index = index
        user_question_sequence.save()
    if user.status == SURVEY_STATUS_UNDER_REVIEW:
        user.status = SURVEY_STATUS_IN_PROGRESS
        user.save()


def find_user_by_id(user_id: UUID) -> SurveyUser:
    """Get a user by its UUID."""
    try:
        return SurveyUser.objects.get(user_id=user_id)
    except SurveyUser.DoesNotExist as e:
        logger.error("SurveyUser does not exist.")
        raise e


def get_answer_choices(question: SurveyQuestion, lang: str) -> List[Tuple[int, str]]:
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


def get_questions_with_user_answers(user: SurveyUser):
    survey_user_answers = (
        SurveyUserAnswer.objects.filter(user=user)
        .exclude(answer__question__section__label=CONTEXT_SECTION_LABEL)
        .order_by("answer__question__qindex", "answer__aindex")
    )

    answered_questions_sequences = get_answered_questions_sequences(user)

    user_feedbacks = SurveyUserFeedback.objects.filter(
        user=user, question__isnull=False
    )
    feedbacks_per_question = {}
    for user_feedback in user_feedbacks:
        question_index = user_feedback.question.qindex
        for answered_question_sequence in answered_questions_sequences:
            if answered_question_sequence.question.id == user_feedback.question.id:
                question_index = answered_question_sequence.index
                break

        feedbacks_per_question[question_index] = user_feedback.feedback

    questions_with_user_answers: Dict[int, QuestionWithUserAnswers] = {}
    for survey_user_answer in survey_user_answers:
        question_title = _(survey_user_answer.answer.question.label)
        question_index = survey_user_answer.answer.question.qindex
        for answered_question_sequence in answered_questions_sequences:
            if (
                answered_question_sequence.question.id
                == survey_user_answer.answer.question.id
            ):
                question_index = answered_question_sequence.index
                break

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

    return {k: v for k, v in sorted(questions_with_user_answers.items())}


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


def get_current_user_question_index_from_sequence(user: SurveyUser) -> int:
    user_question_sequence = SurveyUserQuestionSequence.objects.filter(
        user=user, question=user.current_question, is_active=True
    )
    if user_question_sequence:
        return user_question_sequence[0].index
    else:
        return 0


def get_sequence_by_user_and_index(
    user: SurveyUser, index: int
) -> SurveyUserQuestionSequence:
    return SurveyUserQuestionSequence.objects.filter(user=user, index=index)[:1][0]


def get_active_sequence_by_user_and_question(
    user: SurveyUser, question: SurveyQuestion
) -> Optional[SurveyUserQuestionSequence]:
    sequence = SurveyUserQuestionSequence.objects.filter(
        user=user, question=question, is_active=True
    )[:1]
    if sequence:
        return sequence[0]

    return None


def get_number_of_questions_in_user_sequence(user) -> int:
    return SurveyUserQuestionSequence.objects.filter(user=user, is_active=True).count()


def get_next_sequence_with_not_answered_question(
    user: SurveyUser, question_index: int, current_sequence: SurveyUserQuestionSequence
) -> Optional[SurveyUserQuestionSequence]:
    questions_sequence = (
        SurveyUserQuestionSequence.objects.filter(
            user=user, has_been_answered=False, is_active=True
        )
        .exclude(id=current_sequence.id)
        .order_by("branch", "level", "index")[:1]
    )
    if questions_sequence:
        return questions_sequence[0]

    return None


def get_answered_questions_sequences(
    user: SurveyUser,
) -> List[SurveyUserQuestionSequence]:
    return SurveyUserQuestionSequence.objects.filter(
        user=user, has_been_answered=True, is_active=True
    ).order_by("branch", "level", "index")


def mark_sequence_as_answered(sequence: SurveyUserQuestionSequence) -> None:
    if not sequence.has_been_answered:
        sequence.has_been_answered = True
        sequence.save()


def has_user_answered_on_the_question(
    user: SurveyUser, question: SurveyQuestion
) -> bool:
    return SurveyUserQuestionSequence.objects.filter(
        user=user, question=question, has_user_answered_on_the_question=True
    ).exists()


def increment_questions_sequence_order_from(
    user: SurveyUser, question_index: int, index_limit: int, increment: int
) -> None:
    """Shifts the sequences indexes.
    To reduce the indexes sequence index_limit and increment params can be 0.
    """
    questions_sequence = SurveyUserQuestionSequence.objects.filter(
        user=user, is_active=True, index__gt=question_index
    ).order_by("branch", "level", "index")
    if index_limit:
        questions_sequence = questions_sequence.filter(index__lt=index_limit)
    for question_sequence in questions_sequence:
        question_sequence.index = question_index + increment
        increment += 1
        question_sequence.save()


def get_total_questions_number(user: SurveyUser, question_index: int) -> int:
    if not SurveyAnswerQuestionMap.objects.exists():
        return SurveyUserQuestionSequence.objects.filter(
            user=user, is_active=True
        ).count()

    if (
        "is_simple_questionnaire_tree" in CUSTOM
        and CUSTOM["is_simple_questionnaire_tree"]
    ):
        return (
            SurveyAnswerQuestionMap.objects.filter(
                branch=get_last_user_sequence(user).branch
            )
            .order_by("question")
            .distinct("question")
            .count()
            + 1
        )

    branches_number = SurveyAnswerQuestionMap.objects.aggregate(Max("branch"))[
        "branch__max"
    ]
    if question_index > 1:
        branches_number = (
            SurveyUserQuestionSequence.objects.filter(
                user=user, is_active=True, branch__isnull=False
            )
            .values("branch")
            .distinct()
            .count()
        )
    total_questions_num = (
        SurveyAnswerQuestionMap.objects.values("question").distinct().count()
    )
    total_questions_num = int(math.ceil(total_questions_num * 5 / branches_number))
    if total_questions_num <= question_index:
        total_questions_num = question_index + 1

    return total_questions_num


def get_last_user_sequence(user: SurveyUser) -> SurveyUserQuestionSequence:
    return SurveyUserQuestionSequence.objects.filter(
        user=user, is_active=True
    ).order_by("-index")[:1][0]


def get_related_inactive_instances(
    sequence: SurveyUserQuestionSequence,
) -> List[SurveyUserQuestionSequence]:
    return SurveyUserQuestionSequence.objects.filter(
        user=sequence.user, answer=sequence.answer, is_active=False
    )


def get_list_of_available_branches(
    user: SurveyUser,
    posted_answers: List[Union[int, str]],
    question_index: int,
    exclude_question: Optional[SurveyQuestion] = None,
) -> List[SurveyUserQuestionSequence]:
    query = SurveyUserQuestionSequence.objects.filter(
        user=user, is_active=True
    ).exclude(branch=0)
    if exclude_question:
        query = query.exclude(question=exclude_question)

    available_branches = list(
        query.values("branch").distinct().values_list("branch", flat=True)
    )

    """The 1st question's answers are the branches definitions."""
    first_question = SurveyQuestion.objects.get(qindex=1)
    """if we modify the 1st question the posted answers has to be used as they are not saved yet."""
    if question_index == 1:
        first_question_selected_answers = posted_answers
    else:
        survey_user_answers = SurveyUserAnswer.objects.filter(
            user=user, answer__question=first_question, uvalue="1"
        )
        first_question_selected_answers = [ua.answer.id for ua in survey_user_answers]
    for index, answer in enumerate(
        SurveyQuestionAnswer.objects.filter(question=first_question).order_by(
            first_question.answers_order
        )
    ):
        branch = index + 1
        """Compare first questions answers and add the branch respectful their order."""
        if (
            branch not in available_branches
            and answer.id in first_question_selected_answers
        ):
            available_branches.append(branch)

    return available_branches


def does_answers_questions_map_exist() -> bool:
    return SurveyAnswerQuestionMap.objects.exists()
