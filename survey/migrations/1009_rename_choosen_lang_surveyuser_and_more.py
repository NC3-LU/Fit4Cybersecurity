# Generated by Django 4.0 on 2022-01-04 13:10
import django.db.models.deletion
from django.db import connection
from django.db import migrations
from django.db import models


def load_data_from_sql(apps, schema_editor):
    with connection.cursor() as c:
        c.execute("update survey_surveyquestion set qtype = 'SO' where qtype = 'SS';")


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "1008_surveyquestion_answers_order_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="surveyuser",
            old_name="choosen_lang",
            new_name="chosen_lang",
        ),
        migrations.AddField(
            model_name="surveyquestionanswer",
            name="value",
            field=models.CharField(blank=True, null=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name="company",
            name="contact_address_country",
            field=models.CharField(max_length=64),
        ),
        # Update the data in the db.
        migrations.RunPython(load_data_from_sql),
        migrations.AlterField(
            model_name="surveyquestion",
            name="qtype",
            field=models.CharField(
                choices=[
                    ("M", "Multiple Choice"),
                    ("S", "Single Choice"),
                    ("SO", "Single Option Choice"),
                    ("T", "Free text"),
                    ("MT", "Multiple Choice + Free Text"),
                    ("ST", "Single Choice + Free Text"),
                    ("CL", "Countries list"),
                ],
                default="M",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="surveyuseranswer",
            name="uvalue",
            field=models.CharField(default="0", max_length=100),
        ),
        migrations.AddField(
            model_name="surveyquestion",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="surveyquestionanswer",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="surveyuseranswer",
            name="answer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="survey.surveyquestionanswer",
            ),
        ),
    ]
