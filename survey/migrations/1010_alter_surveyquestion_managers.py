# Generated by Django 4.0 on 2022-01-07 14:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '1009_rename_choosen_lang_surveyuser_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='surveyquestion',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
