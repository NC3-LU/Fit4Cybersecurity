from django.contrib import admin

from audit.models import Company
from audit.models import AuditUser
from audit.models import Audit
from audit.models import AuditCompanyUser

admin.site.register(Company)
admin.site.register(AuditUser)
admin.site.register(Audit)
admin.site.register(AuditCompanyUser)
