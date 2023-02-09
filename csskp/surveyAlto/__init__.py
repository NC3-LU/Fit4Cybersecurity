from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey ALTO",
    "intro_text": gettext_lazy(
        "Les PME ne disposent souvent pas de l'expertise nécessaire en interne afin de gérer les données personnelles conformément au RGPD. Elles sont désavantagées par rapport aux grandes structures en termes de coûts, d'impact, notamment. De plus, elles sont peu nombreuses à avoir développé des stratégies ou des « réflexes de responsable de traitement ». Ces constats sont dus à un manque de connaissance et de sensibilisation, d'une part, et à un manque d'informations et d'outils pratiques, d'autre part. Par conséquent, il est nécessaire de renforcer la sensibilisation des PME à l'importance de la protection des données à caractère personnel et de les accompagner pour améliorer leur mise en conformité au RGPD." 
        "<br><br>"
        "Le projet ALTO a pour objectif de mettre en œuvre un outil d'auto-évaluation afin de répondre aux défis quotidiens des PME en matière de protection des données."
        "<br><br>"
        "Le présent questionnaire <strong><ins>strictement anonyme</ins></strong> est adressé aux PME pour cerner les défis en matière de protection des données auxquels sont confrontées les PME, afin de créer et mettre à leur disposition un outil d'auto-évaluation répondant à leurs besoins."
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
        ("fr", "French"),
    ],
    # Logos paths
    "right_cover_logo": "templates/report/images/nc3_logo.svg",
    "left_cover_logo": "templates/report/images/lhc_logo.svg",
    # Custom CSS:
    "survey_css": "survey/css/style.css",
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
        "requestDiagnostic": True,
        "requestTraining": True,
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
        "size": True,
        "country": True,
        "status": True,
        "language": True,
        "section": True,
        "category": True,
    },
    "chart_exclude_sections": [],
    "is_simple_questionnaire_tree": True,
    "is_single_branch_tree": True,
}
