# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from survey.lib.utils import export_survey


@login_required
def export_survey_json(request):
    result = export_survey()
    return JsonResponse(result, safe=False)
