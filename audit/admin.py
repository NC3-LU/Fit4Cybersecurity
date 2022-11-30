from django.contrib import admin
from audit.models import (
    Company,
    AuditUser,
    Certificate,
    Audit,
    AuditByCompany,
    AuditByUser,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "type", "is_active"]
    list_filter = ["type"]
    search_fields = ["name"]


@admin.register(AuditUser)
class AuditUserAdmin(admin.ModelAdmin):
    list_display = ["user", "company"]
    list_filter = ["company"]
    search_fields = ["user", "company"]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = [
        "status",
        "validate_by_company",
        "validate_by_user",
        "validation_date",
        "revocation_date",
    ]
    list_filter = ["status", "validate_by_company", "validate_by_user"]
    search_fields = ["validate_by_company", "validate_by_user"]


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ["survey_user", "product_name", "product_ref", "certificate"]
    search_fields = ["product_name", "product_ref"]


@admin.register(AuditByCompany)
class AuditByCompanyAdmin(admin.ModelAdmin):
    list_display = ["audit", "audit_company"]
    list_filter = ["audit_company"]
    search_fields = ["audit", "audit_company"]


@admin.register(AuditByUser)
class AuditByUserAdmin(admin.ModelAdmin):
    def get_audit(self, obj):
        return obj.audit_by_company.audit

    get_audit.short_description = "Audit"

    list_display = ["audit_user", "audit_by_company", "get_audit"]
    list_filter = ["audit_user"]
    search_fields = ["audit_user", "audit_by_company"]
