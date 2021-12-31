# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _
from csskp.settings import CUSTOM

DEFAULT_SECTOR_CHOICES = [
    ("BANK", _("Banking, insurance and real estate")),
    ("SALE", _("Trading, sales and mass distribution")),
    ("MARK", _("Marketing, media and multimedia")),
    ("BUIL", _("Construction industries and civil engineering")),
    ("REST", _("Hotel and restoration, tourism and entertainment")),
    ("INDU", _("Industry")),
    ("INST", _("Installation and maintenance")),
    ("ARTI", _("Creation or placing of objects that are artistic and decorative")),
    ("HEAL", _("Health")),
    ("SERV", _("Home-Care Service or Community Service")),
    ("SHOW", _("Shows")),
    ("SUPP", _("Company Support")),
    ("LOGI", _("Transport and Logistics")),
    ("FARM", _("Farming and fishing, natural spaces and green spaces, animal care")),
    ("PUBL", _("Public administration")),
]

SECTOR_CHOICES = DEFAULT_SECTOR_CHOICES
if "sectors" in CUSTOM.keys() and len(CUSTOM["sectors"]) > 0:
    SECTOR_CHOICES = CUSTOM["sectors"]

DEFAULT_COUNTRIES = [
    ("LU", "Luxembourg"),
    ("DE", "Deutschland"),
    ("BE", "Belgique"),
    ("FR", "France"),
]

COUNTRIES = DEFAULT_COUNTRIES
if "countries" in CUSTOM.keys() and len(CUSTOM["countries"]) > 0:
    COUNTRIES = CUSTOM["countries"]

SERVICE_TARGETS = [
    ("SME", "Small to Medium Size Entreprises"),
    ("BC", "Big Company"),
    ("MN", "Multinationals Coorporations"),
    ("IND", "Independent"),
    ("PRI", "Private Person"),
]

DEFAULT_COMPANY_SIZE = [
    ("a", "1-5"),
    ("b", "6-10"),
    ("c", "10-20"),
    ("d", "20-50"),
    ("e", "50-100"),
    ("f", "100-200"),
    ("g", "200-500"),
    ("h", "500-1000"),
    ("i", "1000-5000"),
    ("j", "5000+"),
]

COMPANY_SIZE = DEFAULT_COMPANY_SIZE
if "company_size" in CUSTOM.keys() and len(CUSTOM["company_size"]) > 0:
    COMPANY_SIZE = CUSTOM["company_size"]

QUESTION_TYPES = [
    ("M", "Multiple Choice"),
    ("S", "Single Choice"),
    ("SS", "Single Select Choice"),
    ("T", "Free text"),
    ("MT", "Multiple Choice + Free Text"),
    ("ST", "Single Choice + Free Text"),
]

ANSWER_TYPES = [
    ("P", "Predefined answer"),
    ("T", "Free text"),
]

TRANSLATION_TYPES = [
    ("Q", "Question"),
    ("A", "Answer"),
    ("R", "Recommendation"),
    ("S", "Question Section"),
    ("C", "Company Service Category"),
]
