from django.urls import path
from django.views.generic import TemplateView

from .views import SurveyQuestionAnswerApiView
from .views import SurveyQuestionApiView

urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="survey/swagger-ui.html",
            extra_context={"schema_url": "survey/api/openapi-schema.yml"},
        ),
        name="swagger-ui",
    ),
    path("survey_question", SurveyQuestionApiView.as_view()),
    path("survey_question_answer", SurveyQuestionAnswerApiView.as_view()),
]
