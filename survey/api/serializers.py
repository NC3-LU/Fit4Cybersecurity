from rest_framework import serializers

from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer
from survey.models import SurveySection
from survey.models import SurveyUser


class SurveySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveySection
        fields = ["id", "label"]


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ["section", "label", "tooltip", "qindex", "maxPoints"]


class SurveyQuestionAnszerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAnswer
        fields = ["label", "value"]


class SurveyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyUser
        fields = ["user_id", "chosen_lang", "status", "created_at", "updated_at"]
