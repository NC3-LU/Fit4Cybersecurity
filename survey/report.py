# -*- coding: utf-8 -*-

import os
import base64
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


from django.conf import settings
from survey.models import SurveyUser


from django.utils.translation import gettext, ngettext


def environment() -> Environment:
    """Define an environment for Jinja and adds the i18n extension."""
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
    return env


def create_html_report(user: SurveyUser, lang: str) -> str:
    """Generate a HTML report."""
    env = environment()
    template = env.get_template("template.html")
    output_from_parsed_template = template.render(
        REPORT_TITLE="Fit4Cybersecurity report",
        SURVEY_USER=user,
    )

    return output_from_parsed_template


def makepdf(html):
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html)
    return htmldoc.write_pdf()

    # other example:
    pdf_content = HTML(string=html).write_pdf()
    b64_content = base64.b64encode(pdf_content)
    return pdf_content
    # return {'pdf': b64_content}
