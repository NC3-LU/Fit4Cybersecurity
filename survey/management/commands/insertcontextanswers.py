# -*- coding: utf-8 -*-

"""insertcontextanswers.py - Generate JSON files with the output of the command:

$ python manage.py dumpdata --indent 2 survey.surveyuser > contrib/out.json
$ python manage.py insertcontextanswers
"""

import json
from django.core.management.base import BaseCommand
from survey.models import SurveyUser, SurveyQuestion, SurveyUserAnswer, SurveyQuestionAnswer


class Command(BaseCommand):
    help = """Creates context questions answers based on the old data structure."""

    def handle(self, *args, **options):
        # Added the site-name as param:
        site_name = 'fit4privacy'
        with open("./contrib/" + site_name + "_users_data.json") as f:
            data = json.loads(f.read())

        question_employees = SurveyQuestion.objects.get(
            label="How many employees?", section__label="__context"
        )
        question_country = SurveyQuestion.objects.get(
            label__contains="your country", section__label="__context"
        )
        question_sector = SurveyQuestion.objects.get(
            label="What is your sector?", section__label="__context"
        )

        for user in data:
            user = SurveyUser.objects.get(user_id=user["user_id"])
            employees_answer = SurveyQuestionAnswer.objects.get(
                question=question_employees, value=user["e_count"]
            )
            country_answer = SurveyQuestionAnswer.objects.get(
                question=question_country, aindex=1
            )
            sector_answer = SurveyQuestionAnswer.objects.get(
                question=question_sector, value=user["sector"]
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=employees_answer,
                uvalue=user["e_count"],
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=country_answer,
                uvalue=user["country_code"],
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=sector_answer,
                uvalue=user["sector"],
            )
