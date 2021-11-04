# -*- coding: utf-8 -*-

import os
from datetime import datetime
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

from django.conf import settings
from survey.models import SurveyUser
from csskp.settings import CUSTOM

from django.utils.translation import gettext, ngettext


def format_datetime(value: str, format: str = 'medium') -> str:
    """Custom Jinja filter to format a datetime object."""
    if format == 'full':
        format = "%Y-%m-%d %H:%M"
    elif format == 'medium':
        format = "%Y-%m-%d %H:%M"
    elif format == 'compact':
        format = "%Y-%m-%d"
    return value.strftime(format)


def environment() -> Environment:
    """Define an environment for Jinja, adds the i18n extension, the filters
    and make available the variable CUSTOM."""
    filepath = os.path.join(settings.BASE_DIR, settings.WORD_TEMPLATES_DIR)
    # i18n extension
    options = {}
    options["extensions"] = [
        "jinja2.ext.i18n",
        "jinja2.ext.autoescape",
        "jinja2.ext.with_",
    ]
    env = Environment(**options, loader=FileSystemLoader(filepath))
    # i18n template functions
    env.install_gettext_callables(gettext=gettext, ngettext=ngettext, newstyle=True)
    env.filters['format_datetime'] = format_datetime
    env.globals['CUSTOM'] = CUSTOM
    return env


def create_html_report(user: SurveyUser, lang: str) -> str:
    """Generate a HTML report."""
    env = environment()
    template = env.get_template("template.html")
    output_from_parsed_template = template.render(
        REPORT_TITLE="Fit4Cybersecurity report",
        DATE=datetime.today(),
        SURVEY_USER=user,
    )

    return output_from_parsed_template


def makepdf(html: str) -> bytes:
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html)
    return htmldoc.write_pdf()
