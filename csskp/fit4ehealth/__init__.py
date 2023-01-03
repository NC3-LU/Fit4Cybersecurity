from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4eHealth",
    "intro_text": gettext_lazy(
        "The objective of the self-assessment tool, is to measure the maturity of an organization "
        "in terms of applicable good practices in the field of information security.<br /> "
        "This document, as the outcome of the self-assessment, is for the exclusive use of "
        "the user. It is in this respect confidential.<br /> Given the methodology used and "
        "the fact that it is a self-assessment, the overall results cannot be exhaustive in any "
        "way.<br /> As such, the actual risk assessment or the list of identified risks and "
        "vulnerabilities is therefore based on the information provided by the user.<br /> "
        "The tool may provide recommendations, but the user must be aware that these are neither "
        "exclusive nor exhaustive.<br /> It should also be noted that the information you have "
        "provided to us is recorded for statistical reasons.<br /> Due to the nature of the data, "
        "we cannot identify you, the self-assessment is performed anonymously."
    ),
    "countries_first": [],
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
    "minimal_acceptable_score": 75,
    # Show or not the questions number left to complete the survey.
    "show_progress_questions_numbers": True,
    # Custom parts of templates
    #   main dir for PARTS_TEMPLATE_DIR:
    "templates_parts_dir": "templates/parts",
    "templates_parts": {
        # path of the templates parts
        "terms": "terms_part.html",
        "footer": "fit4ehealth/footer_part.html",
        "main_logo": "logo_part.html",
    },
    # Available modules
    "modules": {
        "reportDownload": True,
        "reportEmail": False,
        "requestDiagnostic": True,
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
        "size": False,
        "country": True,
        "status": True,
        "language": True,
        "section": True,
        "category": True,
    },
    "chart_exclude_sections": ["eSanté"],
}
