# -*- coding: utf-8 -*-

from django.db import connection
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load data from SQL. Temporary solution. This command should not be used."

    def add_arguments(self, parser):
        parser.add_argument("sql_file", type=str, help="The path of the SQL file.")

    def handle(self, *args, **options):
        file_path = options["sql_file"]
        sql_statement = open(file_path).read()
        with connection.cursor() as c:
            c.execute(sql_statement)

        self.stdout.write(self.style.SUCCESS("Data imported."))
