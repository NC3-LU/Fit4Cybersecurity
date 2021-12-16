# -*- coding: utf-8 -*-

from django.urls import path

from admin import views

urlpatterns = [
    path("export/survey.json", views.export_survey_json),
    path("site_stats", views.site_stats),
    path(
        "compile-translations", views.compile_translations, name="compile_translations"
    ),
    path("migrate-database", views.migrate_database, name="migrate_database"),
    path("update-software", views.update_software, name="update_software"),
    path(
        "stats/survey-status-count.json",
        views.survey_status_count,
        name="survey_status_count",
    ),
    path(
        "stats/survey-language-count.json",
        views.survey_language_count,
        name="survey_language_count",
    ),
]
