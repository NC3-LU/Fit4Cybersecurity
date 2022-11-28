from django.db import models
from survey.models import SurveyUser
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.TextField()
    admin_email = models.EmailField()
    admin_first_name = models.TextField()
    admin_last_name = models.TextField()


class AuditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Audit(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    product_name = models.TextField()
    product_ref = models.TextField()
    certificate_status = models.TextField()
    certificate_revocation_date = models.DateField()


class AuditCompanyUser(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    company_user = models.ForeignKey(AuditUser, on_delete=models.CASCADE)
