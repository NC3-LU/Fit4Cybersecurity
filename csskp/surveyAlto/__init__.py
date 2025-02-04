from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "DAAZ",
    "intro_text": gettext_lazy(
        "Managing personal data in accordance with the General Data Protection Regulation "
        '(hereinafter "<strong>GDPR</strong>") can be a challenge for small and medium-sized '
        'enterprises (hereinafter "<strong>SMEs</strong>"), which are often at a disadvantage '
        "compared to large structures in terms of costs and impact, in particular. Moreover, "
        'the development of data management strategies or "data controller reflexes" are rarely '
        "at the top of the agenda - the possible lack of knowledge and awareness, "
        "on the one hand, and information and practical tools , "
        "on the other hand could constitute the presumed causes. "
        "In any case, it is necessary to raise awareness among SMEs of the importance of "
        "protecting personal data and to support them in "
        "improving their compliance with the GDPR."
        "<br><br>"
        "The ALTO project, born of a partnership between the National Commission for "
        "Data Protection (<i>Commission Nationale pour la Protection des Données</i> "
        '- "<strong>CNPD</strong>") and the Luxembourg House of CyberSecurity, '
        "National CyberSecurity Competence Center "
        '(hereafter "<strong>LHC-NC3</strong>"), has aims to implement a self-assessment tool '
        "to meet the daily challenges of SMEs in terms of data protection."
        "<br><br>"
        "This questionnaire, which is intended to be anonymous, aims to identify "
        "the data protection obstacles/problems/questions faced by SMEs, "
        "in order to create and make available to them a self-assessment tool "
        "that meets their needs."
        "<br><br>"
        "To find out more about the ALTO project, we invite you to visit "
        "<a href=https://cnpd.public.lu/en/professionnels/outils-conformite/projet-alto.html "
        "target=_blank rel=noopener noreferrer>the dedicated web page.</a>"
    ),
    "countries_first": [
        "LU",
        "BE",
        "FR",
        "DE",
        "NL",
        "GB",
    ],
    "defaultLanguage": "fr",
    "languages": [
        ("en", "English"),
        ("fr", "French"),
        ("de", "German"),
    ],
    # Logos paths
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/surveyAlto/style.css",
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
        "footer": "surveyAlto/footer_part.html",
        "main_logo": "surveyAlto/logo_part.html",
        "privacy": "surveyAlto/privacy_policy_part.html",
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
