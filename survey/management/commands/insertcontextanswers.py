# -*- coding: utf-8 -*-

"""insertcontextanswers.py - Parses JSON file with the old user data content:
[
    {
        "user_id": "99fd7b40-86d1-402d-bf3e-542e2fd16d88",
        "sector": "SALE",
        "e_count": "c",
        "country_code": "DE"
    }
]
"""

import json
from django.core.management.base import BaseCommand
from survey.models import (
    SurveyUser,
    SurveyQuestion,
    SurveyUserAnswer,
    SurveyQuestionAnswer,
    CONTEXT_SECTION_LABEL,
)


class Command(BaseCommand):
    help = """Creates context questions answers based on the old data structure."""

    def add_arguments(self, parser):
        parser.add_argument("--site_name", type=str)

    def handle(self, *args, **options):
        site_name = options["site_name"]
        with open("./contrib/" + site_name + "_users_data.json") as f:
            data = json.loads(f.read())

        question_employees = SurveyQuestion.objects.get(
            label="How many employees?", section__label=CONTEXT_SECTION_LABEL
        )
        question_country = SurveyQuestion.objects.get(
            label__contains="your country", section__label=CONTEXT_SECTION_LABEL
        )
        question_sector = SurveyQuestion.objects.get(
            label="What is your sector?", section__label=CONTEXT_SECTION_LABEL
        )

        nb_created_answers = 0
        for user_data in data:
            try:
                user = SurveyUser.objects.get(user_id=user_data["user_id"])
            except SurveyUser.DoesNotExist:
                continue

            employees_answer = SurveyQuestionAnswer.objects.get(
                question=question_employees, value=user_data["e_count"]
            )
            country_answer = SurveyQuestionAnswer.objects.get(
                question=question_country, aindex=1
            )
            sector_answer = SurveyQuestionAnswer.objects.get(
                question=question_sector, value=user_data["sector"]
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=employees_answer,
                uvalue=user_data["e_count"],
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=country_answer,
                uvalue=user_data["country_code"],
            )

            SurveyUserAnswer.objects.create(
                user=user,
                answer=sector_answer,
                uvalue=user_data["sector"],
            )
            nb_created_answers += 3

        self.stdout.write(
            self.style.SUCCESS(
                "  Number of created questions: {}".format(nb_created_answers)
            )
        )
