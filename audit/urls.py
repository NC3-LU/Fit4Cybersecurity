from django.urls import path

from audit import views

urlpatterns = [
    path("", views.index, name="audit"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("product/<int:audit_id>", views.audit),
    path("edit/<int:audit_id>", views.edit, name="edit"),
]
