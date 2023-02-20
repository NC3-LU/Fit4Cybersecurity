from django.urls import path
from django.views.generic import TemplateView

from .views import SurveyQuestionAnswerApiView
from .views import SurveyQuestionApiView
from .views import SurveySectionApiView
from .views import SurveyUserAnswerApiView
from .views import SurveyUserApiView
from .views import SurveyUsersApiView


urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="survey/swagger-ui.html",
            extra_context={"schema_url": "survey/api/openapi-schema.yml"},
        ),
        name="swagger-ui",
    ),
    path("survey_section/", SurveySectionApiView.as_view()),
    path("survey_question/", SurveyQuestionApiView.as_view()),
    path("survey_question_answer/", SurveyQuestionAnswerApiView.as_view()),
    path("survey_user/", SurveyUsersApiView.as_view()),
    path("survey_user/<uuid:id>/", SurveyUserApiView.as_view()),
    path("survey_user_answer/<uuid:id>/", SurveyUserAnswerApiView.as_view()),
]
