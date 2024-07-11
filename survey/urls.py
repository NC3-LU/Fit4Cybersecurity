from django.urls import include
from django.urls import path

from csskp.settings import DEBUG
from survey import views

urlpatterns = [
    path("", views.index),
    # path("start", views.start),
    # path("question/<int:question_index>", views.handle_question_form),
    path("language/<slug:lang>", views.change_lang),
    path("resume/", views.resume),
    path("review", views.review),
    path("finish", views.finish),
    path("report", views.show_report),
    path("feedback", views.save_general_feedback),
    path("companies", views.get_companies),
    path("api/v1/", include("survey.api.urls")),
]
if DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
