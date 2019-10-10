from django.contrib import admin

from survey.models import SurveyQuestion,SurveyQuestionAnswer,SurveyQuestionServiceCategory,SurveySection,SurveyUser,SurveyUserAnswer,Recommendations,TranslationKey





class SurveyQuestionAdmin(admin.ModelAdmin):
    # add the necessary restrictions for the fieds so we can limit the choice in the language base ;)
    pass









# Register your models here.

admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAnswer)
admin.site.register(SurveyQuestionServiceCategory)
admin.site.register(SurveySection)
admin.site.register(SurveyUser)
admin.site.register(SurveyUserAnswer)
admin.site.register(Recommendations)
admin.site.register(TranslationKey)