from django.utils.translation import gettext_lazy

CUSTOM = {
    # Generic configurations
    "tool_name": "Fit4OperatorSurvey",
    "intro_text": gettext_lazy(
        "This survey aims to identify the level of maturity "
        + "of the operators in Luxembourg with respect to risk management and governance, "
        + "collaboration on national and EU level and Incident reporting. We collect the "
        + "answers to these 30 questions to understand where guidance and knowledge is "
        + "already advanced and where there is room for improvement. "
        + "As such, it is recommended that a person is taking this survey that is knowing "
        + "the company's maturity on the aforementioned topics well. "
        + "<br /><br />"
        + "The survey will be online and available between December 2021 and March 31st 2022. "
        + "After the survey, the data will be processed and results will be interpreted. "
        + "However, since the survey is completely anonymous, we cannot identify you nor "
        + "your company and thus deletion of specific records is not possible: we cannot "
        + "be sure that it is indeed your survey. The results will be made available "
        + "through another channel."
        + "<br /><br />"
        + "If you are not able to do the survey in one go and you want to later "
        + "pick up where you have left off, please be sure to save the link by clicking "
        + "on the \"continue later\" button. "
        + "We will not be able to help you to find your answers again otherwise."
    ),
    "countries_first": [],
    "defaultLanguage": "en",
    "languages": [
        ("en", "English"),
    ],
    # Logos paths
    "tool_logo": "static/images/logo-fit4operatorsurvey.png",
    "cases_logo": "templates/report/images/cases_logo.svg",
    "secin_logo": "templates/report/images/secin_logo.svg",
    # Minimal score
    "minimal_acceptable_score": 65,
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
        "displayResults": False,
    },
    # Available report parts
    "report": {
        "introduction": True,
        "description": False,
        "results": False,
        "recommendations": True,
        "questions": True,
    },
    "sectors": [
        ("ENER", gettext_lazy("Energy")),
        ("TRAN", gettext_lazy("Transport")),
        ("BANK", gettext_lazy("Banking")),
        ("FINA", gettext_lazy("Financial market infrastructure")),
        ("HEAL", gettext_lazy("Health")),
        ("DRIN", gettext_lazy("Dringking water")),
        ("WWAT", gettext_lazy("Waste Water")),
        ("DIGI", gettext_lazy("Digital Infrastructure and Service Providers")),
        ("PUBL", gettext_lazy("Public Administration")),
        ("SPAC", gettext_lazy("Space")),
        ("POST", gettext_lazy("Postal and Courrier Services")),
        ("WMAN", gettext_lazy("Waste Management")),
        ("CHEM", gettext_lazy("Manufacture, production and distribution of chemicals")),
        ("FOOD", gettext_lazy("Food Production, processing and distribution")),
        ("MEDI", gettext_lazy("Manufacturing of medical devices")),
        ("COMP", gettext_lazy("Manufacture of computer, electronics and optical products")),
        ("ELEC", gettext_lazy("Manufacture of electrical equipment")),
        ("MACH", gettext_lazy("Manufacture of machinery and equipment")),
    ],
    "company_size": [
        ("a", gettext_lazy("Under 10 employees")),
        ("b", gettext_lazy("From 10 to 49 employees")),
        ("c", gettext_lazy("From 50 to 249 employees")),
        ("d", gettext_lazy("Over 250 employees")),
    ],
    "countries": [
        ("LU", "Luxembourg"),
        ("EEA", "EEA"),
        ("NEEA", "Not EEA"),
        ("EU", "Europe"),
    ],
}
