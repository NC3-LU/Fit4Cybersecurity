import sys
from datetime import datetime
from typing import Any
from typing import Dict

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.conf.global_settings import LANGUAGES
from django.db.models import Count
from django.db.models import Sum
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext as _
from django_countries import countries

from csskp.settings import CUSTOM
from csskp.settings import LANGUAGE_CODE
from survey.lib.utils import mean_gen
from survey.lib.utils import tree
from survey.models import CONTEXT_SECTION_LABEL
from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer
from survey.models import SurveyUser
from survey.models import SurveyUserAnswer
from survey.reporthelper import calculateResult


def index(request):
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    now = datetime.now()
    if not date_from:
        # 12 months ago
        date_from = (now - relativedelta(months=12)).strftime("%Y-%m-%d")

    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    nb_finished_surveys_for_period = SurveyUser.objects.filter(
        status=3, created_at__gte=date_from
    ).count()
    nb_surveys_for_period = SurveyUser.objects.filter(created_at__gte=date_from).count()
    survey_countries = (
        SurveyUserAnswer.objects.filter(
            user__status=3,
            user__created_at__gte=date_from,
            answer__question__section__label=CONTEXT_SECTION_LABEL,
            answer__question__label__contains="country",
        )
        .values_list("uvalue", flat=True)
        .distinct()
    )
    try:
        first_survey = SurveyUser.objects.filter(status=3).order_by("created_at")[0]
    except Exception:
        first_survey = ""
    nb_surveys = SurveyUser.objects.count()

    time_frames = (
        (
            _("Last week"),
            (now - relativedelta(weeks=1)).strftime("%Y-%m-%d"),
        ),
        (
            _("Last month"),
            (now - relativedelta(months=1)).strftime("%Y-%m-%d"),
        ),
        (
            _("Last quarter"),
            (now - relativedelta(months=4)).strftime("%Y-%m-%d"),
        ),
        (
            _("Last year"),
            (now - relativedelta(months=12)).strftime("%Y-%m-%d"),
        ),
    )

    context = {
        "date_from": date_from,
        "time_frames": time_frames,
        "nb_surveys": nb_surveys,
        "first_survey_date": getattr(first_survey, "created_at", False),
        "nb_finished_surveys": nb_finished_surveys,
        "nb_surveys_for_period": nb_surveys_for_period,
        "nb_finished_surveys_for_period": nb_finished_surveys_for_period,
        "survey_countries": survey_countries,
        "python_version": "{}.{}.{}".format(*sys.version_info[:3]),
        "others_translation": str(_("Others")),
        "range": range(5),
        "stats_options": CUSTOM.get("stats"),
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

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    result = (
        SurveyUser.objects.filter(
            created_at__gte=date_from,
        )
        .values("status")
        .annotate(count=Count("status"))
        .order_by("count")
        .reverse()
    )
    status = {1: _("In progress"), 2: _("Under review"), 3: _("Finished")}
    return JsonResponse(
        {status[item["status"]]: item["count"] for item in result.all()}
    )


def survey_language_count(request):
    """Returns the count for the SurveyUser chosen_lang property."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    result = (
        SurveyUser.objects.filter(
            created_at__gte=date_from,
        )
        .values("chosen_lang")
        .annotate(count=Count("chosen_lang"))
        .order_by("count")
        .reverse()
    )
    return JsonResponse(
        {
            str(
                _([lang for lang in LANGUAGES if lang[0] == item["chosen_lang"]][0][1])
            ): item["count"]
            for item in result.all()
        }
    )


def survey_per_country(request):
    """Return the count the surveys per country"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    nb_finished_surveys = SurveyUser.objects.filter(
        status=3, created_at__gte=date_from
    ).count()
    threshold = 0.01

    result: Dict[str, Any] = dict()
    query_gt = (
        SurveyUserAnswer.objects.alias(entries=Count("answer"))
        .filter(
            user__status=3,
            user__created_at__gte=date_from,
            answer__question__section__label=CONTEXT_SECTION_LABEL,
            answer__question__label__contains="country",
            entries__gt=nb_finished_surveys * threshold,
        )
        .values("uvalue")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )

    query_lte = (
        SurveyUserAnswer.objects.alias(entries=Count("answer"))
        .filter(
            user__status=3,
            user__created_at__gte=date_from,
            answer__question__section__label=CONTEXT_SECTION_LABEL,
            answer__question__label__contains="country",
            entries__lte=nb_finished_surveys * threshold,
        )
        .values("uvalue")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )

    for q in query_gt:
        try:
            country = _(dict(countries).get(q["uvalue"]))
        except AttributeError:
            country = SurveyQuestionAnswer.objects.get(value=q["uvalue"]).label

        result[country] = q["count"]

    if query_lte:
        result[_("Others")] = {}
        for q in query_lte:
            try:
                country = _(dict(countries).get(q["uvalue"]))
            except AttributeError:
                country = SurveyQuestionAnswer.objects.get(value=q["uvalue"]).label

            result[_("Others")][country] = q["count"]

    return JsonResponse(result)


def survey_per_company_size(request):
    """Return the count the surveys per company size"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    result: Dict[str, int] = dict()
    query = (
        SurveyUserAnswer.objects.filter(
            user__status=3,
            user__created_at__gte=date_from,
            answer__question__section__label=CONTEXT_SECTION_LABEL,
            answer__question__label__contains="employees",
        )
        .values("answer__label")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )
    result = {_(q["answer__label"]): q["count"] for q in query}

    return JsonResponse(result)


def survey_per_company_sector(request):
    """Return the count the surveys per company sector"""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    result: Dict[str, int] = dict()
    query = (
        SurveyUserAnswer.objects.filter(
            user__status=3,
            user__created_at__gte=date_from,
            answer__question__section__label=CONTEXT_SECTION_LABEL,
            answer__question__label__contains="sector",
        )
        .values("answer__label")
        .annotate(count=Count("answer"))
        .order_by("count")
        .reverse()
    )
    result = {_(q["answer__label"]): q["count"] for q in query}

    return JsonResponse(result)


def answers_per_section(request):
    """Return a dict with the mean of the user's answers per section, with the
    surveys completed during the last month."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    chart_exclude_sections = [CONTEXT_SECTION_LABEL]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 month ago
        date_from = datetime.now() - relativedelta(months=12)
        # date_to = datetime.now()

    users = SurveyUser.objects.filter(status=3, created_at__gte=date_from)

    result = tree()
    generators = tree()

    questions = (
        SurveyQuestion.objects.exclude(section__label__in=chart_exclude_sections)
        .values_list("section_id")
        .order_by("section_id")
        .annotate(total=Sum("maxPoints"))
    )
    sections = list(questions.values_list("section__label", flat=True).distinct())
    max_evaluations_per_section = {q[0]: q[1] for q in questions}

    for user in users:
        user_evaluations = user.get_evaluations_by_section(max_evaluations_per_section)
        employees_number_code = user.get_employees_number_label()

        for index, section in enumerate(sections):
            section_label = str(_(section))
            if section_label not in generators.get(employees_number_code, {}):
                generators[employees_number_code][section_label] = mean_gen()
                generators[employees_number_code][section_label].send(None)
            result["all"][employees_number_code][section_label] = generators[
                employees_number_code
            ][section_label].send(user_evaluations[index])
            result[user.get_country_code()][employees_number_code][
                section_label
            ] = generators[employees_number_code][section_label].send(
                user_evaluations[index]
            )

    return JsonResponse(result)


def answers_per_category(request):
    """Return a dict with the mean of the user's answers per category, with the
    surveys completed during the last year."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)
    chart_exclude_sections = ["__context"]
    if "chart_exclude_sections" in CUSTOM.keys():
        chart_exclude_sections = (
            chart_exclude_sections + CUSTOM["chart_exclude_sections"]
        )

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 month ago
        date_from = datetime.now() - relativedelta(months=12)
        # date_to = datetime.now()

    users = SurveyUser.objects.filter(status=3, created_at__gte=date_from)

    result = tree()
    generators = tree()

    questions = (
        SurveyQuestion.objects.exclude(section__label__in=chart_exclude_sections)
        .values_list("service_category_id")
        .order_by("service_category_id")
        .annotate(total=Sum("maxPoints"))
    )
    categories = list(
        questions.values_list("service_category__label", flat=True).distinct()
    )
    max_evaluations_per_category = {q[0]: q[1] for q in questions}

    for user in users:
        user_evaluations = user.get_evaluations_by_category(
            max_evaluations_per_category
        )
        employees_number_code = user.get_employees_number_label()
        for index, category in enumerate(categories):
            category_label = str(_(category))
            if category_label not in generators.get(employees_number_code, {}):
                generators[employees_number_code][category_label] = mean_gen()
                generators[employees_number_code][category_label].send(None)
            result["all"][employees_number_code][category_label] = generators[
                employees_number_code
            ][category_label].send(user_evaluations[index])
            result[user.get_country_code()][employees_number_code][
                category_label
            ] = generators[employees_number_code][category_label].send(
                user_evaluations[index]
            )

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


def survey_current_question(request):
    """Returns the count for the SurveyUser current_question_id property."""
    lang = request.session.get(settings.LANGUAGE_COOKIE_NAME, LANGUAGE_CODE)
    translation.activate(lang)

    date_from = request.GET.get("from", None)
    # date_to = request.GET.get('to', None)
    if not date_from:
        # 12 months ago
        date_from = datetime.now() - relativedelta(months=12)

    query = (
        SurveyUser.objects.filter(
            created_at__gte=date_from,
        )
        .values("current_question_id__qindex", "current_question_id__label")
        .annotate(count=Count("current_question_id__label"))
        .order_by("count")
        .reverse()
    )
    result = {
        str(q["current_question_id__qindex"])
        + ". "
        + _(q["current_question_id__label"])[:45]
        + "...": q["count"]
        for q in query
    }

    return JsonResponse(result)
