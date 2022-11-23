from django.contrib import admin

from .models import Audit
from .models import Auditor


class AuditAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Audit, AuditAdmin)
admin.site.register(Auditor, AuditAdmin)
