from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4eHealth",
    "intro_text": gettext_lazy("Description of the tool."),
    "countries_first": [],
    "defaultLanguage": "en",
    "languages": [
        ("en", "English"),
        ("fr", "French"),
        ("lb", "Luxembourgish"),
        ("de", "German"),
    ],
    # Logos paths
    "cases_logo": "templates/report/images/cases_logo.svg",
    "secin_logo": "templates/report/images/secin_logo.svg",
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
    "chart_exclude_sections": ["eSanté"],
}
