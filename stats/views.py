# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.conf.global_settings import LANGUAGES
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from stats.stats_logic import get_finished_surveys_list
from survey.models import SurveyUser
from survey.reporthelper import calculateResult


@login_required
def index(request):
    result = get_finished_surveys_list(request)
    if result is None:
        return HttpResponseRedirect("/admin/export/statistics/")

    return render(request, "admin/stats.html", result)


def overall(request):
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
