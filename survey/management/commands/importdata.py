# -*- coding: utf-8 -*-

import json
from django.core.management.base import BaseCommand, CommandError
from survey.models import SurveySection, SurveyQuestion


class Command(BaseCommand):
    help = "Import a set of questions and answers."

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="The path of the JSON file.")

    def handle(self, *args, **options):
        with open(options["json_file"]) as f:
            json_file = f.read()

        json_data = json.loads(json_file)

        for question in json_data:
            print(question["titleKey"])

            for answer in question["answers"]:
                print("  {}".format(answer["answerKey"]))



        #     try:
        #         poll = SurveyQuestion.objects.get_or_create(pk=poll_id)
        #     #except SurveyQuestion.DoesNotExist:
        #         #raise CommandError('"%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(self.style.SUCCESS("Data imported"))
