from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4CSA",
    "intro_text": gettext_lazy(
        "Fit4CSA is a self-assessment tool to streamline the process of applying for a basic-level "
        "cybersecurity certification in the context of the CyberSecurity Act (CSA - EU 2019/881). "
        'Fit4CSA is part of the <a href="https://coral-project.org/" target="_blank">CORAL</a> '
        "EU-funded project."
        "<br><br>"
        "<h4>How does Fit4CSA work?</h4>"
        "<ol>"
        "<li>Select what you would like to assess: an ICT service, an ICT process, "
        "an ICT product - Web application or an ICT generic product.</li>"
        "<li>Depending on your choice, you will need to fill in a questionnaire with both single "
        "choice and multiple choice questions. If you have supporting evidence for each of your "
        "answers (a policy, procedure, etc.), we recommend that you to keep track of this all "
        "throughout the questionnaire in order to establish a mapping of this evidence as you "
        "progress.</li>"
        "<li>At the end of the survey, you will be given a score and a set of recommendations. "
        "Your Scybersecurity maturity can improve if you follow these recommendations.</li>"
        "<li>If you scored at least 85%, Fit4CSA will additionally ask if you want a CSA "
        "conformity self-assessment, or to apply a basic-level certification. In the first case, "
        "you will be able to download the report with your answers and use it as a basis of your "
        "conformity self-assessment. In the second case, you will be asked to register and start "
        "an audit process based on the report issued within Fit4CSA. Keep in mind that all "
        "evidence supporting your answers might be requested later by the auditor of your choice."
        "</li>"
        "</ol>"
        "The first 3 steps of this process are anonymous."
        "<br><br>"
        "If at some point, you wish to continue the survey later, you click on the "
        "<strong>Continue later button</strong> and save the provided link separately. "
        "Using that link, you can pick up where you left off anytime."
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
    "minimal_acceptable_score": 85,
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
        "activity": True,
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
