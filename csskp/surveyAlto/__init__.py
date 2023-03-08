from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Survey ALTO",
    "intro_text": gettext_lazy(
        "Gérer les données personnelles conformément au Règlement Général relatif à la Protection des Données (ci-après le « <strong>RGPD</strong> ») peut constituer un défi pour les petites et moyennes entreprises (ci-après les « <strong>PME</strong> »), qui sont souvent désavantagées par rapport aux grandes structures en termes de coûts et d'impact, notamment. De plus, le développement de stratégies de gestion de données ou de « réflexes de responsable de traitement » sont rarement en tête des priorités – les éventuels manques de connaissance et de sensibilisation, d'une part, et d'informations et d'outils pratiques, d'autre part pourraient constituer les causes présumées. En tout état de cause, il est nécessaire de renforcer la sensibilisation des PME à l'importance de la protection des données à caractère personnel et de les accompagner pour améliorer leur mise en conformité au RGPD" 
        "<br><br>"
        "Le projet ALTO, né d'un partenariat entre la Commission nationale pour la protection des données (ci-après « <strong>CNPD</strong> ») et la Luxembourg House of Cybersecurity, National Cybersecurity Competence Center (ci-après le « <strong>LHC-NC3</strong> »), a pour objectif de mettre en œuvre un outil d'auto-évaluation afin de répondre aux défis quotidiens des PME en matière de protection des données."
        "<br><br>"
        "Le présent questionnaire, qui se veut anonyme, a pour but de cerner les obstacles/problèmes/questions en matière de protection des données auxquels sont confrontés les PME, afin de créer et mettre à leur disposition un outil d'auto-évaluation répondant à leurs besoins."
        "<br><br>"
        "Pour en savoir plus sur le projet ALTO, nous vous invitons à vous rendre sur <a href=https://cnpd.public.lu target=_blank rel=noopener noreferrer>la page internet dédiée.</a>"
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
        # ("en", "English"),
        ("fr", "French"),
        # ("de", "German"),
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
        "footer": "surveyAlto/footer_part.html",
        "main_logo": "surveyAlto/logo_part.html",
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
        "sector": False,
        "size": False,
        "country": False,
        "status": True,
        "language": False,
        "section": False,
        "category": False,
    },
    "chart_exclude_sections": [],
    "is_simple_questionnaire_tree": True,
    "is_single_branch_tree": True,
}