from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey Market Cybersecurity Luxembourg",
    "intro_text": gettext_lazy(
        " The Luxembourg House of Cybersecurity (LHC) is the cybersecurity, agency for the private sector in Luxembourg. We are responsible for  supporting the development of the national cybersecurity ecosystem, and for promoting cybersecurity awareness and best practices. "
        " <br /> "
        " <br /> "
        "This survey is part of the market intelligence observatory of" 
        " the National Cybersecurity Competence Center (NC3). The NC3 is a "
        "department of the LHC and supported by the Ministry of the Economy." 
        " The observatory collects and analyzes data on the cybersecurity "
        "market in Luxembourg, in order to inform policy decisions and "
        "support the development of the ecosystem."
        " <br /> "
        " <br /> "
        "This survey is directed to providers of cybersecurity services "
        "and solutions in Luxembourg. Your participation is important to "
        "help us understand the current state of the market and the needs of "
        "businesses and organizations"
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
        ("fr", "French"),
        ("de", "German"),
    ],
    # Logos paths
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/style.css",
    # Minimal score
    "minimal_acceptable_score": 65,
    # Show or not the questions number left to complete the survey.
    "show_progress_questions_numbers": False,
    # Custom parts of templates
    #   main dir for PARTS_TEMPLATE_DIR:
    "templates_parts_dir": "templates/parts",
    "templates_parts": {
        # path of the templates parts
        "terms": "terms_part.html",
        "footer": "surveySMEDemand/footer_part.html",
        "main_logo": "logo_part.html",
        "privacy": "privacy_policy_part.html",
    },
    # Available modules
    "modules": {
        "displayProgressBar": True,
        "reportDownload": False,
        "reportEmail": False,
        "requestDiagnostic": False,
        "requestTraining": False,
        "displayResults": False,
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
        "country": False,
        "status": True,
        "language": True,
        "section": False,
        "category": False,
        "current_question": True,
    },
    "chart_exclude_sections": [],
    "is_simple_questionnaire_tree": True,
    "is_single_branch_tree": True,
}
