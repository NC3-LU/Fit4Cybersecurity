from django.urls import path

from audit import views

urlpatterns = [
    path("", views.index, name="audit"),
]
