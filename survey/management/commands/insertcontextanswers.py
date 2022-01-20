# -*- coding: utf-8 -*-

"""insertcontextanswers.py - Generate JSON files with the output of the command:

$ python manage.py dumpdata --indent 2 survey.surveyuser > contrib/out.json
$ python manage.py insertcontextanswers
"""

import json
import argparse
from django.core.management.base import BaseCommand
from survey.models import SurveyUserAnswer, SurveyQuestionAnswer


class Command(BaseCommand):
    help = """Export a set of questions and answers.
    Usage: ``python manage.py export_questions >> out.json``"""

    def handle(self, *args, **options):
        with open("./contrib/out.json") as f:
            data = json.loads(f.read())

        users = [elem for elem in data if elem["model"] == "survey.surveyuser"]

        questions_json = []
        for user in users:

            print(user)

            SurveyQuestionAnswer()
