from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from .views import AuditQuestionApiView
from .views import CompanyApiView


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="audit"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="audit"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="audit"), name="redoc-audit"),
    path("company/", CompanyApiView.as_view()),
    path("audit_question/", AuditQuestionApiView.as_view()),
]
