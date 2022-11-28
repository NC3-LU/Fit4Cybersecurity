from django.db import models
from survey.models import SurveyUser


class Company(models.Model):
    name = models.TextField()
    admin_email = models.EmailField()
    admin_first_name = models.TextField()
    admin_last_name = models.TextField()


class AuditCompany(models.Model):
    name = models.TextField()
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=12)


class CompanyUser(models.Model):
    first_name = models.TextField()
    last_name =  models.TextField()
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Auditor(models.Model):
    first_name = models.TextField()
    last_name =  models.TextField()
    email = models.EmailField()
    company = models.ForeignKey(AuditCompany, on_delete=models.CASCADE)


class Audit(models.Model):
    survey_user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE)
    product_name = models.TextField()
    product_ref = models.TextField()
    certificate_status = models.TextField()
    certificate_revocation_date = models.DateField()


class AuditAuditor(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)


class AuditCompanyUser(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
