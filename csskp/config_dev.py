from django.utils.translation import gettext_lazy

ALLOWED_HOSTS = []

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
    "tool_name": "<TOOL_NAME>",
    "intro_text": gettext_lazy("Description from a string or a file."),
    "logoFull": gettext_lazy("/static/images/logoFull-en.png"),
    "countries_first": [],
    "languages": ["en", "fr", "de"],

    "templates_parts": {
        "terms": "parts/terms.html",
        "footer": "parts/footer.html",
        "main_logo": "parts/logo.html",
    }
}

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
