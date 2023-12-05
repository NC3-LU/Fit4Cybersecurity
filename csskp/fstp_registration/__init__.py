from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "FSTP Registration",
    "intro_text": gettext_lazy(
        "TO BE DEFINED 895"
    ),
    "countries_first": [
        "LU",
        "BE",
        "FR",
        "DE",
        "NL",
        "GB",
    ],
    "defaultLanguage": "en",
    "languages": [
        ("en", "English"),
    ],
    # Logos paths
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
        "terms": "fstp_registration/terms_part.html",
        "footer": "fstp_registration/footer_part.html",
        "main_logo": "fstp_registration/logo_part.html",
        "privacy": "fstp_registration/privacy_policy_part.html",
    },
    # Available modules
    "modules": {
        "reportDownload": True,
        "reportEmail": True,
        "requestDiagnostic": False,
        "requestTraining": False,
        "displayResults": False,
    },
    # Available report parts
    "report": {
        "introduction": True,
        "description": True,
        "results": False,
        "recommendations": False,
        "questions": True,
    },
    # Available stats charts
    "stats": {
        "activity": False,
        "sector": False,
        "size": False,
        "country": False,
        "status": False,
        "language": False,
        "section": False,
        "category": False,
        "current_question": False,
    },
    "chart_exclude_sections": [],
}
