from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from django.http import (
    StreamingHttpResponse,
    HttpResponseRedirect
)
from stats.stats_logic import (
    get_finished_surveys_list
)


@login_required
def index(request):
    result = get_finished_surveys_list(request)
    if result is None:
        return HttpResponseRedirect("/admin/statistics/")

    return render(request, "admin/stats.html", result)
