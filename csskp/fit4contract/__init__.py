from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4Contract",
    "intro_text": gettext_lazy(
        "This questionnaire aims to identify the general scope of the contractual "
        "relationship considered, in order to set up an acquisition, a lease, "
        "a development or any other service in the field of information and communication "
        "technologies. Based on this scope, Fit4Contract provides a list of basic "
        "information security requirements that are recommended to be considered in "
        "establishing the contractual relationship. This is a self assessment tool and "
        "as such cannot provide definitive guidelines. This tool is simply raising "
        "awareness for Information Security in ICT product and service contracts. "
        "Additionally, many countries have their own legal requirements for contracts "
        "and thus, we do not take any responsibilities concerning the answers and we "
        "clarify that the user of this survey needs to verify, and adapt their "
        "contracts accordingly, to comply with all national and international laws."
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
        "footer": "fit4contract/footer_part.html",
        "main_logo": "logo_part.html",
        "privacy": "privacy_policy_part.html",
    },
    # Available modules
    "modules": {
        "displayProgressBar": True,
        "reportDownload": True,
        "reportEmail": False,
        "requestDiagnostic": False,
        "requestTraining": False,
        "displayResults": False,
    },
    # Available report parts
    "report": {
        "introduction": True,
        "description": True,
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
        "language": True,
        "section": False,
        "category": False,
        "current_question": True,
    },
    "chart_exclude_sections": [],
}
