# Generated by Django 4.0.1 on 2022-01-14 12:39
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "1011_alter_surveyuseranswer_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyquestion",
            name="tooltip",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="surveyquestionanswer",
            name="tooltip",
            field=models.TextField(blank=True, default=""),
        ),
    ]
