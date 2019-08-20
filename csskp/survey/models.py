from django.db import models

# import global constants
from survey.globals import SECTOR_CHOICES,QUESTION_TYPES
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


class SurveyQuestionServiceCategory(models.Model):
    # QuestionCatID

    title = models.CharField(max_length=128)

    def __str__(self):
        return str(self.title)



class SurveySection(models.Model):
    # Section ID
    # Section title

    sectionTitle = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.sectionTitle)



class SurveyQuestion(models.Model):
    # Question id --> translation in other table
    # QuestionCatID
    # Section ID

    service_category = models.ForeignKey(SurveyQuestionServiceCategory, on_delete=models.CASCADE)
    section = models.ForeignKey(SurveySection,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    qtype = models.CharField(max_length=1,choices=QUESTION_TYPES,default=QUESTION_TYPES[0][0])
    qindex = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.title)



class SurveyQuestionAnswer(models.Model):
    # Answer id --> translation in other table
    # Question id --> can be 1-question to multi-answers

    question = models.ForeignKey(SurveyQuestion,on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
    aindex = models.IntegerField()

    def __str__(self):
        return str(self.answer)

    class Meta:
        unique_together = ('aindex','question')



class SurveyUser(models.Model):
    # user ID - Hash or UUID
    # Sector
    # OtherSector Description
    # number of employees

    user_id = models.UUIDField(default=uuid.uuid4)
    sector = models.CharField(max_length=4, choices=SECTOR_CHOICES, default=SECTOR_CHOICES[0][0])

    current_question = models.IntegerField(default=0)
    survey_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)



class SurveyUserAnswers(models.Model):
    # UUID user
    # QuestionID
    # AnswerListID

    user = models.ForeignKey(SurveyUser,on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)



class SurveyUserAnswer(models.Model):
    # AnswerID
    # AnswerListID
    user = models.ForeignKey(SurveyUser,on_delete=models.CASCADE)
    answer = models.ForeignKey(SurveyQuestionAnswer,on_delete=models.CASCADE)
    # 0, 1 for true, false selections, or -inf to +inf for value slider questions
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.answer)

