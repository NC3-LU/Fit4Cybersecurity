from django.utils.translation import gettext_lazy

PUBLIC_URL = ""
ALLOWED_HOSTS = ["127.0.0.1", locals().get("PUBLIC_URL", "")]
OPERATOR_EMAIL = "info@example.org"

SECRET_KEY = "u__*z&=urjtc0t)b)@5qbt_a#3-354=k9x(j)@eu#h7sb=-66s"

HASH_KEY = b"hDs3HftLkd9OsxI9smHP-TmGv-4z7h-1xaQp0RYuY20="

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": 5432,
    }
}

CUSTOM = {
    # Generic configurations
    "tool_name": "<TOOL_NAME>",
    "intro_text": gettext_lazy("Description of the tool."),
    "countries_first": [],
    "defaultLanguage": "en",
    "languages": [
        ("en", "English"),
        ("fr", "French"),
        ("de", "German"),
    ],
    # Logos paths
    "tool_logo": "static/images/logoFull-en.png",
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
    "report_texts": {
        "introduction": gettext_lazy("""The objective of the self-assessment tool,
            %(tool_name)s is to assess the maturity of an organization in terms of
            applicable good practices in the field of information security.
            <br /><br />
            This document, based on the %(tool_name)s, is for the exclusive use of
            the customer. It is in this respect confidential.
            <br /><br />
            In view of the methodology used and the fact that it is a self-assessment,
            it is understood that the overall results can not in any way be exhaustive.
            As such, the actual risk assessment or the list of identified risks and
            vulnerabilities are based on the information provided by the client.
            The analysis resulting from this assessment can engage only the customer
            for any omission or error that would be due to third parties or not.
            <br /><br />
            The tool, %(tool_name)s can possibly provide recommendations. It is
            understood by the client that the recommendations are neither exclusive
            nor exhaustive.
            <br /><br />
            It should also be noted that the information you have provided to us will
            be recorded for statistical reasons.
            Due to the nature of the data, we can not identify you. Unless you later
            contact us to do a Diagnostic CASES."""),
        "description": gettext_lazy("""This self-assessment tool is named %(tool_name)s
            to highlight the introduction to information security.
            It is also a prerequisite for doing a CASES Diagnostic: a minimum score of
            %(minimal_acceptable_score)s/100 is required.
            The purpose for this restriction gives us the opportunity to better
            tailor the recommendations to your organization during the Diagnostic.
            <br /><br />
            During this self-assessment multiple choice questions were asked. After
            analyzing your answers, recommendations have been provided.
            <br /><br />
            Finally, you can download a report, which will help you to communicate
            the results to your suppliers, if necessary."""),
        "results": gettext_lazy("""You have achieved %(SCORE)s/100 with your
            answers. You must reach at least %(minimal_acceptable_score)s/100
            to be able to make a CASES Diagnosis.
            <br /><br />
            We remind you that this is a self-assessment and it is important
            to understand that all the results can not in any way be exhaustive."""),
    },
    "sectors": [],
    "company_size": [],
    "countries": [],
}

REPORT_TEMPLATE_DIR = "./templates/report/"

EMAIL_HOST = "localhost"
EMAIL_PORT = 25

# Logging mechanism
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
