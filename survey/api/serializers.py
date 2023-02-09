from rest_framework import serializers

from survey.models import SurveyQuestion
from survey.models import SurveyQuestionAnswer


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ["section", "label", "tooltip", "qindex", "maxPoints"]


class SurveyQuestionAnszerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAnswer
        fields = ["label", "value"]
