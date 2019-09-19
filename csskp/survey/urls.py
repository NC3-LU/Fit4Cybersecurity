from django.urls import path

from survey import views


urlpatterns = [
    path('',views.index),
    path('gotoquestion/<int:id>',views.gotoQuestion),
    path('startsurvey/',views.index),
    path('startsurvey/<slug:lang>',views.startSurvey),
    path('continueselfeval/<uuid:userId>',views.loadSelfEval),
    path('finishsurvey',views.finishSurvey),
    #path('finishsurvey',views.showReport),
    path('report/<slug:lang>',views.showReport),
    path('report/',views.finishSurvey),
    path('companylist',views.getCompanies),
]
