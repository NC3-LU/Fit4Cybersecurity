# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="survey/swagger-ui.html",
            extra_context={"schema_url": "survey/api/openapi-schema.yml"},
        ),
        name="swagger-ui",
    ),
]
