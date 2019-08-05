from django.urls import path

from survey import views


urlpatterns = [
    path('',views.index),
    path('gotoquestion/<int:id>',views.gotoQuestion),
    path('startsurvey',views.startSurvey),
    path('continueselfeval',views.continueSelfEval),
    path('continueselfeval/<key>',views.loadSelfEval),
    path('finishsurvey',views.finishSurvey),
    path('report',views.showReport),
    path('companylist',views.getCompanies),
]
