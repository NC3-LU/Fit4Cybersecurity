# -*- coding: utf-8 -*-

from rest_framework import serializers
from survey.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ["original", "translated", "lang"]
