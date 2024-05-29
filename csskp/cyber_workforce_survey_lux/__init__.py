from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Cybersecurity Workforce Survey Luxembourg",
    "intro_text": gettext_lazy(
        " Welcome to the Cybersecurity Workforce Survey, designed for professionals in Luxembourg. This survey is crucial as it builds on the 2023 national ecosystem study, which revealed that 82% of market participants view human resources as a major obstacle, including challenges related to location, recruitment, and retention. "
        " <br /> "
        " <br /> "
        " Furthermore, 77% of respondents expressed concerns about "
        "talent scarcity and the limitations of remote work. " 
        "Your insights are vital for better understanding and addressing "
		"these workforce challenges. "
        " <br /> "
        " <br /> "
        "The survey is anonymous and there are no right or wrong answers. "
		"It is conducted by the National Cybersecurity Competence Center "
		"of the Luxembourg House of Cybersecurity. Your participation will " "help shape effective strategies to enhance the cybersecurity "
		"workforce in Luxembourg."
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
