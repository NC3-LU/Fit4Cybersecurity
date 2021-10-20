from django import template
from django.utils import translation

register = template.Library()


@register.filter(name="translate")
def translate(string, language):
    with translation.override(language):
        return translation.gettext(string)
