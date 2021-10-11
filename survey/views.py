from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _
from django import forms
import traceback

from survey.viewLogic import (
    handle_start_survey,
    handle_question_answers_request,
    find_user_by_id,
    get_questions_with_user_answers,
    handle_general_feedback,
)
from survey.reporthelper import calculateResult, createAndSendReport, getRecommendations
from survey.globals import TRANSLATION_UI, MIN_ACCEPTABLE_SCORE, LANG_SELECT
from survey.models import SurveyUser, SURVEY_STATUS_FINISHED
from django.contrib import messages
from django.utils import translation
from uuid import UUID
from csskp.settings import HASH_KEY
from cryptography.fernet import Fernet


def index(request):
    return render(request, "survey/index.html")


def start(request, lang="EN"):
    try:
        form_data = handle_start_survey(request, lang)

        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang

        if isinstance(form_data, SurveyUser):
            return HttpResponseRedirect(
                "/survey/question/" + str(form_data.current_qindex)
            )
    except Exception as e:
        messages.error(request, e)
        messages.error(traceback.format_exc())
        return HttpResponseRedirect("/")

    add_form_translations(form_data, lang, "question")

    return render(request, "survey/start.html", context=form_data)


def handle_question_form(request, question_index: int):
    if request.session.get("user_id", None) is None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(request.session["user_id"])

    if user.is_survey_finished():
        return HttpResponseRedirect("/survey/finish")
    elif user.current_qindex < question_index or question_index <= 0:
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    review_ancher = ""
    if user.is_survey_under_review():
        review_ancher = "#question-" + str(question_index)

    result = handle_question_answers_request(request, user, question_index)

    if type(result) is SurveyUser:
        if result.is_survey_under_review():
            return HttpResponseRedirect("/survey/review" + review_ancher)

        return HttpResponseRedirect("/survey/question/" + str(result.current_qindex))

    add_form_translations(result, user.choosen_lang, "question")

    return render(request, "survey/questions.html", context=result)


def change_lang(request, lang: str):
    user_id = request.session.get("user_id", None)
    if user_id == None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(user_id)
    user.choosen_lang = lang
    user.save()

    if user.is_survey_in_progress():
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    if user.is_survey_under_review():
        return HttpResponseRedirect("/survey/review")

    if user.is_survey_finished():
        return HttpResponseRedirect("/survey/finish")

    return HttpResponseRedirect("/")


def show_report(request, lang):
    user_id = request.session.get("user_id", None)
    if user_id == None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(user_id)

    if not user.is_survey_finished():
        messages.error(
            request, _("To generate a report you have to finish the survey.")
        )

        return HttpResponseRedirect("/")

    try:
        return createAndSendReport(user, lang)
    except Exception as e:
        messages.warning(request, e)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def review(request):
    user_id = request.session.get("user_id", None)
    if user_id == None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(user_id)
    if user.is_survey_finished():
        return HttpResponseRedirect("/survey/finish")
    elif user.is_survey_in_progress():
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    if request.method == "POST" and forms.Form(data=request.POST).is_valid():
        user.status = SURVEY_STATUS_FINISHED
        user.save()

        return HttpResponseRedirect("/survey/finish")

    questions_with_user_answers = get_questions_with_user_answers(user)

    lang = user.choosen_lang
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    textLayout = {
        "questions_with_user_answers": questions_with_user_answers,
        "form": forms.Form(),
        "user": user,
        "translations": {
            "title": TRANSLATION_UI["review"]["title"][lang],
            "validate_answers_button": TRANSLATION_UI["review"][
                "validate_answers_button"
            ][lang],
            "modify_button": TRANSLATION_UI["review"]["modify_button"][lang],
            "feedback_label": TRANSLATION_UI["form"]["questions"]["feedback_label"][
                lang
            ],
            "custom_response": TRANSLATION_UI["form"]["questions"]["custom_response"][
                lang
            ],
            "continue_later": {
                "button": TRANSLATION_UI["question"]["continue_later"]["button"][lang],
                "title": TRANSLATION_UI["question"]["continue_later"]["title"][lang],
                "text": TRANSLATION_UI["question"]["continue_later"]["text"][lang],
                "button_download": TRANSLATION_UI["question"]["continue_later"][
                    "button_download"
                ][lang],
                "button_close": TRANSLATION_UI["question"]["continue_later"][
                    "button_close"
                ][lang],
            },
            "leave_survey": {
                "title": TRANSLATION_UI["question"]["leave_survey"]["title"][lang],
                "yes": TRANSLATION_UI["question"]["leave_survey"]["yes"][lang],
                "no": TRANSLATION_UI["question"]["leave_survey"]["no"][lang],
            },
        },
        "available_langs": [lang[0] for lang in LANG_SELECT],
    }

    return render(request, "survey/review.html", context=textLayout)


def finish(request):
    user_id = request.session.get("user_id", None)
    if user_id == None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(user_id)
    if not user.is_survey_finished():
        return HttpResponseRedirect("/")

    user_lang = user.choosen_lang
    translation.activate(user_lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_lang

    # make survey readonly and show results.
    # also needs saving here!
    # show a "Thank you" and a "get your report" button

    txt_score, radar_current, sections_list = calculateResult(user, user_lang)

    diagnostic_email_body = TRANSLATION_UI["report"]["request_diagnostic"]["email_body"][user_lang]

    recommendations = getRecommendations(user, user_lang)
    # To properly display breaking lines \n on html page.
    for rx in recommendations:
        recommendations[rx] = [x.replace("\n", "<br>") for x in recommendations[rx]]

    textLayout = {
        "title": "Fit4Cybersecurity - " + TRANSLATION_UI["report"]["title"][user_lang],
        "description": TRANSLATION_UI["report"]["description"][user_lang],
        "recommendations": recommendations,
        "user": user,
        "reportlink": "/survey/report",
        "txtscore": txt_score,
        "chartTitles": str(sections_list),
        "chartlabelYou": TRANSLATION_UI["report"]["result"][user_lang],
        "chartdataYou": str(radar_current),
        "min_acceptable_score": MIN_ACCEPTABLE_SCORE,
        "available_langs": [lang[0] for lang in LANG_SELECT],
        "general_feedback_form": handle_general_feedback(user, request),
    }

    add_form_translations(textLayout, user.choosen_lang, "report")

    crypter = Fernet(HASH_KEY)

    textLayout["translations"]["request_diagnostic"] = {
        "title": TRANSLATION_UI["report"]["request_diagnostic"]["title"][user_lang],
        "description": TRANSLATION_UI["report"]["request_diagnostic"]["description"][user_lang],
        "service_fee": TRANSLATION_UI["report"]["request_diagnostic"]["service_fee"][user_lang],
        "email_subject": TRANSLATION_UI["report"]["request_diagnostic"]["email_subject"][user_lang],
        "email_body": diagnostic_email_body.replace("{userId}", str(crypter.encrypt(user_id.encode("utf-8")))),
    }
    textLayout["translations"]["request_training"] = {
        "description": TRANSLATION_UI["report"]["request_training"]["description"][user_lang].replace(
            "{score}", str(txt_score) + "/100"
        ),
        "let_us_know": TRANSLATION_UI["report"]["request_training"]["let_us_know"][user_lang],
        "email_subject": TRANSLATION_UI["report"]["request_training"]["email_subject"][user_lang],
        "email_body": TRANSLATION_UI["report"]["request_training"]["email_body"][user_lang].replace(
            "{userId}", str(crypter.encrypt(user_id.encode("utf-8")))
        ),
    }
    textLayout["translations"]["txtdownload"] = TRANSLATION_UI["report"]["download"][user_lang]
    textLayout["translations"]["txtreport"] = TRANSLATION_UI["report"]["report"][user_lang]
    textLayout["translations"]["general_feedback"] = {
        "button": TRANSLATION_UI["report"]["general_feedback"]["button"][user_lang],
        "title": TRANSLATION_UI["report"]["general_feedback"]["title"][user_lang],
        "button_close": TRANSLATION_UI["report"]["general_feedback"]["button_close"][user_lang],
        "button_send": TRANSLATION_UI["report"]["general_feedback"]["button_send"][user_lang],
    }

    return render(request, "survey/finishedSurvey.html", context=textLayout)


def get_companies(request):
    """Get Companies contained in certain category.
    Returns a company list related to the selected recommendations"""
    return HttpResponse(
        "Here is the JSON list of companies that are related to that category"
    )


def resume(request):
    try:
        user_id = UUID(request.GET.get("user_id"))

        user = find_user_by_id(str(user_id))
    except:
        messages.warning(
            request,
            _(
                "We could not find a survey with the requested key, please start a new one."
            ),
        )
        return HttpResponseRedirect("/")

    request.session["user_id"] = str(user_id)

    if user.is_survey_in_progress():
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    if user.is_survey_under_review():
        return HttpResponseRedirect("/survey/review")

    if user.is_survey_finished():
        return HttpResponseRedirect("/survey/finish")

    return HttpResponseRedirect("/")


def save_general_feedback(request):
    user_id = request.session["user_id"]
    user = find_user_by_id(user_id)
    if not user.is_survey_finished():
        return HttpResponseRedirect("/")

    form = handle_general_feedback(user, request)

    if user.is_survey_finished():
        if form.errors:
            messages.warning(
                request, _("Feedback sending errors: " + form.errors.split(", "))
            )

        return HttpResponseRedirect("/survey/finish")

    if user.is_survey_in_progress():
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    if user.is_survey_under_review():
        return HttpResponseRedirect("/survey/review")

    return HttpResponseRedirect("/")


def add_form_translations(data, lang: str, topic="question"):
    data["translations"] = {
        "continue_later": {
            "button": TRANSLATION_UI[topic]["continue_later"]["button"][lang],
            "title": TRANSLATION_UI[topic]["continue_later"]["title"][lang],
            "text": TRANSLATION_UI[topic]["continue_later"]["text"][lang],
            "button_download": TRANSLATION_UI[topic]["continue_later"][
                "button_download"
            ][lang],
            "button_close": TRANSLATION_UI[topic]["continue_later"]["button_close"][
                lang
            ],
        },
        "leave_survey": {
            "title": TRANSLATION_UI[topic]["leave_survey"]["title"][lang],
            "yes": TRANSLATION_UI[topic]["leave_survey"]["yes"][lang],
            "no": TRANSLATION_UI[topic]["leave_survey"]["no"][lang],
        },
    }

    if "next_button" in TRANSLATION_UI[topic]:
        data["translations"]["next_button"] = TRANSLATION_UI[topic]["next_button"][lang]
    if "back_button" in TRANSLATION_UI[topic]:
        data["translations"]["back_button"] = TRANSLATION_UI[topic]["back_button"][lang]
    if "modify_button" in TRANSLATION_UI[topic]:
        data["translations"]["modify_button"] = TRANSLATION_UI[topic]["modify_button"][
            lang
        ]
    if "cancel_button" in TRANSLATION_UI[topic]:
        data["translations"]["cancel_button"] = TRANSLATION_UI[topic]["cancel_button"][
            lang
        ]
    if "select_multi_descr" in TRANSLATION_UI[topic]:
        data["translations"]["select_multi_descr"] = TRANSLATION_UI[topic][
            "select_multi_descr"
        ][lang]
    if (
        "feedback_descr1" in TRANSLATION_UI[topic]
        and "feedback_descr2" in TRANSLATION_UI[topic]
    ):
        data["translations"]["feedback_descr1"] = TRANSLATION_UI[topic][
            "feedback_descr1"
        ][lang]
        data["translations"]["feedback_descr2"] = TRANSLATION_UI[topic][
            "feedback_descr2"
        ][lang]


def get_terms(request):
    return render(request, "survey/terms.html")
