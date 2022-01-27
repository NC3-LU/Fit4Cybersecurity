# -*- coding: utf-8 -*-

from django.urls import path, include

from survey import views

urlpatterns = [
    path("", views.index),
    path("start", views.start),
    path("question/<int:question_index>", views.handle_question_form),
    path("language/<slug:lang>", views.change_lang),
    path("resume/", views.resume),
    path("review", views.review),
    path("finish", views.finish),
    path("report", views.show_report),
    path("feedback", views.save_general_feedback),
    path("companies", views.get_companies),
    path("api/", include("survey.api.urls")),
]
