# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _
from csskp.settings import CUSTOM


SERVICE_TARGETS = [
    ("SME", "Small to Medium Size Entreprises"),
    ("BC", "Big Company"),
    ("MN", "Multinationals Coorporations"),
    ("IND", "Independent"),
    ("PRI", "Private Person"),
]

QUESTION_TYPES = [
    ("M", "Multiple Choice"),
    ("S", "Single Choice"),
    ("SO", "Single Option Choice"),
    ("T", "Free text"),
    ("MT", "Multiple Choice + Free Text"),
    ("ST", "Single Choice + Free Text"),
    ("CL", "Countries list"),
]

ANSWER_TYPES = [
    ("P", "Predefined answer"),
    ("T", "Free text"),
]
