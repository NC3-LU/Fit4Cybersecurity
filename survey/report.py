# -*- coding: utf-8 -*-

import os
from datetime import datetime
from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader

from django.conf import settings
from django.utils.translation import gettext as _
from survey.models import SurveyUser
from csskp.settings import CUSTOM
from survey.reporthelper import (
    generate_chart_png,
    calculateResult,
    getRecommendations,
)  # temporary imports

from django.utils.translation import gettext, ngettext


def format_datetime(value: str, format: str = "medium") -> str:
    """Custom Jinja filter to format a datetime object."""
    if format == "full":
        format = "%Y-%m-%d %H:%M"
    elif format == "medium":
        format = "%Y-%m-%d %H:%M"
    elif format == "compact":
        format = "%Y-%m-%d"
    return value.strftime(format)


def environment() -> Environment:
    """Define an environment for Jinja, adds the i18n extension, the filters
    and make available the variable CUSTOM."""
    filepath = os.path.join(settings.BASE_DIR, settings.REPORT_TEMPLATE_DIR)
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
    env.filters["format_datetime"] = format_datetime
    env.globals["CUSTOM"] = CUSTOM
    return env


def create_html_report(user: SurveyUser, lang: str) -> str:
    """Generate a HTML report."""
    env = environment()
    template = env.get_template("template.html")

    cases_logo = os.path.abspath(
        os.path.join(settings.REPORT_TEMPLATE_DIR, "images/cases_logo.svg")
    )
    secin_logo = os.path.abspath(
        os.path.join(settings.REPORT_TEMPLATE_DIR, "images/secin_logo.svg")
    )
    tool_logo = os.path.abspath(os.path.join(settings.BASE_DIR, CUSTOM["logoFull"]))

    # Calculate the result
    score, details, section_list = calculateResult(user, lang)

    # Generate the chart
    try:
        chart_png_base64 = generate_chart_png(
            user, details, section_list, lang, "base64"
        )
    except Exception as e:
        chart_png_base64 = None
        print(e)

    # Get the list of recommendations
    recommendationList = getRecommendations(user, lang)

    # Render the HTML file
    output_from_parsed_template = template.render(
        REPORT_TITLE=_("Final report"),
        CASES_LOGO=cases_logo,
        SECIN_LOGO=secin_logo,
        TOOL_LOGO=tool_logo,
        TOOL_NAME=CUSTOM["tool_name"],
        DATE=datetime.today(),
        SURVEY_USER=user,
        CHART=chart_png_base64,
        SCORE=score,
        recommendations=recommendationList,
    )

    return output_from_parsed_template


def makepdf(html: str) -> bytes:
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html)
    stylesheets = [
        CSS(
            os.path.abspath(
                os.path.join(settings.REPORT_TEMPLATE_DIR, "css/custom.css")
            )
        )
    ]
    return htmldoc.write_pdf(stylesheets=stylesheets)
