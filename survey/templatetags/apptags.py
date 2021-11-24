# -*- coding: utf-8 -*-

from datetime import datetime
from django import template
from django.conf import settings
from django.utils import translation
from survey.reporthelper import get_translation

register = template.Library()


@register.filter(name="translate")
def translate(string: str, language: str) -> str:
    with translation.override(language):
        return translation.gettext(string)


@register.filter(name="translate_db")
def translate_db(string: str, language: str) -> str:
    return get_translation(string, language)


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


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter
def find_tuple(list, key):
    """Find an element in a list of tuples with key of the element
    (first item of the tuple).
    Example:
    liste|find_tuple:'ENER'
    """
    try:
        return next(elem[1] for elem in list if elem[0] == key)
    except StopIteration:
        return None
