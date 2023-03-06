from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "FitCyber4Africa",
    "intro_text": gettext_lazy(
        "This survey will ask a few questions and provide "
        "recommendations. Keep in mind, that it is a self-assessment tool and that it "
        "only touches the surface of information security by giving a very basic maturity "
        "level estimate and some basic recommendations."
    ),
    "countries_first": [],
    "defaultLanguage": "en",
    "defaultCountryCode": "SN",
    "languages": [
        ("en", "English"),
        ("fr", "French"),
        ("de", "German"),
    ],
    # Logos paths
    "tool_logo": "static/images/logo-fit4operatorsurvey.png",
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/custom.css",
    # Minimal score
    "minimal_acceptable_score": 65,
    # Show or not the questions number left to complete the survey.
    "show_progress_questions_numbers": True,
    # Custom parts of templates
    #   main dir for PARTS_TEMPLATE_DIR:
    "templates_parts_dir": "templates/parts/fit4africa",
    "templates_parts": {
        # path of the templates parts
        "terms": "terms_part.html",
        "footer": "footer_part.html",
        "main_logo": "logo_part.html",
    },
    # Available modules
    "modules": {
        "reportDownload": True,
        "reportEmail": True,
        "requestDiagnostic": False,
        "requestTraining": False,
        "displayResults": True,
    },
    # Available report parts
    "report": {
        "introduction": True,
        "description": True,
        "results": True,
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
    "is_simple_questionnaire_tree": True,
}
