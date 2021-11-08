# -*- coding: utf-8 -*-

import os
from datetime import datetime
from weasyprint import HTML, CSS

from django.template.loader import render_to_string

from django.conf import settings
from django.utils.translation import gettext as _
from survey.models import (
    SurveyUser,
    SurveyQuestion,
    SurveyQuestionAnswer,
    SurveyUserAnswer,
)
from csskp.settings import CUSTOM
from survey.reporthelper import (
    generate_chart_png,
    calculateResult,
    getRecommendations,
    get_formatted_translations,
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


def create_html_report(user: SurveyUser, lang: str) -> str:
    """Generate a HTML report."""
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
    recommendations_list = getRecommendations(user, lang)

    # Get the list of questions
    # questions_translations = get_formatted_translations(lang, "Q")
    # answers_translations = get_formatted_translations(lang, "A")
    questions_list = SurveyQuestion.objects.all().order_by("qindex")
    # answers_list = []
    # user_answers_values = []
    questions = []
    for index, question in enumerate(questions_list):

        questions.append(
            {
                "question": question,
                "possible_answers": SurveyQuestionAnswer.objects.filter(
                    question=question
                ).order_by("aindex"),
                "user_answers": SurveyUserAnswer.objects.filter(
                    user=user,
                ),
            }
        )
        # answers_list = SurveyQuestionAnswer.objects.filter(question=question).order_by(
        #     "aindex"
        # )
        # user_answers = SurveyUserAnswer.objects.filter(user=user)
        # user_answers_values = {}
        # for user_answer in user_answers:
        #     user_answers_values[user_answer.answer_id] = user_answer
        # for answer in answers_list:
        #     user_answer = user_answers_values[answer.id]

    # Render the HTML file
    output_from_parsed_template = render_to_string(
        "report/template.html",
        {
            "REPORT_TITLE": _("Final report"),
            "CASES_LOGO": cases_logo,
            "SECIN_LOGO": secin_logo,
            "TOOL_LOGO": tool_logo,
            "TOOL_NAME": CUSTOM["tool_name"],
            "DATE": datetime.today(),
            "SURVEY_USER": user,
            "CHART": chart_png_base64,
            "SCORE": score,
            "recommendations": recommendations_list,
            "questions": questions,
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
