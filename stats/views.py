# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.conf.global_settings import LANGUAGES
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.utils import translation
from csskp.settings import CUSTOM, LANGUAGE_CODE
from survey.lib.utils import tree, mean_gen
from survey.models import SurveyUser, CONTEXT_SECTION_LABEL
from survey.reporthelper import calculateResult


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
        "first_survey_date": first_survey.created_at,
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
    result = SurveyUser.objects.values("status").annotate(count=Count("status"))
    status = {1: "In progress", 2: "Under reviews", 3: "Finished"}
    return JsonResponse(
        {status[item["status"]]: item["count"] for item in result.all()}
    )


def survey_language_count(request):
    """Returns the count for the SurveyUser chosen_lang property."""
    result = SurveyUser.objects.values("chosen_lang").annotate(
        count=Count("chosen_lang")
    )
    return JsonResponse(
        {
            [lang for lang in LANGUAGES if lang[0] == item["chosen_lang"]][0][1]: item[
                "count"
            ]
            for item in result.all()
        }
    )


def answers_per_section(request):
    """Return a dict with the mean of the user's answers per section, with the
    surveys completed during the last month."""
    chart_exclude_sections = [CONTEXT_SECTION_LABEL]
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
