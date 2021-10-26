# -*- coding: utf-8 -*-

from django.urls import path

from survey import views

urlpatterns = [
    path("", views.index),
    path("start", views.start),
    path("start/<slug:lang>", views.start),
    path("question/<int:question_index>", views.handle_question_form),
    path("language/<slug:lang>", views.change_lang),
    path("resume/", views.resume),
    path("review", views.review),
    path("finish", views.finish),
    path("report", views.finish),
    path("report/<slug:lang>", views.show_report),
    path("feedback", views.save_general_feedback),
    path("companies", views.get_companies),
]
