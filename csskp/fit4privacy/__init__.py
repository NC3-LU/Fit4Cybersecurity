from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4Privacy",
    "intro_text": gettext_lazy(
        "This questionnaire, created in consultation with "
        + '<a href="https://cnpd.public.lu/en.html" target="_blank">CNPD</a>, '
        + "aims to help organisations assess to what extent they are in control of their personal "
        + "data risks. First, Fit4Privacy asks questions to understand the amount of personal "
        + "data processing already in place, then its questions examine the response of the "
        + "organisation towards GDPR obligations. Based on the identified scope, the tool offers "
        + "a set of recommendations that could be consolidated into the first steps towards "
        + "implementing privacy and data protection. Note that this is a self-assessment tool "
        + "and as such cannot provide definitive guidelines. Yet, Fit4Privacy is raising "
        + "awareness around key topics such as personal data processing, data lifecycle "
        + "management, and basic data protection obligations for which organisations should "
        + "already be prepared as of 2021."
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
    "chart_exclude_sections": [],
}
