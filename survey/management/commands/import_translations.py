# -*- coding: utf-8 -*-

import json
from django.core.management.base import BaseCommand
from survey.models import (
    Translation,
)


class Command(BaseCommand):
    help = "Import a set of translations."

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="The path of the JSON file.")

    def handle(self, *args, **options):
        with open(options["json_file"]) as f:
            json_file = f.read()
        json_data = json.loads(json_file)

        for translation in json_data:
            translation_obj = Translation.objects.create(**translation)
            translation_obj.save()

        self.stdout.write(self.style.SUCCESS("Translations imported."))
