from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from .views import RecommendationsApiView
from .views import SurveyQuestionAnswerApiView
from .views import SurveyQuestionApiView
from .views import SurveySectionApiView
from .views import SurveyUserAnswerApiView
from .views import SurveyUserApiView
from .views import SurveyUsersApiView


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Fit4Cybersecurity API",
#         default_version="v1",
#         description="Documentation of the Fit4Cybersecurity API.",
#         contact=openapi.Contact(email="opensource@nc3.lu"),
#         license=openapi.License(name="GNU Affero General Public License version 3"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("recommendation/", RecommendationsApiView.as_view()),
    path("survey_section/", SurveySectionApiView.as_view()),
    path("survey_question/", SurveyQuestionApiView.as_view()),
    path("survey_question_answer/", SurveyQuestionAnswerApiView.as_view()),
    path("survey_user/", SurveyUsersApiView.as_view()),
    path("survey_user/<uuid:id>/", SurveyUserApiView.as_view()),
    path("survey_user_answer/<uuid:id>/", SurveyUserAnswerApiView.as_view()),
]
