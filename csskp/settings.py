# -*- coding: utf-8 -*-

"""
Django settings for csskp project.
"""

import os
import sys
import importlib
from django.contrib.messages import constants as messages

try:
    from csskp import config
except ImportError:  # pragma: no cover
    from csskp import config_dev as config

try:
    site_config = importlib.import_module("csskp." + config.SITE_NAME + ".site_config")
except ImportError:  # pragma: no cover
    site_config = []

# Initialization of the custom variables (strings, templates, icons, active modules)
CUSTOM = {key: value for key, value in getattr(site_config, "CUSTOM", {}).items()}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Include BOOTSTRAP4_FOLDER in path
BOOTSTRAP4_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "bootstrap4"))
if BOOTSTRAP4_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP4_FOLDER)

MAIN_TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
PARTS_TEMPLATE_DIR = os.path.join(
    BASE_DIR, CUSTOM.get("templates_parts_dir", "templates/parts")
)
SITE_TEMPLATE_DIR = os.path.join(MAIN_TEMPLATE_DIR, config.SITE_NAME)

STATIC_DIR = os.path.join(BASE_DIR, "static")

PICTURE_DIR = "/tmp/csskp/"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

try:
    REPORT_TEMPLATE_DIR = config.REPORT_TEMPLATE_DIR

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config.SECRET_KEY
    HASH_KEY = config.HASH_KEY

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = config.DEBUG
    LOGGING = config.LOGGING
    LOG_DIRECTORY = config.LOG_DIRECTORY

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    DATABASES = config.DATABASES

    ALLOWED_HOSTS = config.ALLOWED_HOSTS
    PUBLIC_URL = config.PUBLIC_URL
    OPERATOR_EMAIL = config.OPERATOR_EMAIL

    EMAIL_HOST = config.EMAIL_HOST
    EMAIL_PORT = config.EMAIL_PORT
except AttributeError as e:
    print("Please check you configuration file for the missing configuration variable:")
    print("  {}".format(e))
    exit(1)

try:
    if LOG_DIRECTORY:
        # if not logging in stdout
        os.makedirs(LOG_DIRECTORY, exist_ok=True)
except Exception as e:
    print("Impossible to create the log directory:")
    print("  {}".format(e))
    exit(1)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "survey",
    "bootstrap4",
    "django_countries",
    "bootstrap_datepicker_plus",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "csskp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            SITE_TEMPLATE_DIR,
            MAIN_TEMPLATE_DIR,
            PARTS_TEMPLATE_DIR,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "survey.context_processors.get_version",
                "survey.context_processors.instance_configurations",
            ],
        },
    },
]

WSGI_APPLICATION = "csskp.wsgi.application"

LOGIN_URL = "/admin/login/"
LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = CUSTOM.get("defaultLanguage", "en")

LANGUAGES = CUSTOM.get("languages", [])
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

STATIC_DIR = os.path.join(BASE_DIR, "static")
PICTURE_DIR = "/tmp/csskp/"

STATICFILES_DIRS = [
    STATIC_DIR,
]

SITE_IMAGES_DIR = os.path.join(STATIC_DIR, "images", config.SITE_NAME)
SITE_IMAGES_URL = STATIC_URL + "images/" + config.SITE_NAME

# Settings for django-bootstrap4
BOOTSTRAP4 = {
    "error_css_class": "bootstrap4-error",
    "required_css_class": "bootstrap4-required",
    "javascript_in_head": True,
    "include_jquery": True,
}

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# First displayed countries on start survey page
COUNTRIES_FIRST = CUSTOM.get("countries_first", [])
COUNTRIES_FIRST_BREAK = "---------------------"


# Default settings
BOOTSTRAP4 = BOOTSTRAP4 = {
    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "/static/npm_components/bootstrap/dist/css/bootstrap.min.css",
        "crossorigin": "anonymous",
    },
    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "/static/npm_components/bootstrap/dist/js/bootstrap.min.js",
        "crossorigin": "anonymous",
    },
    # The complete URL to the Bootstrap CSS file (None means no theme)
    "theme_url": None,
    # The URL to the jQuery JavaScript file (full)
    "jquery_url": {
        "url": "/static/npm_components/jquery/dist/jquery.min.js",
        "crossorigin": "anonymous",
    },
    # The URL to the jQuery JavaScript file (slim)
    "jquery_slim_url": {
        "url": "/static/npm_components/jquery/dist/jquery.slim.min.js",
        "crossorigin": "anonymous",
    },
    # The URL to the Popper.js JavaScript file (slim)
    "popper_url": {
        "url": "/static/npm_components/popper.js/dist/umd/popper.min.js",
        "crossorigin": "anonymous",
    },
    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use
    # bootstrap4.html)
    "javascript_in_head": True,
    # Include jQuery with Bootstrap JavaScript False|falsy|slim|full (default=False)
    # False - means tag bootstrap_javascript use default value - `falsy` and does not
    # include jQuery)
    "include_jquery": True,
    # Label class to use in horizontal forms
    "horizontal_label_class": "col-md-3",
    # Field class to use in horizontal forms
    "horizontal_field_class": "col-md-9",
    # Set placeholder attributes to label if no placeholder is provided
    "set_placeholder": True,
    # Class to indicate required (better to set this in your Django form)
    "required_css_class": "",
    # Class to indicate error (better to set this in your Django form)
    "error_css_class": "is-invalid",
    # Class to indicate success, meaning the field has valid input
    # (better to set this in your Django form)
    "success_css_class": "is-valid",
    # Renderers (only set these if you have studied the source and understand the inner
    # workings)
    "formset_renderers": {
        "default": "bootstrap4.renderers.FormsetRenderer",
    },
    "form_renderers": {
        "default": "bootstrap4.renderers.FormRenderer",
    },
    "field_renderers": {
        "default": "bootstrap4.renderers.FieldRenderer",
        "inline": "bootstrap4.renderers.InlineFieldRenderer",
    },
}
