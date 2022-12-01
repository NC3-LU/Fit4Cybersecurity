import uuid

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
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    type = models.CharField(
        max_length=2,
        choices=COMPANY_TYPE,
        default="CS",
    )
    is_active = models.BooleanField("Active", default=False)

    def __str__(self):
        return self.name


class AuditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    User.add_to_class("__str__", User.get_full_name)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=2,
        choices=CERTIFICATE_STATUS,
        default="RQ",
    )
    validate_by_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True, default=None
    )
    validate_by_user = models.ForeignKey(
        AuditUser, on_delete=models.CASCADE, blank=True, null=True, default=None
    )
    validation_date = models.DateField(blank=True, null=True)
    revocation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Audit(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    product_name = models.CharField("Product / Service name", max_length=128)
    product_ref = models.CharField("Product / Service reference", max_length=128)
    certificate = models.OneToOneField(
        Certificate, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.product_name


class AuditByCompany(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    audit_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["audit", "audit_company"], name="unique_auditByCompany"
            ),
        ]

    def __str__(self):
        return self.audit_company.name


class AuditByUser(models.Model):
    audit_by_company = models.ForeignKey(AuditByCompany, on_delete=models.CASCADE)
    audit_user = models.ForeignKey(AuditUser, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["audit_by_company", "audit_user"], name="unique_auditByUser"
            ),
        ]

    def __str__(self):
        return self.audit_user.user.first_name
