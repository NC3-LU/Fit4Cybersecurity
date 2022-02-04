# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from operator import itemgetter
from dateutil.relativedelta import relativedelta
from django.conf.global_settings import LANGUAGES
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _
from csskp.settings import CUSTOM, LANGUAGE_CODE
from survey.lib.utils import tree, mean_gen
from survey.models import SurveyUser, SurveyUserAnswer
from survey.reporthelper import calculateResult
from django_countries import countries


def index(request):
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    try:
        first_survey = SurveyUser.objects.filter(status=3).order_by("created_at")[0]
    except Exception:
        first_survey = ""
    nb_surveys = SurveyUser.objects.count()
    context = {
        "nb_surveys": nb_surveys,
        "first_survey_date": getattr(first_survey, "created_at", False),
        "nb_finished_surveys": nb_finished_surveys,
        "python_version": "{}.{}.{}".format(*sys.version_info[:3]),
    }

    return render(request, "survey/stats.html", context=context)


def overall(request):
    """Returns the page which will display some statistics."""
    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    nb_surveys = SurveyUser.objects.count()
    last_surveys = SurveyUser.objects.filter(status=3).order_by("-created_at")[:10]
    survey_results = {user.id: calculateResult(user)[0] for user in last_surveys}
    result = {
        "nb_surveys": nb_surveys,
        "nb_finished_surveys": nb_finished_surveys,
        "survey_results": survey_results,
    }

    return JsonResponse(result)


def survey_status_count(request):
    """Returns the count for the SurveyUser status property."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    result = SurveyUser.objects.values("status").annotate(count=Count("status"))
    status = {1: _("In progress"), 2: _("Under review"), 3: _("Finished")}
    return JsonResponse(
        {status[item["status"]]: item["count"] for item in result.all()}
    )


def survey_language_count(request):
    """Returns the count for the SurveyUser chosen_lang property."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    result = SurveyUser.objects.values("chosen_lang").annotate(
        count=Count("chosen_lang")
    )
    return JsonResponse(
        {
            str(
                _([lang for lang in LANGUAGES if lang[0] == item["chosen_lang"]][0][1])
            ): item["count"]
            for item in result.all()
        }
    )


def survey_context(request):
    """Return the surveys context (country, size, sector)"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    result = tree()

    sector_query = (
        SurveyUserAnswer.objects.filter(
            answer__question__section__label="__context",
            answer__question__label="What is your sector?",
        )
        .values("answer__label")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )
    sector_keys = list(map(itemgetter("answer__label"), sector_query))
    sector_values = list(map(itemgetter("count"), sector_query))
    result["sectors"] = {_(k): v for k, v in zip(sector_keys, sector_values)}

    size_query = (
        SurveyUserAnswer.objects.filter(
            answer__question__section__label="__context",
            answer__question__label="How many employees?",
        )
        .values("answer__label")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )
    size_keys = list(map(itemgetter("answer__label"), size_query))
    size_values = list(map(itemgetter("count"), size_query))
    result["company_sizes"] = {_(k): v for k, v in zip(size_keys, size_values)}

    country_query = (
        SurveyUserAnswer.objects.filter(
            answer__question__section__label="__context",
            answer__question__label="Please select your country",
        )
        .values("uvalue")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )
    country_keys = list(map(itemgetter("uvalue"), country_query))
    country_values = list(map(itemgetter("count"), country_query))
    result["countries"] = {
        _(dict(countries)[k]): v for k, v in zip(country_keys, country_values)
    }

    return JsonResponse(result)


def survey_per_country(request):
    """Return the count the surveys per country"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    users = SurveyUser.objects.all()

    result: dict[str, int] = dict()
    for user in users:
        country = _(dict(countries)[user.get_country_code()])
        result[country] = result.get(country, 0) + 1
    return JsonResponse(result)


def survey_per_company_size(request):
    """Return the count the surveys per company size"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    users = SurveyUser.objects.all()

    result: dict[str, int] = dict()
    for user in users:
        company_size = _(user.get_employees_number_label())
        result[company_size] = result.get(company_size, 0) + 1
    return JsonResponse(result)


def survey_per_company_sector(request):
    """Return the count the surveys per company sector"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    users = SurveyUser.objects.all()

    result: dict[str, int] = dict()
    for user in users:
        company_sector = _(user.get_sector_label())
        result[company_sector] = result.get(company_sector, 0) + 1
    return JsonResponse(result)


def answers_per_section(request):
    """Return a dict with the mean of the user's answers per section, with the
    surveys completed during the last month."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    chart_exclude_sections = ["__context"]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

    one_month_ago = datetime.now() - relativedelta(months=1)
    users = SurveyUser.objects.filter(status=3, created_at__gt=one_month_ago)

    result = tree()
    generators = tree()
    for user in users:
        _, _, user_evaluations, sections = calculateResult(user)
        employees_number_code = user.get_employees_number_label()
        for index, section in enumerate(sections):
            section_label = str(section)
            if section not in generators.get(employees_number_code, {}):
                generators[employees_number_code][section_label] = mean_gen()
                generators[employees_number_code][section_label].send(None)
            result[employees_number_code][section_label] = generators[
                employees_number_code
            ][section_label].send(user_evaluations[index])

    return JsonResponse(result)


def activity_chart(request):
    """Aggregate and count completed surveys."""
    count = (
        SurveyUser.objects.filter(status=3)
        .annotate(month=TruncDay("created_at"))
        .values("created_at")
        .annotate(c=Count("id"))
        .order_by("created_at")
    )
    result = []
    for elem in count:
        result.append({"timestamp": str(elem["created_at"]), "count": elem["c"]})
    return JsonResponse(result, safe=False)
