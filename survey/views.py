# -*- coding: utf-8 -*-

import json
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext as _
from django import forms

from survey.viewLogic import (
    handle_start_survey,
    handle_question_answers_request,
    find_user_by_id,
    get_questions_with_user_answers,
    handle_general_feedback,
)
from survey.reporthelper import calculateResult, getRecommendations
from survey.report import create_html_report, makepdf
from survey.models import SurveyUser, SURVEY_STATUS_FINISHED
from utils.notifications import send_report
from django.contrib import messages
from django.utils import translation
from uuid import UUID
from csskp.settings import HASH_KEY, CUSTOM, LANGUAGE_CODE
from cryptography.fernet import Fernet


def index(request, lang=LANGUAGE_CODE):
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
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
        return HttpResponseRedirect("/")

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

    return render(request, "survey/questions.html", context=result)


def change_lang(request, lang: str):
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    user_id = request.session.get("user_id", None)
    previous_path = request.META.get("HTTP_REFERER", "/")

    if previous_path.__contains__("/survey/start/"):
        return HttpResponseRedirect("/survey/start/" + lang)

    if user_id is None:
        return HttpResponseRedirect("/" + lang)

    user = find_user_by_id(user_id)
    user.choosen_lang = lang
    user.save()

    user = find_user_by_id(user_id)
    user.choosen_lang = lang
    user.save()

    if user.is_survey_in_progress() and previous_path.__contains__("/survey/question/"):
        return HttpResponseRedirect("/survey/question/" + str(user.current_qindex))

    if user.is_survey_under_review() and previous_path.__contains__("/survey/review"):
        return HttpResponseRedirect("/survey/review")

    if user.is_survey_finished() and previous_path.__contains__("/survey/finish"):
        return HttpResponseRedirect("/survey/finish")

    return HttpResponseRedirect("/" + lang)


def show_report(request, lang: str) -> HttpResponseRedirect:
    user_id = request.session.get("user_id", None)
    if user_id is None:
        return HttpResponseRedirect("/")

    user = find_user_by_id(user_id)

    if not user.is_survey_finished():
        messages.error(
            request, _("To generate a report you have to finish the survey.")
        )

        return HttpResponseRedirect("/")

    # Generation of the PDF report
    try:
        html_report = create_html_report(user, lang)
        pdf_report = makepdf(html_report)
    except Exception as e:
        # todo: handle exception
        messages.warning(request, e)

    # Try to get the email address in case the user wants to send the report
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email_address = body.get("email-address", None)
    except Exception:
        email_address = None

    if CUSTOM["modules"]["reportEmail"] and email_address:
        # Send the report via email
        send_report(email_address, pdf_report)
    else:
        # Return the report in the HTTP answer
        response = HttpResponse(pdf_report, content_type="application/pdf")
        response["Content-Disposition"] = "attachment;filename=Report{}_{}.pdf".format(
            CUSTOM["tool_name"], date.today()
        )
        return response

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def review(request):
    user_id = request.session.get("user_id", None)
    if user_id is None:
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
        "title": CUSTOM["tool_name"] + " - " + _("Answers review"),
        "questions_with_user_answers": questions_with_user_answers,
        "form": forms.Form(),
        "user": user,
    }

    return render(request, "survey/review.html", context=textLayout)


def finish(request):
    crypter = Fernet(HASH_KEY)
    user_id = request.session.get("user_id", None)
    if user_id is None:
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

    recommendations = getRecommendations(user, user_lang)
    # To properly display breaking lines \n on html page.
    for rx in recommendations:
        recommendations[rx] = [x.replace("\n", "<br>") for x in recommendations[rx]]

    textLayout = {
        "title": CUSTOM["tool_name"] + " - " + _("Final summary"),
        "recommendations": recommendations,
        "user": user,
        "userId": str(crypter.encrypt(user_id.encode("utf-8"))),
        "reportlink": "/survey/report",
        "txtscore": txt_score,
        "string_score": str(txt_score),
        "chartTitles": str(sections_list),
        "chartdataYou": str(radar_current),
        "general_feedback_form": handle_general_feedback(user, request),
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

        user = find_user_by_id(user_id)
    except Exception:
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


def get_terms(request):
    return render(request, "survey/terms.html")
