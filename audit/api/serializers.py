from rest_framework import serializers

from audit.models import Audit
from audit.models import AuditQuestion
from audit.models import Company
from survey.models import SurveyUser


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
        Create and return a new instance, given the validated data.
        """
        return Company.objects.create(**validated_data)


class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = ["id", "product_name", "product_ref", "status"]


class AuditRequestSerializer(serializers.ModelSerializer):
    survey_user = serializers.SlugRelatedField(
        queryset=SurveyUser.objects.all(), slug_field="user_id"
    )

    class Meta:
        model = Audit
        fields = ["survey_user", "product_name", "product_ref", "status"]

    def create(self, validated_data):
        """
        Create and return a new instance, given the validated data.
        """
        # print(validated_data)
        return Audit.objects.create(**validated_data)


class AuditQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditQuestion
        fields = ["id", "references", "observations", "status"]
