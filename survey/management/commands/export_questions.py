# -*- coding: utf-8 -*-

import json
import argparse
from django.core.management.base import BaseCommand
from survey.lib.utils import export_survey


class Command(BaseCommand):
    help = """Export a set of questions and answers.
    Usage: ``python manage.py export_questions >> out.json``"""

    def add_arguments(self, parser):
        parser.add_argument("--with-ids", action=argparse.BooleanOptionalAction)

    def handle(self, *args, **options):
        result = export_survey(options["with_ids"])
        print(json.dumps(result, indent=2, sort_keys=True))
