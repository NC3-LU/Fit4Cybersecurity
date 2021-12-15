# -*- coding: utf-8 -*-

import sys
import subprocess
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from survey.lib.utils import export_survey
from survey.models import SurveyUser


@login_required
def export_survey_json(request):
    result = export_survey()
    return JsonResponse(result, safe=False)


@login_required
def site_stats(request):
    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    nb_surveys = SurveyUser.objects.count()
    context = {
        "nb_surveys": nb_surveys,
        "nb_finished_surveys": nb_finished_surveys
    }
    return render(
        request, "admin/site_stats.html", context=context
    )


@login_required
def compile_translations(request):
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "compilemessages",
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE)
    messages.info(request, 'Compiled translations files migrated.')
    return HttpResponseRedirect("/admin/")


@login_required
def migrate_database(request):
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "migrate",
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE)
    messages.info(request, 'Database up-to-date.')
    return HttpResponseRedirect("/admin/")
