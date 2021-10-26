# -*- coding: utf-8 -*-

from django import template
from django.utils import translation

register = template.Library()


@register.filter(name="translate")
def translate(string: str, language: str) -> str:
    with translation.override(language):
        return translation.gettext(string)
