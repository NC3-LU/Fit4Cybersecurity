from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4CSA",
    "intro_text": gettext_lazy(
        "You might want to assess either an ICT service, an ICT process, an ICT Web application or an ICT generic product."
        "<br><br>"
        "Depending on your choice from these 4 options, the tool will present to you a questionnaire with several multiple choice questions. Sometimes you can select one single answer, sometimes multiple answers are possible."
        "<br><br>"
        "Please take your time and respond truthfully, knowing that your self-assessment is key to correctly quantify the maturity of your service, process, application or generic product."
        "<br><br>"
        "Depending on your answers, after the survey you will be offered a set of recommendations, as well as a report that can serve as a conformity self-assessment. If the overall score is good enough (85% correct answers), you will be able to use the report as the basic documentation of a CSA-basic level certification conducted separately by an external auditor. If your score is lower, you can improve your cybersecurity maturity by implementing the given recommendations."
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
    "languages": [("en", "English")],
    # Logos paths
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/style.css",
    # Minimal score
    "minimal_acceptable_score": 0,
    # Show or not the questions number left to complete the survey.
    "show_progress_questions_numbers": True,
    # Custom parts of templates
    #   main dir for PARTS_TEMPLATE_DIR:
    "templates_parts_dir": "templates/parts",
    "templates_parts": {
        # path of the templates parts
        "terms": "terms_part.html",
        "footer": "fit4csa/footer_part.html",
        "main_logo": "fit4csa/logo_part.html",
    },
    # Available modules
    "modules": {
        "reportDownload": True,
        "reportEmail": False,
        "requestDiagnostic": True,
        "requestTraining": False,
        "displayResults": True,
        "audit": True,
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
        "activity": False,
        "sector": False,
        "size": False,
        "country": False,
        "status": True,
        "language": False,
        "section": False,
        "category": False,
    },
    "chart_exclude_sections": ["Select survey"],
    "is_simple_questionnaire_tree": True,
}
