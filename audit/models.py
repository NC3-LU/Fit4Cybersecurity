import uuid
from typing import Any

from django.contrib.auth.models import User
from django.db import models

from audit.globals import CERTIFICATE_STATUS
from audit.globals import COMPANY_TYPE
from audit.globals import QUESTION_STATUS
from survey.models import SurveyQuestion
from survey.models import SurveyUser


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

    # Relationships
    members = models.ManyToManyField(User, blank=True)

    # Foreign keys
    company_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="company_admin"
    )

    def __str__(self):
        return self.name


class AuditUser(models.Model):
    # Relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Foreign keys
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    User.add_to_class("__str__", User.get_full_name)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_all_audits(self) -> dict[str, Any]:
        auditsByUser = self.auditbyuser_set.all()

        for auditByUser in auditsByUser:
            auditByUser.audit_company_selected = (
                auditByUser.audit.auditbycompany_set.filter(
                    audit_company__type="AD"
                ).first()
            )
            auditByUser.audit.statusDetails = {}
            audit_questions = auditByUser.audit.survey_user.auditquestion_set.all()
            if audit_questions:
                for status in QUESTION_STATUS:
                    auditByUser.audit.statusDetails[status[1]] = audit_questions.filter(
                        status=status[0]
                    ).count()

        return auditsByUser


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
    status = models.CharField(
        max_length=2,
        choices=QUESTION_STATUS,
        default="OG",
    )
    audit_comments = models.TextField(null=True, blank=True, default=None)

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
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    audit_user = models.ForeignKey(AuditUser, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["audit", "audit_user"], name="unique_auditByUser"
            ),
        ]

    def __str__(self):
        return self.audit_user.user.first_name


class AuditQuestion(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    references = models.TextField(null=True, blank=True, default=None)
    observations = models.TextField(null=True, blank=True, default=None)
    status = models.CharField(
        max_length=2,
        choices=QUESTION_STATUS,
        default="OG",
    )

    def __str__(self):
        return self.status
