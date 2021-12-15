# -*- coding: utf-8 -*-

from django.urls import path
from stats import views

app_name = "stats"

urlpatterns = [
    path("", views.index, name="index"),
]
