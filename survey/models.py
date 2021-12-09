# -*- coding: utf-8 -*-

from typing import Optional
import uuid
from django.db import models
from csskp.settings import LANGUAGES, LANGUAGE_CODE

# import global constants
from survey.globals import (
    SECTOR_CHOICES,
    QUESTION_TYPES,
    ANSWER_TYPES,
    COMPANY_SIZE,
    SERVICE_TARGETS,
)

# Create your models here.

# REMEMBER: use models.UUIDField for every object

"""
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
"""

LOCAL_DEFAULT_LANG = LANGUAGE_CODE
SURVEY_STATUS_IN_PROGRESS = 1
SURVEY_STATUS_UNDER_REVIEW = 2
SURVEY_STATUS_FINISHED = 3


class RightMixin:
    @staticmethod
    def _fields_base_write():
        return set()

    @staticmethod
    def _fields_base_read():
        return set(["id"])

    @classmethod
    def fields_base_write(cls):
        return cls._fields_base_write()

    @classmethod
    def fields_base_read(cls):
        return cls._fields_base_write().union(cls._fields_base_read())

    def dump(self):
        dict = {k: getattr(self, k) for k in self.fields_base_read()}
        return dict


class SurveyQuestionServiceCategory(models.Model):
    # QuestionCatID

    label = models.TextField()

    def __str__(self):
        return self.label


class SurveySection(models.Model):
    # Section ID
    # Section title

    label = models.TextField()

    @staticmethod
    def _fields_base_read():
        return {"id", "label"}

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label


class SurveyQuestion(models.Model, RightMixin):
    # Question id --> translation in other table
    # QuestionCatID
    # Section ID

    service_category = models.ForeignKey(
        SurveyQuestionServiceCategory, on_delete=models.CASCADE
    )
    section = models.ForeignKey(SurveySection, on_delete=models.CASCADE)
    label = models.TextField()
    tooltip = models.TextField(null=False, blank=True, default="")
    qtype = models.CharField(
        max_length=2, choices=QUESTION_TYPES, default=QUESTION_TYPES[0][0]
    )
    qindex = models.IntegerField(unique=True)
    maxPoints = models.IntegerField(default=10)

    @staticmethod
    def _fields_base_read():
        return {
            "id",
            "label",
            "section",
            "maxPoints",
        }

    def __str__(self):
        return self.label


class SurveyQuestionAnswer(models.Model):
    # Answer id --> translation in other table
    # Question id --> can be 1-question to multi-answers

    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    label = models.TextField()
    tooltip = models.TextField(null=False, blank=True, default="")
    aindex = models.IntegerField()
    uniqueAnswer = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)
    atype = models.CharField(
        max_length=2, choices=ANSWER_TYPES, default=ANSWER_TYPES[0][0]
    )
    dependant_answers = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.label

    class Meta:
        unique_together = ("aindex", "question")


class SurveyUser(models.Model):
    # user ID - Hash or UUID
    # Sector
    # OtherSector Description
    # number of employees

    user_id = models.UUIDField(default=uuid.uuid4)
    choosen_lang = models.CharField(
        max_length=2, choices=LANGUAGES, default=LOCAL_DEFAULT_LANG
    )
    current_qindex = models.IntegerField(default=0)
    status = models.SmallIntegerField(default=SURVEY_STATUS_IN_PROGRESS)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.user_id)

    def is_survey_in_progress(self):
        return self.status == SURVEY_STATUS_IN_PROGRESS

    def is_survey_under_review(self):
        return self.status == SURVEY_STATUS_UNDER_REVIEW

    def is_survey_finished(self):
        return self.status == SURVEY_STATUS_FINISHED

    def get_context(self, question: Optional[str] = ""):
        result = {}
        user_answers = SurveyUserAnswer.objects.filter(user=self).filter(
            answer__question__section__label="__context", uvalue__gte=0
        )
        if question:
            user_answers = user_answers.filter(answer__question__label=question)
        user_answers = user_answers.order_by(
            "answer__question__qindex", "answer__aindex"
        )
        for user_answer in user_answers:
            result[user_answer.answer.question.label] = user_answer
        return result


class SurveyUserAnswer(models.Model):
    # AnswerID
    # AnswerListID
    user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(SurveyQuestionAnswer, on_delete=models.CASCADE)
    # 0, 1 for true, false selections
    uvalue = models.IntegerField(default=0)
    content = models.TextField(null=False, blank=True, default="")

    def __str__(self):
        return str(self.answer)


class SurveyUserFeedback(models.Model):
    user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, null=True)
    feedback = models.TextField(null=False, blank=True, default="")

    def __str__(self):
        return str(self.feedback)


class Recommendations(models.Model):
    label = models.TextField()
    min_e_count = models.CharField(
        max_length=2, choices=COMPANY_SIZE, default=COMPANY_SIZE[0][0]
    )
    max_e_count = models.CharField(
        max_length=2, choices=COMPANY_SIZE, default=COMPANY_SIZE[-1][0]
    )
    sector = models.CharField(
        max_length=4, choices=SECTOR_CHOICES, null=True, blank=True, default=None
    )
    forAnswer = models.ForeignKey(SurveyQuestionAnswer, on_delete=models.CASCADE)
    answerChosen = models.BooleanField(default=False)

    def __str__(self):
        return self.label


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
    contact_address_country = models.CharField(max_length=4)
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
    category = models.ForeignKey(
        SurveyQuestionServiceCategory, on_delete=models.CASCADE
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    target = models.CharField(max_length=3, choices=SERVICE_TARGETS)
