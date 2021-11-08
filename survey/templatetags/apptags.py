# -*- coding: utf-8 -*-

from django import template
from django.utils import translation
from csskp.settings import LANGUAGE_CODE

from survey.models import (
    TranslationKey,
)

register = template.Library()


@register.filter(name="translate")
def translate(string: str, language: str) -> str:
    with translation.override(language):
        return translation.gettext(string)


@register.filter(name="format_datetime")
def format_datetime(value: str, format: str = "medium") -> str:
    """Custom Jinja filter to format a datetime object."""
    if format == "full":
        format = "%Y-%m-%d %H:%M"
    elif format == "medium":
        format = "%Y-%m-%d %H:%M"
    elif format == "compact":
        format = "%Y-%m-%d"
    return value.strftime(format)


@register.filter(name="ifinlist")
def ifinlist(value, list):
    return True if str(value) in list else False
