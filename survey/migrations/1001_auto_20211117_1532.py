# Generated by Django 3.2.9 on 2021-11-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "1000_alter_company_contact_address_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="surveyuser",
            name="choosen_lang",
            field=models.CharField(
                choices=[("en", "English"), ("fr", "French")],
                default="en",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="translationkey",
            name="lang",
            field=models.CharField(
                choices=[("en", "English"), ("fr", "French")],
                default="en",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="Translation",
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
                ("original", models.TextField()),
                ("translated", models.TextField()),
                (
                    "lang",
                    models.CharField(
                        choices=[("en", "English"), ("fr", "French")],
                        default="en",
                        max_length=2,
                    ),
                ),
            ],
            options={
                "unique_together": {("lang", "id")},
            },
        ),
    ]