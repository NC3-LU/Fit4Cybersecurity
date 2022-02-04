# -*- coding: utf-8 -*-

from django.urls import path

from stats import views


urlpatterns = [
    path("", views.index, name="stats"),
    path("overall.json", views.overall, name="overall"),
    path(
        "survey-status-count.json",
        views.survey_status_count,
        name="survey_status_count",
    ),
    path(
        "survey-language-count.json",
        views.survey_language_count,
        name="survey_language_count",
    ),
    path(
        "answers-per-section.json",
        views.answers_per_section,
        name="answers_per_section",
    ),
    path(
        "survey_per_country.json",
        views.survey_per_country,
        name="survey_per_country",
    ),
    path(
        "survey_per_company_size.json",
        views.survey_per_company_size,
        name="survey_per_company_size",
    ),
    path(
        "survey_per_company_sector.json",
        views.survey_per_company_sector,
        name="survey_per_company_sector",
    ),
    path(
        "activity-chart.json",
        views.activity_chart,
        name="activity_chart",
    ),
]
