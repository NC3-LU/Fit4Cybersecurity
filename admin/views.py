# -*- coding: utf-8 -*-

import sys
import subprocess
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from survey.lib.utils import export_survey


@login_required
def export_survey_json(request):
    result = export_survey()
    return JsonResponse(result, safe=False)


@login_required
def compile_translations(request):
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "compilemessages",
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return HttpResponseRedirect("/admin/")
