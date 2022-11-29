from django.contrib import admin
from audit.models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'email', 'phone']
    list_filter = ['type']
    search_fields = ['name']


@admin.register(AuditUser)
class AuditUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'company']
    list_filter = ['company']
    search_fields = ['user','company']


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ['survey_user', 'product_name', 'product_ref', 'certificate_status', 'certificate_revocation_date']
    list_filter = ['certificate_status']
    search_fields = ['product_name','product_ref']

@admin.register(AuditByUser)
class AuditByUserAdmin(admin.ModelAdmin):
    list_display = ['audit_user', 'audit']
    list_filter = ['audit_user']
    search_fields = ['audit_user','audit']