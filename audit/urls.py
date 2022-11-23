from django.urls import path

from survey import views

urlpatterns = [
    # Root
    path("", views.index, name="index"),
]
