# Generated by Django 4.2.16 on 2024-09-30 13:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "1014_alter_surveyuser_user_id_surveyquestionmaxscore_and_more"),
    ]

    operations = [
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
                    ("CT", "Context with Text"),
                ],
                default="M",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="surveyuser",
            name="user_id",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.CreateModel(
            name="SurveyUserCustomAnswer",
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
                ("question", models.CharField(default="0", max_length=100)),
                ("answer", models.TextField(blank=True, default="")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.surveyuser",
                    ),
                ),
            ],
        ),
    ]
