# -*- coding: utf-8 -*-

from django.urls import path

from admin import views

urlpatterns = [
    path("translations/questions", views.translations_questions),
]
