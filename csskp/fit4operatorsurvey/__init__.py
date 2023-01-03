from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "OperatorSurvey",
    "intro_text": gettext_lazy(
        "This survey aims to identify the level of maturity "
        "of the operators in Luxembourg with respect to risk management and governance, "
        "collaboration on national and EU level and Incident reporting. We collect the "
        "answers to these 30 questions to understand where guidance and knowledge is "
        "already advanced and where there is room for improvement. "
        "As such, it is recommended that a person is taking this survey that is knowing "
        "the company's maturity on the aforementioned topics well. "
        "<br /><br />"
        "The survey will be online and available between December 2021 and April 30th 2022. "
        "After the survey, the data will be processed and results will be interpreted. "
        "However, since the survey is completely anonymous, we cannot identify you nor "
        "your company and thus deletion of specific records is not possible: we cannot "
        "be sure that it is indeed your survey. The results will be made available "
        "through another channel."
        "<br /><br />"
        "If you are not able to do the survey in one go and you want to later "
        "pick up where you have left off, please be sure to save the link by clicking "
        'on the "continue later" button. '
        "We will not be able to help you to find your answers again otherwise."
    ),
    "countries_first": [],
    "defaultLanguage": "en",
    "languages": [
        ("en", "English"),
    ],
    # Logos paths
    "tool_logo": "static/images/logo-fit4operatorsurvey.png",
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/style.css",
    # Minimal score
    "minimal_acceptable_score": 65,
    # Show or not the questions number left to complete the survey.
    "show_progress_questions_numbers": True,
    # Custom parts of templates
    #   main dir for PARTS_TEMPLATE_DIR:
    "templates_parts_dir": "templates/parts",
    "templates_parts": {
        # path of the templates parts
        "terms": "terms_part.html",
        "footer": "footer_part.html",
        "main_logo": "logo_part.html",
    },
    # Available modules
    "modules": {
        "reportDownload": True,
        "reportEmail": False,
        "requestDiagnostic": False,
        "requestTraining": False,
        "displayResults": False,
    },
    # Available report parts
    "report": {
        "introduction": True,
        "description": False,
        "results": False,
        "recommendations": True,
        "questions": True,
    },
    # Available stats charts
    "stats": {
        "activity": True,
        "sector": True,
        "size": True,
        "country": True,
        "status": True,
        "language": False,
        "section": False,
        "category": False,
    },
    "chart_exclude_sections": [],
}
