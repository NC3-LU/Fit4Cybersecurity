# Generated by Django 3.2.9 on 2021-11-17 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '1001_auto_20211117_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendations',
            old_name='textKey',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='surveyquestion',
            old_name='titleKey',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='surveyquestionanswer',
            old_name='answerKey',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='surveyquestionservicecategory',
            old_name='titleKey',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='surveysection',
            old_name='sectionTitleKey',
            new_name='label',
        ),
    ]
