# -*- coding: utf-8 -*-

from django.urls import path
from .views import (
    TranslationListApiView,
    TranslationDetailApiView,
)

urlpatterns = [
    path("", TranslationListApiView.as_view()),
    path("<int:translation_id>/", TranslationDetailApiView.as_view()),
]
