from django.db import models
from survey.models import SurveyUser
from django.contrib.auth.models import User
from audit.globals import *


class Company(models.Model):
    name = models.CharField(max_length=128)
    address_street = models.CharField("Street", max_length=128)
    address_zip_code = models.CharField("ZIP / Postal code", max_length=10)
    address_city = models.CharField("City", max_length=64)
    address_country = models.CharField("Country", max_length=64)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    type = models.CharField(
        max_length=2,
        choices=COMPANY_TYPE,
        default='CU',
    )

    def __str__(self):
        return self.name


class AuditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Audit(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    product_name = models.CharField("Product / Service name", max_length=128)
    product_ref = models.CharField(
        "Product / Service reference", max_length=128)
    certificate_status = models.CharField(
        max_length=2,
        choices=CERTIFICATE_STATUS,
        default='RQ',
    )
    certificate_revocation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.product_name


class AuditByUser(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    audit_user = models.ForeignKey(AuditUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.audit.product_name
