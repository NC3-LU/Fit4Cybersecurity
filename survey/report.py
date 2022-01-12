# -*- coding: utf-8 -*-

import os
import logging
from datetime import datetime
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import translation
from django.http import HttpRequest
from survey.models import SurveyUser
from csskp.settings import CUSTOM, SITE_IMAGES_DIR
from survey.reporthelper import (
    generate_chart_png,
    calculateResult,
    getRecommendations,
)  # temporary imports
from survey.viewLogic import get_questions_with_user_answers
from survey import globals

# Get an instance of a logger
logger = logging.getLogger(__name__)

cases_logo = os.path.abspath(os.path.join(settings.BASE_DIR, CUSTOM["cases_logo"]))
secin_logo = os.path.abspath(os.path.join(settings.BASE_DIR, CUSTOM["secin_logo"]))


def create_html_report(user: SurveyUser, lang: str, request: HttpRequest) -> str:
    """Generate a HTML report."""
    translation.activate(lang)

    # Calculate the result
    score, bonus_score, details, section_list = calculateResult(user)

    # Generate the chart
    try:
        chart_png_base64 = generate_chart_png(user, details, section_list, "base64")
    except AssertionError as e:
        logger.error(e)
        chart_png_base64 = None
    except Exception as e:
        logger.error("Error when generating the PNG chart: {}.".format(e))
        chart_png_base64 = None
        raise e

    # Get the list of recommendations
    recommendations_list = getRecommendations(user, lang)

    # Get the list of questions
    question_list = get_questions_with_user_answers(user)

    # Render the HTML file
    output_from_parsed_template = render_to_string(
        "report/template.html",
        {
            "GLOBALS": globals,
            "CASES_LOGO": cases_logo,
            "SECIN_LOGO": secin_logo,
            "TOOL_LOGO": SITE_IMAGES_DIR + "/logo-" + lang + ".png",
            "DATE": datetime.today(),
            "SURVEY_USER": user,
            "CONTEXT": user.get_all_context_answers(),
            "CHART": chart_png_base64,
            "SCORE": str(score),
            "BONUS_SCORE": bonus_score,
            "recommendations": recommendations_list,
            "questions": question_list,
        },
        request=request,
    )

    return output_from_parsed_template


def makepdf(html: str, lang: str) -> bytes:
    """Generate a PDF file from a string of HTML."""
    base_url = os.path.abspath(settings.REPORT_TEMPLATE_DIR)
    htmldoc = HTML(string=html, base_url=base_url)

    stylesheets = [
        CSS(
            string='''
            :root {
                --tool_logo_url: url("'''
            + SITE_IMAGES_DIR
            + "/logo-"
            + lang
            + ".png"
            + '''");
                --secin_logo_url: url("'''
            + secin_logo
            + """");
            }
            """
        ),
        CSS(
            os.path.join(
                settings.BASE_DIR, settings.REPORT_TEMPLATE_DIR, "css/custom.css"
            )
        ),
    ]

    return htmldoc.write_pdf(stylesheets=stylesheets)
