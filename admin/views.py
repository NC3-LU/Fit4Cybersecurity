# -*- coding: utf-8 -*-

import sys
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.utils import exec_cmd, exec_cmd_no_wait
from stats.stats_logic import get_finished_surveys_list
from survey.reporthelper import calculateResult
from survey.lib.utils import export_survey
from survey.models import SurveyUser
from stats.forms import DatesLimitForm


@login_required
def export_survey_json(request):
    """Returns the survey (questions, answers, recommendations and sections) in JSON."""
    result = export_survey()
    return JsonResponse(result, safe=False)


@login_required
def site_stats(request):
    """Returns the page which will display some statistics."""
    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    nb_surveys = SurveyUser.objects.count()
    last_surveys = SurveyUser.objects.filter(status=3).order_by("-created_at")[:10]
    survey_results = {user.id: calculateResult(user)[0] for user in last_surveys}
    context = {
        "nb_surveys": nb_surveys,
        "nb_finished_surveys": nb_finished_surveys,
        "last_surveys": last_surveys,
        "survey_results": survey_results,
    }
    return render(request, "admin/site_stats.html", context=context)


@login_required
def results_stats(request):
    if request.method == "POST":
        dates_limit_form = DatesLimitForm(data=request.POST)
        if not dates_limit_form.is_valid():
            return None
        start_date = dates_limit_form.cleaned_data["start_date"]
        end_date = dates_limit_form.cleaned_data["end_date"]
    else:
        dates_limit_form = DatesLimitForm()
        start_date = dates_limit_form.fields["start_date"].initial
        end_date = dates_limit_form.fields["end_date"].initial

    result = get_finished_surveys_list(start_date, end_date)
    context = {
        "dates_limit_form": dates_limit_form,
        "surveys_users_results": json.dumps(result, indent=2, sort_keys=True),
    }

    return render(request, "admin/results_stats.html", context=context)


@login_required
def compile_translations(request):
    """Triggers the compilation of the translation files in a subprocess."""
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "compilemessages",
    ]
    result = exec_cmd(" ".join(cmd))
    print(result)  # TODO: log the result
    messages.info(request, "Translations files compiled.")
    return HttpResponseRedirect("/admin/")


@login_required
def migrate_database(request):
    """Triggers the execution of the database migration scripts."""
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "migrate",
    ]
    result = exec_cmd(" ".join(cmd))
    print(result)  # TODO: log the result
    messages.info(request, "Database up-to-date.")
    return HttpResponseRedirect("/admin/")


@login_required
def update_software(request):
    """Triggers the execution of the script which will update the software."""
    cmd = ["./contrib/update.sh"]
    exec_cmd_no_wait(cmd)
    messages.info(request, "Updated.")
    return HttpResponseRedirect("/admin/")
