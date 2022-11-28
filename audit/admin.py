from django.contrib import admin

from audit.models import AuditCompany
from audit.models import CompanyUser
from audit.models import Auditor
from audit.models import Audit
from audit.models import AuditAuditor
from audit.models import AuditCompanyUser

admin.site.register(AuditCompany)
admin.site.register(CompanyUser)
admin.site.register(Auditor)
admin.site.register(Audit)
admin.site.register(AuditAuditor)
admin.site.register(AuditCompanyUser)
