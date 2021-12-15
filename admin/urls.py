# -*- coding: utf-8 -*-

from django.urls import path

from admin import views

urlpatterns = [
    path("export/survey.json", views.export_survey_json),
    path("compile-translations", views.compile_translations, name="compile_translations"),
]
