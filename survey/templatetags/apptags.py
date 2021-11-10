# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.utils import translation
from datetime import datetime

register = template.Library()


@register.filter(name="translate")
def translate(string: str, language: str) -> str:
    with translation.override(language):
        return translation.gettext(string)


@register.filter(name="format_datetime")
def format_datetime(value: datetime, format: str = "medium") -> str:
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


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
