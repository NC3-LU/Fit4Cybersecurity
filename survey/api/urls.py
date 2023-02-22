from django.urls import path
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import RecommendationsApiView
from .views import SurveyQuestionAnswerApiView
from .views import SurveyQuestionApiView
from .views import SurveySectionApiView
from .views import SurveyUserAnswerApiView
from .views import SurveyUserApiView
from .views import SurveyUsersApiView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("recommendation/", RecommendationsApiView.as_view()),
    path("survey_section/", SurveySectionApiView.as_view()),
    path("survey_question/", SurveyQuestionApiView.as_view()),
    path("survey_question_answer/", SurveyQuestionAnswerApiView.as_view()),
    path("survey_user/", SurveyUsersApiView.as_view()),
    path("survey_user/<uuid:id>/", SurveyUserApiView.as_view()),
    path("survey_user_answer/<uuid:id>/", SurveyUserAnswerApiView.as_view()),
]
