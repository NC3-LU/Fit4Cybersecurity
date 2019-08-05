from django.db import models

from survey.globals import COUNTRIES,SERVICE_TARGETS
# Create your models here.

# from survey.models import SurveyQuestionServiceCategory, SurveyUserAnswers, SurveyUserAnswer, SurveyUser
from survey.models import SurveyQuestionAnswer, SurveyQuestionServiceCategory

class SurveyAnswerRecommendation(models.Model):
    # surveyUserAnswers --> depending on selection
    answer = models.ForeignKey(SurveyQuestionAnswer,on_delete=models.CASCADE)
    recommendation = models.TextField()

class Company(models.Model):
    # company name
    # company contact email
    # company contact phone
    # company contact address
    # company special notes # what is important to know: "We only fix MACs ;)"
    name = models.CharField(max_length=128)
    contact_email = models.EmailField()
    contact_tel = models.TextField(max_length=32)
    contact_address_street = models.CharField(max_length=128)
    contact_address_city = models.CharField(max_length=64)
    contact_address_country = models.CharField(max_length=2,choices=COUNTRIES)
    contact_address_number = models.IntegerField()
    contact_address_postcode = models.CharField(max_length=10)
    notes = models.TextField()

class CompanyService(models.Model):
    # SurveyQuestionServiceCategory connection
    # Company
    # for who are there services
        # SME
        # Corporate
        # private
    category = models.ForeignKey(SurveyQuestionServiceCategory,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    target = models.CharField(max_length=3,choices=SERVICE_TARGETS)