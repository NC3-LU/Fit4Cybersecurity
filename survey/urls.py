from django.urls import path

from survey import views

urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('start/<slug:lang>', views.start),
    path('question/<int:question_index>', views.handle_question_form),
    path('resume/', views.resume),
    path('preview', views.preview),
    path('finish', views.finish),
    path('report', views.finish),
    path('report/<slug:lang>', views.show_report),
    path('companies', views.get_companies),
]
