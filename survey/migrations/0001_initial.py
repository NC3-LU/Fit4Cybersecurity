# Generated by Django 2.2.3 on 2019-09-09 11:30

from django.db import migrations, models
import django.db.models.deletion
from csskp.settings import LANGUAGES, LANGUAGE_CODE
import uuid
from survey.globals import (
    QUESTION_TYPES,
    SERVICE_TARGETS,
)
from survey.models import SURVEY_STATUS_IN_PROGRESS

LOCAL_DEFAULT_LANG = LANGUAGE_CODE


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SurveyQuestion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titleKey", models.CharField(max_length=32)),
                (
                    "tooltip",
                    models.TextField(null=False, blank=True, default=""),
                ),
                (
                    "qtype",
                    models.CharField(choices=QUESTION_TYPES, default="M", max_length=1),
                ),
                ("qindex", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SurveyQuestionAnswer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answerKey", models.CharField(max_length=32)),
                (
                    "tooltip",
                    models.TextField(null=False, blank=True, default=""),
                ),
                ("aindex", models.IntegerField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.SurveyQuestion",
                    ),
                ),
                ("uniqueAnswer", models.BooleanField(default=False)),
                ("score", models.IntegerField(default=0)),
            ],
            options={
                "unique_together": {("aindex", "question")},
            },
        ),
        migrations.CreateModel(
            name="SurveyQuestionServiceCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titleKey", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="SurveySection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sectionTitleKey", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="SurveyUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.UUIDField(default=uuid.uuid4)),
                ("sector", models.CharField(max_length=4)),
                ("e_count", models.CharField(max_length=2)),
                (
                    "chosenLang",
                    models.CharField(
                        choices=LANGUAGES, default=LOCAL_DEFAULT_LANG, max_length=2
                    ),
                ),
                ("current_qindex", models.IntegerField(default=0)),
                ("status", models.SmallIntegerField(default=SURVEY_STATUS_IN_PROGRESS)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TranslationKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=32)),
                ("text", models.TextField()),
                (
                    "lang",
                    models.CharField(
                        choices=LANGUAGES, default=LOCAL_DEFAULT_LANG, max_length=2
                    ),
                ),
                ("ttype", models.CharField(default="Q", max_length=1)),
            ],
            options={
                "unique_together": {("lang", "id")},
            },
        ),
        migrations.CreateModel(
            name="SurveyUserAnswer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uvalue", models.IntegerField(default=0)),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.SurveyQuestionAnswer",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.SurveyUser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="surveyquestion",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="survey.SurveySection"
            ),
        ),
        migrations.AddField(
            model_name="surveyquestion",
            name="service_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="survey.SurveyQuestionServiceCategory",
            ),
        ),
        migrations.AddField(
            model_name="surveyquestion",
            name="maxPoints",
            field=models.IntegerField(default=10),
        ),
        migrations.CreateModel(
            name="Recommendations",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("textKey", models.CharField(max_length=32)),
                ("min_e_count", models.CharField(default='a', max_length=2)),
                ("max_e_count", models.CharField(default='z', max_length=2)),
                (
                    "sector",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=4,
                        null=True,
                    ),
                ),
                ("answerChosen", models.BooleanField(default=False)),
                (
                    "forAnswer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.SurveyQuestionAnswer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("contact_email", models.EmailField(max_length=254)),
                ("contact_tel", models.TextField(max_length=32)),
                ("contact_address_street", models.CharField(max_length=128)),
                ("contact_address_city", models.CharField(max_length=64)),
                ("contact_address_country", models.CharField(max_length=64)),
                ("contact_address_number", models.IntegerField()),
                ("contact_address_postcode", models.CharField(max_length=10)),
                ("notes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CompanyService",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("target", models.CharField(choices=SERVICE_TARGETS, max_length=3)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.SurveyQuestionServiceCategory",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="survey.Company"
                    ),
                ),
            ],
        ),
    ]
