from django.urls import path

from csskp.settings import CUSTOM
from stats import views


urlpatterns = [
    path("", views.index, name="stats"),
    path("overall.json", views.overall, name="overall"),
]

extrapatterns = []

if CUSTOM["stats"].get("activity", False):
    extrapatterns.append(
        path(
            "activity-chart.json",
            views.activity_chart,
            name="activity_chart",
        )
    )

if CUSTOM["stats"].get("sector", False):
    extrapatterns.append(
        path(
            "survey_per_company_sector.json",
            views.survey_per_company_sector,
            name="survey_per_company_sector",
        )
    )

if CUSTOM["stats"].get("size", False):
    extrapatterns.append(
        path(
            "survey_per_company_size.json",
            views.survey_per_company_size,
            name="survey_per_company_size",
        )
    )

if CUSTOM["stats"].get("country", False):
    extrapatterns.append(
        path(
            "survey_per_country.json",
            views.survey_per_country,
            name="survey_per_country",
        )
    )

if CUSTOM["stats"].get("status", False):
    extrapatterns.append(
        path(
            "survey-status-count.json",
            views.survey_status_count,
            name="survey_status_count",
        )
    )

if CUSTOM["stats"].get("language", False):
    extrapatterns.append(
        path(
            "survey-language-count.json",
            views.survey_language_count,
            name="survey_language_count",
        )
    )

if CUSTOM["stats"].get("section", False):
    extrapatterns.append(
        path(
            "answers-per-section.json",
            views.answers_per_section,
            name="answers_per_section",
        )
    )

if CUSTOM["stats"].get("category", False):
    extrapatterns.append(
        path(
            "answers-per-category.json",
            views.answers_per_category,
            name="answers_per_category",
        )
    )

if CUSTOM["stats"].get("current_question", False):
    extrapatterns.append(
        path(
            "survey_current_question.json",
            views.survey_current_question,
            name="survey_current_question",
        )
    )

urlpatterns.extend(extrapatterns)
