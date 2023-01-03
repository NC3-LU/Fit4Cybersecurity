import logging
import os
from datetime import datetime

from django.conf import settings
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils import translation
from weasyprint import CSS
from weasyprint import HTML

from csskp.settings import CUSTOM
from csskp.settings import SITE_IMAGES_DIR
from survey import globals
from survey.models import SurveyUser
from survey.reporthelper import calculateResult
from survey.reporthelper import generate_chart_png
from survey.reporthelper import getRecommendations
from survey.viewLogic import get_questions_with_user_answers

# Get an instance of a logger
logger = logging.getLogger(__name__)

right_cover_logo = os.path.abspath(
    os.path.join(settings.BASE_DIR, CUSTOM["right_cover_logo"])
)
left_cover_logo = os.path.abspath(
    os.path.join(settings.BASE_DIR, CUSTOM["left_cover_logo"])
)


def create_html_report(user: SurveyUser, lang: str, request: HttpRequest) -> str:
    """Generate a HTML report."""
    translation.activate(lang)

    # Calculate the result
    (
        score,
        bonus_score,
        sections_data,
        sections_labels,
        categories_data,
        categories_labels,
    ) = calculateResult(user)

    # Generate the chart
    try:
        section_chart_png_base64 = generate_chart_png(
            user, sections_data, sections_labels, "base64"
        )
        category_chart_png_base64 = generate_chart_png(
            user, categories_data, categories_labels, "base64"
        )
    except AssertionError as e:
        logger.error(e)
        section_chart_png_base64 = None
        category_chart_png_base64 = None
    except Exception as e:
        logger.error(f"Error when generating the PNG chart: {e}.")
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
            "RIGHT_COVER_LOGO": right_cover_logo,
            "LEFT_COVER_LOGO": left_cover_logo,
            "BASE_DIR": settings.BASE_DIR,
            "TOOL_LOGO": SITE_IMAGES_DIR + "/logo-" + lang + ".png",
            "DATE": datetime.today(),
            "SURVEY_USER": user,
            "CONTEXT": user.get_all_context_answers(),
            "SECTION_CHART": section_chart_png_base64,
            "CATEGORY_CHART": category_chart_png_base64,
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
                --left_logo_url: url("'''
            + left_cover_logo
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
