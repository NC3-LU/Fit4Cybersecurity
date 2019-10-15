# Generated by Django 2.2.6 on 2019-10-10 12:12

from django.db import migrations, connection
import os

def load_data_from_sql(apps, schema_editor):
   file_path = os.path.join(os.path.dirname(__file__), 'initial_data.sql')
   sql_statement = open(file_path).read()
   with connection.cursor() as c:
       c.execute(sql_statement)

class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
        ('survey', '0002_auto_20191010_1212'),
    ]

    operations = [
        migrations.RunPython(load_data_from_sql),
    ]