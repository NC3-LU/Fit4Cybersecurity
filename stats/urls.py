# -*- coding: utf-8 -*-

from django.urls import path
from stats import views

app_name = "stats"

urlpatterns = [
    path("", views.index, name="index"),
    path("overall.json", views.overall, name="overall"),
    path("survey_language_count.json", views.survey_language_count, name="survey_language_count"),
]
