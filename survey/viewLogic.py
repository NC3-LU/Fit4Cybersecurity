from django.utils.html import format_html, mark_safe
from django.db import transaction
from django.utils import translation

from survey.models import (
    SurveyUser,
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUserAnswer,
    TranslationKey,
    SurveyUserFeedback,
    SURVEY_STATUS_UNDER_REVIEW,
)
from survey.forms import InitialStartForm, AnswerMChoice, GeneralFeedback
from survey.globals import LANG_SELECT, TRANSLATION_UI
from survey.reporthelper import getRecommendations, get_formatted_translations


def create_user(lang: str, sector: str, company_size: str, country: str):
    user = SurveyUser()
    user.sector = sector
    user.e_count = company_size
    user.country_code = country
    survey_question = SurveyQuestion.objects.order_by("qindex")[:1]
    user.current_qindex = survey_question[0].qindex

    # prevent the use of custom languages
    langs = [x[0] for x in LANG_SELECT]
    if lang in langs:
        user.choosen_lang = lang
    else:
        user.choosen_lang = LANG_SELECT[0][0]

    user.save()

    return user


def handle_start_survey(request, lang: str):
    action = "/survey/start/" + lang
    question = TRANSLATION_UI["question"]["description"][lang]
    title = "Fit4Cybersecurity - " + TRANSLATION_UI["question"]["title"][lang]

    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    if request.method == "POST":
        form = InitialStartForm(data=request.POST, lang=lang)

        if form.is_valid():
            user = create_user(
                lang,
                form.cleaned_data["sector"],
                form.cleaned_data["compSize"],
                form.cleaned_data["country"],
            )

            request.session["user_id"] = str(user.user_id)

            return user
    else:
        form = InitialStartForm(lang=lang)

    return {
        "title": title,
        "question": question,
        "form": form,
        "action": action,
        "choosen_lang": lang,
    }


def handle_question_answers_request(request, user: SurveyUser, question_index: int):
    (
        previous_question,
        current_question,
        next_question,
        total_questions_num,
    ) = get_questions_slice(question_index)

    try:
        tuple_answers = get_answer_choices(current_question, user.choosen_lang)
    except Exception as e:
        raise e

    translation.activate(user.choosen_lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = user.choosen_lang

    if request.method == "POST":
        form = AnswerMChoice(
            tuple_answers,
            data=request.POST,
            lang=user.choosen_lang,
            answers_field_type=current_question.qtype,
        )

        if form.is_valid():
            with transaction.atomic():
                user = SurveyUser.objects.select_for_update(nowait=True).filter(id=user.id)[0]
                answers = form.cleaned_data["answers"]
                save_answers(tuple_answers, answers, user)

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

                if next_question != None:
                    user.current_qindex = next_question.qindex
                else:
                    user.status = SURVEY_STATUS_UNDER_REVIEW

                user.save()

                return user
    else:
        user_answers = SurveyUserAnswer.objects.filter(
            user=user, answer__question=current_question, uvalue__gt=0
        )
        selected_answers = []
        for user_answer in user_answers:
            selected_answers.append(user_answer.answer.id)

        user_feedback = SurveyUserFeedback.objects.filter(
            user=user, question=current_question
        )[:1]

        form = AnswerMChoice(
            tuple_answers,
            lang=user.choosen_lang,
            answers_field_type=current_question.qtype,
        )
        form.set_answers(selected_answers)
        if user_feedback:
            form.set_feedback(user_feedback[0].feedback)

    uniqueAnswers = SurveyQuestionAnswer.objects.filter(
        question=current_question, uniqueAnswer=True
    )
    uniqueAnswers = ",".join(str(uniqueAnswer.id) for uniqueAnswer in uniqueAnswers)
    form.set_unique_answers(uniqueAnswers)

    return {
        "title": "Fit4Cybersecurity - "
        + TRANSLATION_UI["question"]["question"][user.choosen_lang]
        + " "
        + str(current_question.qindex),
        "question": TranslationKey.objects.filter(
            key=current_question.titleKey, lang=user.choosen_lang
        )[0].text,
        "form": form,
        "action": "/survey/question/" + str(current_question.qindex),
        "user": user,
        "current_question_index": current_question.qindex,
        "previous_question_index": previous_question.qindex,
        "total_questions_num": total_questions_num,
        "available_langs": [lang[0] for lang in LANG_SELECT],
    }


def save_answers(answer_choices, answers, user: SurveyUser):
    existing_answer_ids = [int(i[0]) for i in answer_choices]
    user_answers = [int(i) for i in answers]
    for a in existing_answer_ids:
        answer = SurveyUserAnswer.objects.filter(user=user, answer__id=a)[:1]
        if not answer:
            answer = SurveyUserAnswer()
            answer.user = user
            qanswer = SurveyQuestionAnswer.objects.filter(id=a)[:1]
            answer.answer = qanswer[0]
        else:
            answer = answer[0]

        answer.uvalue = 0
        if a in user_answers:
            answer.uvalue = 1

        answer.save()


def find_user_by_id(user_id):
    return SurveyUser.objects.filter(user_id=user_id)[0]


def get_answer_choices(survey_question: SurveyQuestion, user_lang: str):
    tuple_answers = []
    answer_choices = SurveyQuestionAnswer.objects.order_by("aindex").filter(
        question=survey_question
    )

    for answer_choice in answer_choices:
        translation_key = TranslationKey.objects.filter(
            lang=user_lang, key=answer_choice.answerKey
        )
        if translation_key.count() == 0:
            raise Exception(
                "The translation has to be done for the answers choices. "
                + "Please choose an another language."
            )

        tuple_answers.append(
            (
                answer_choice.id,
                format_html(
                    "{}{}",
                    mark_safe('<span class="checkmark"></span>'),
                    translation_key[0].text,
                ),
            )
        )

    return tuple_answers


def get_questions_slice(question_index: int):
    survey_questions = SurveyQuestion.objects.order_by("qindex")
    total_questions_num = len(survey_questions)
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
    survey_user_answers = SurveyUserAnswer.objects.filter(user=user).order_by(
        "answer__question__qindex", "answer__aindex"
    )
    questions_translations = get_formatted_translations(user.choosen_lang, "Q")
    answers_translations = get_formatted_translations(user.choosen_lang, "A")

    user_feedbacks = SurveyUserFeedback.objects.filter(
        user=user, question__isnull=False
    )
    feedbacks_per_question = {}
    for user_feedback in user_feedbacks:
        feedbacks_per_question[user_feedback.question.qindex] = user_feedback.feedback

    questions_with_user_answers = {}
    for survey_user_answer in survey_user_answers:
        question_title = questions_translations[
            survey_user_answer.answer.question.titleKey
        ]
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

        questions_with_user_answers[question_index]["user_answers"].append(
            {
                "value": survey_user_answer.uvalue,
                "title": answers_translations[survey_user_answer.answer.answerKey],
            }
        )

    return questions_with_user_answers


def handle_general_feedback(user: SurveyUser(), request):
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
