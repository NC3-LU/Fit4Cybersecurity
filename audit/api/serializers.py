from rest_framework import serializers

from audit.models import AuditQuestion
from audit.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "address_street",
            "address_zip_code",
            "address_city",
            "address_country",
            "phone",
            "email",
            "type",
            "is_active",
        ]


class AuditQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditQuestion
        fields = ["id", "references", "observations", "status"]
