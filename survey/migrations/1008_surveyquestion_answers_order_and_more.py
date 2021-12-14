# Generated by Django 4.0 on 2021-12-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '1007_auto_20211209_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='answers_order',
            field=models.CharField(default='aindex', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='qtype',
            field=models.CharField(choices=[
                ('M', 'Multiple Choice'),
                ('S', 'Single Choice'),
                ('SS', 'Single Select Choice'),
                ('T', 'Free text'),
                ('MT', 'Multiple Choice + Free Text'),
                ('ST', 'Single Choice + Free Text')
            ], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='surveyquestionanswer',
            name='dependant_answers',
            field=models.ManyToManyField(blank=True, to='survey.SurveyQuestionAnswer'),
        ),
    ]
