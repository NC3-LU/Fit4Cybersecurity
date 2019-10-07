from django.urls import path

from survey import views

urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('start/<slug:lang>', views.start),
    path('question', views.getQuestion),
    path('resume/<str:userId>', views.resume),
    path('finish', views.finish),
    path('report', views.finish),
    path('report/<slug:lang>', views.showReport),
    path('chart', views.show_chart),
    path('companies', views.getCompanies),
]
