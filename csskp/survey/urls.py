from django.urls import path

from survey import views


urlpatterns = [
    path('',views.index),
    path('gotoquestion/<int:id>',views.gotoQuestion),
    path('startsurvey/',views.index),
    path('startsurvey/<slug:lang>',views.startSurvey),
    path('continueselfeval/<uuid:userId>',views.loadSelfEval),
    path('finishsurvey',views.finishSurvey),
    path('report',views.showReport),
    path('companylist',views.getCompanies),
]
