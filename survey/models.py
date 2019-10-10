from django.db import models

# import global constants
from survey.globals import SECTOR_CHOICES,QUESTION_TYPES,COMPANY_SIZE, LANG_SELECT, TRANSLATION_TYPES,COUNTRIES,SERVICE_TARGETS
import uuid

# Create your models here.

# REMEMBER: use models.UUIDField for every object

'''
There are 3 types of questions:
 1. Multiple choice
 2. Single Choice
 3. Slider - integer (minimum int to max int - single steps)

Each question belongs to a section
Each question has a Service Category - helps with assigning companies later
Each question has multiple answers assigned to it
 - for multiple choices for examples
Each question has a type (see above)
Each question has only a question ID - multilanguage
'''

LOCAL_DEFAULT_LANG = LANG_SELECT[1][0]


class TranslationKey(models.Model):
    key = models.CharField(max_length=32)
    text = models.TextField()
    lang = models.CharField(max_length=2,choices=LANG_SELECT,default=LANG_SELECT[0][0])
    ttype = models.CharField(max_length=1,choices=TRANSLATION_TYPES,default=TRANSLATION_TYPES[0][0])

    class Meta:
        unique_together = ('lang','id')
    
    def __str__(self):
        return str(self.text)



class SurveyQuestionServiceCategory(models.Model):
    # QuestionCatID

    titleKey = models.CharField(max_length=32)

    def __str__(self):
        return str(TranslationKey.objects.filter(lang=LOCAL_DEFAULT_LANG).filter(key=self.titleKey)[0])



class SurveySection(models.Model):
    # Section ID
    # Section title

    sectionTitleKey = models.CharField(max_length=32)
    
    def __str__(self):
        return str(TranslationKey.objects.filter(lang=LOCAL_DEFAULT_LANG).filter(key=self.sectionTitleKey)[0])



class SurveyQuestion(models.Model):
    # Question id --> translation in other table
    # QuestionCatID
    # Section ID

    service_category = models.ForeignKey(SurveyQuestionServiceCategory, on_delete=models.CASCADE)
    section = models.ForeignKey(SurveySection,on_delete=models.CASCADE)
    titleKey = models.CharField(max_length=32)
    qtype = models.CharField(max_length=1,choices=QUESTION_TYPES,default=QUESTION_TYPES[0][0])
    qindex = models.IntegerField(unique=True)
    maxPoints = models.IntegerField(default=10)

    def __str__(self):
        return str(TranslationKey.objects.filter(lang=LOCAL_DEFAULT_LANG).filter(key=self.titleKey)[0])



class SurveyQuestionAnswer(models.Model):
    # Answer id --> translation in other table
    # Question id --> can be 1-question to multi-answers

    question = models.ForeignKey(SurveyQuestion,on_delete=models.CASCADE)
    answerKey = models.CharField(max_length=32)
    aindex = models.IntegerField()
    uniqueAnswer = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(TranslationKey.objects.filter(lang=LOCAL_DEFAULT_LANG).filter(key=self.answerKey)[0])

    class Meta:
        unique_together = ('aindex','question')



class SurveyUser(models.Model):
    # user ID - Hash or UUID
    # Sector
    # OtherSector Description
    # number of employees

    user_id = models.UUIDField(default=uuid.uuid4)
    sector = models.CharField(max_length=4, choices=SECTOR_CHOICES, default=SECTOR_CHOICES[0][0])
    e_count = models.CharField(max_length=2, choices=COMPANY_SIZE, default=COMPANY_SIZE[0][0])

    chosenLang = models.CharField(max_length=2, choices=LANG_SELECT, default=LANG_SELECT[0][0])

    current_question = models.IntegerField(default=0)
    survey_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)


'''
class SurveyUserAnswers(models.Model):
    # UUID user
    # QuestionID
    # AnswerListID

    user = models.ForeignKey(SurveyUser,on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

'''

class SurveyUserAnswer(models.Model):
    # AnswerID
    # AnswerListID
    user = models.ForeignKey(SurveyUser,on_delete=models.CASCADE)
    answer = models.ForeignKey(SurveyQuestionAnswer,on_delete=models.CASCADE)
    # 0, 1 for true, false selections, or -inf to +inf for value slider questions
    uvalue = models.IntegerField(default=0)

    def __str__(self):
        return str(self.answer)



class Recommendations(models.Model):
    textKey = models.CharField(max_length=32)
    min_e_count = models.CharField(max_length=2, choices=COMPANY_SIZE, default=COMPANY_SIZE[0][0])
    max_e_count = models.CharField(max_length=2, choices=COMPANY_SIZE, default=COMPANY_SIZE[-1][0])
    sector = models.CharField(max_length=4, choices=SECTOR_CHOICES, null=True, blank=True, default=None)
    forAnswer = models.ForeignKey(SurveyQuestionAnswer,on_delete=models.CASCADE)
    answerChosen = models.BooleanField(default=False)

    def __str__(self):
        return str(TranslationKey.objects.filter(lang=LOCAL_DEFAULT_LANG).filter(key=self.textKey)[0])


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