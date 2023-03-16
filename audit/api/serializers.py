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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Company.objects.create(**validated_data)


class AuditQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditQuestion
        fields = ["id", "references", "observations", "status"]
