from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey SME Demand",
    "intro_text": gettext_lazy(
        " Welcome to our survey on the human resources challenges faced by cybersecurity professionals in Luxembourg. The 2023 national ecosystem study on cybersecurity revealed that an overwhelming 82% of market participants identify human resources as a significant obstacle. This encompasses issues such as the location, recruitment, and retention of cybersecurity professionals. Moreover, the study underscores the growing concerns regarding the scarcity of talent and the constraints imposed by remote work, with 77% of respondents expressing worry about each of these factors. "
        " <br /> "
        " <br /> "
        "This questionnaire is intended for cybersecurity professionals " 
        "working in Luxembourg, and the results are anonymous "
	    "with the sole purpose of better understanding the market dynamics.  "
        "Your insights are invaluable in understanding and "
		"addressing these critical challenges. "
        " <br /> "
        " <br /> "
        "The study is the work product of the Data For Research,"
        " Innovation, and Governance (D4RIG) team of"
        " the National Cybersecurity Competence Center"
        " of the Luxembourg House of Cybersecurity."
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
