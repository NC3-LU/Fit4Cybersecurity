from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey SME Demand",
    "intro_text": gettext_lazy(
        "This questionnaire is intended for managers of small"
        " and medium-sized businesses, between 1 and 250"
        " employees, and must be completed by them in order"
        " to share their vision of their needs in terms of"
        " cybersecurity services and solutions. The objective"
        " is to better understand market practices,"
        " expectations and trends in order to identify the"
        " levers of demand for this type of player in"
        " Luxembourg. Our desire is not to audit companies"
        " individually, this questionnaire is anonymous,"
        " but to understand how the managers of SMEs position"
        " themselves in the face of the regulatory,"
        " technological and human challenges of cybersecurity."
        " <br>"
        " <br>"
        "The study is the work product of the Data For Research,"
        " Innovation, and Governance (D4RIG) team of"
        " the National Cybersecurity Competence Center (NC3)"
        " of the Luxembourg House of Cybersecurity. This is"
        " carried out as part of the research activities"
        " supporting the creation of the Cybersecurity Market"
        " Intelligence Observatory Platform (CSMIOP)."
        " This purposeful work has also engaged local partners"
        " such as chambers and professional organizations, as"
        " well as all the institutional players in the market"
        " who can support and disseminate this questionnaire"
        " as well as the results of the study."
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
