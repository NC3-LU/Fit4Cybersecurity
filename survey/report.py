# -*- coding: utf-8 -*-

import os
from datetime import datetime
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext as _
from survey.models import SurveyUser
from csskp.settings import CUSTOM
from survey.reporthelper import (
    generate_chart_png,
    calculateResult,
    getRecommendations,
)  # temporary imports
from survey.viewLogic import get_questions_with_user_answers


def create_html_report(user: SurveyUser, lang: str) -> str:
    """Generate a HTML report."""
    translation.activate(lang)
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
        ).decode()
    except Exception as e:
        chart_png_base64 = None
        print(e)

    # Get the list of recommendations
    recommendations_list = getRecommendations(user, lang)

    # Get the list of questions
    question_list = get_questions_with_user_answers(user)

    # Render the HTML file
    output_from_parsed_template = render_to_string(
        "report/template.html",
        {
            "REPORT_TITLE": _("Final report"),
            "CUSTOM": CUSTOM,
            "CASES_LOGO": cases_logo,
            "SECIN_LOGO": secin_logo,
            "TOOL_LOGO": tool_logo,
            "DATE": datetime.today(),
            "SURVEY_USER": user,
            "CHART": chart_png_base64,
            "SCORE": score,
            "recommendations": recommendations_list,
            "questions": question_list,
        },
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
