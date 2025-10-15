from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey PQCReadiness",
    "intro_text": gettext_lazy(
        "Post-Quantum Cryptography (PQC) readiness refers to the practice of "
        "preparing computer systems, networks, and sensitive information "
        "for protection against future threats posed by quantum computing."
        " Advances in quantum technologies are expected to break widely"
        " used cryptographic algorithms such as RSA and ECC,"
        " creating potential vulnerabilities across digital infrastructures."
        " This makes PQC readiness essential for businesses of all sizes,"
        " since even small organizations could face risks with serious financial,"
        " reputational, and regulatory consequences."
        "<strong> By proactively planning the transition"
        " to quantum-safe cryptographic solutions,"
        " SMEs can safeguard their digital assets, ensure long-term resilience, "
        " and maintain the trust of their customers and partners. </strong> "
        " <br /> "
        " <br /> "
        "This questionnaire is intended for <strong> all businesses,"
        " </strong> to capture their perspective on PQC readiness and quantum-safe"
        "  security solutions."
        " Our objective is not to audit companies individually — <strong> "
        " this questionnaire is anonymous </strong> — but to evaluate the overall "
        " ecosystem’s readiness and awareness regarding the importance of initiating"
        " early considerations for PQC. <br /> "
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
        "displayReview": False,
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
