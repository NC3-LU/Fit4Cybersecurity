from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Cybersecurity Providers’ Survey",
    "intro_text": gettext_lazy(
        "<b>This survey is directed to providers of cybersecurity services and solutions in Luxembourg</b>. Your participation is important to help us understand the current state of the market in relation to the needs of businesses and organizations."
        "<br /><br />"
        "After a comprehensive survey on the cybersecurity needs of SMEs conducted earlier this year, the National Cybersecurity Competence Center (NC3) has now launched a survey in regards <b>to cybersecurity services and solutions offered by providers in Luxembourg</b>. Through this research the connection between cybersecurity providers and businesses in need of cybersecurity solutions should be made easier and clearer."
        "<br /><br />"
        "This survey is part of the market intelligence observatory of the National Cybersecurity Competence Center (NC3). The NC3 is a department of the LHC and supported by the Ministry of the Economy. The observatory collects and analyzes data on the cybersecurity market in Luxembourg, in order to inform policy decisions and support the development of the ecosystem. "
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
        "footer": "footer_part.html",
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
        "sector": False,
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
