from django.contrib import admin

from survey.models import SurveyQuestion,SurveyQuestionAnswer,SurveyQuestionServiceCategory,SurveySection,SurveyUser,SurveyUserAnswer,SurveyUserAnswers

# Register your models here.

admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAnswer)
admin.site.register(SurveyQuestionServiceCategory)
admin.site.register(SurveySection)
admin.site.register(SurveyUser)
admin.site.register(SurveyUserAnswer)
admin.site.register(SurveyUserAnswers)