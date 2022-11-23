from django.db import models


# Create your models here.
class Audit(models.Model):
    # QuestionCatID

    label = models.TextField()
    company_name = models.TextField()
    # survey_user = models.OneToOneField(models.SurveyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Auditor(models.Model):
    # QuestionCatID

    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.label
