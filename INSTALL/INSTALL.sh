#! /usr/bin/env bash


PYTHON_VERSION='3.10.0'

TOOL_NAME=$TOOL_NAME
TOOL_DESCRIPTION='Description of the tool.'

PROJECT_PATH='/home/ubuntu/Fit4Cybersecurity'
DB_NAME='csskp'
DB_USER='csskp'
DB_PASSWORD="csskp"


echo "--- Updating packages list… ---"
sudo apt-get update
sudo apt-get -y upgrade


echo "--- Installing core dependencies… ---"
sudo apt-get install -y gettext postgresql curl git

sudo apt-get install -y make build-essential libssl-dev libbz2-dev \
    libreadline-dev libsqlite3-dev llvm curl libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev libxml2-dev libxslt-dev libpq-dev python3-openssl

# Pillow prerequisites for Ubuntu 16.04 LTS - 20.04 LTS:
sudo apt-get install -y libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# To install WeasyPrint inside a virtualenv using wheels
sudo apt-get install -y libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0


echo "--- Installation Node… ---"
curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -
sudo apt-get install -y nodejs


echo "--- Installing pyenv… ---"
sudo -u ubuntu curl https://pyenv.run | bash
sudo chown -R ubuntu:ubuntu /home/ubuntu/.pyenv
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
sudo -u ubuntu echo 'export PYENV_ROOT="/home/ubuntu/.pyenv"' >> /home/ubuntu/.profile
sudo -u ubuntu echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/ubuntu/.profile
sudo -u ubuntu echo 'eval "$(pyenv init --path)"' >> /home/ubuntu/.profile
sudo -u ubuntu bash -c 'source /home/ubuntu/.profile'


echo "--- Installing Python $PYTHON_VERSION… ---"
pyenv install $PYTHON_VERSION
pyenv global $PYTHON_VERSION


echo "--- Installing Poetry… ---"
curl -sSL https://install.python-poetry.org | python -
export PATH="/home/ubuntu/.local/bin:$PATH"
echo 'export PATH="/home/ubuntu/.local/bin:$PATH"' >> /home/ubuntu/.bashrc
bash -c 'source /home/ubuntu/.bashrc'


echo "--- Installing $TOOL_NAME… ---"
sudo -u ubuntu git clone https://github.com/CASES-LU/Fit4Cybersecurity.git $PROJECT_PATH
cd $PROJECT_PATH
npm ci
poetry install --no-dev


echo "--- Generation of the $TOOL_NAME configuration file… ---"
sudo -u ubuntu cat > csskp/config.py <<EOF
from django.utils.translation import gettext_lazy
from socket import gethostname, gethostbyname

PUBLIC_URL = ""
ALLOWED_HOSTS = [gethostname(), gethostbyname(gethostname())]
OPERATOR_EMAIL = "info@example.org"

SECRET_KEY = "u__*z&=urjtc0t)b)@5qbt_a#3-354=k9x(j)@eu#h7sb=-66s"

HASH_KEY = b"hDs3HftLkd9OsxI9smHP-TmGv-4z7h-1xaQp0RYuY20="

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "$DB_NAME",
        "USER": "$DB_USER",
        "PASSWORD": "$DB_PASSWORD",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

CUSTOM = {
    # Generic configurations
    "tool_name": "$TOOL_NAME",
    "intro_text": gettext_lazy("$TOOL_DESCRIPTION"),
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
        "introduction": gettext_lazy(
            "The objective of the self-assessment tool, "
            + "%(tool_name)s is to assess the maturity of an organization in terms of "
            + "applicable good practices in the field of information security."
            + "<br /><br />"
            + "This document, based on the %(tool_name)s, is for the exclusive use of "
            + "the customer. It is in this respect confidential."
            + "<br /><br />"
            + "In view of the methodology used and the fact that it is a self-assessment, "
            + "it is understood that the overall results can not in any way be exhaustive. "
            + "As such, the actual risk assessment or the list of identified risks and "
            + "vulnerabilities are based on the information provided by the client. "
            + "The analysis resulting from this assessment can engage only the customer "
            + "for any omission or error that would be due to third parties or not."
            + "<br /><br />"
            + "The tool, %(tool_name)s can possibly provide recommendations. It is "
            + "understood by the client that the recommendations are neither exclusive "
            + "nor exhaustive."
            + "<br /><br />"
            + "It should also be noted that the information you have provided to us will "
            + "be recorded for statistical reasons. "
            + "Due to the nature of the data, we can not identify you. Unless you later "
            + "contact us to do a Diagnostic CASES."
        ),
        "description": gettext_lazy(
            "This self-assessment tool is named %(tool_name)s "
            + "to highlight the introduction to information security. "
            + "It is also a prerequisite for doing a CASES Diagnostic: a minimum score of "
            + "%(minimal_acceptable_score)s/100 is required. "
            + "The purpose for this restriction gives us the opportunity to better "
            + "tailor the recommendations to your organization during the Diagnostic."
            + "<br /><br />"
            + "During this self-assessment multiple choice questions were asked. After "
            + "analyzing your answers, recommendations have been provided."
            + "<br /><br />"
            + "Finally, you can download a report, which will help you to communicate "
            + "the results to your suppliers, if necessary."
        ),
        "results": gettext_lazy(
            "You have achieved %(SCORE)s/100 with your "
            + "answers. You must reach at least %(minimal_acceptable_score)s/100 "
            + "to be able to make a CASES Diagnosis."
            + "<br /><br />"
            + "We remind you that this is a self-assessment and it is important "
            + "to understand that all the results can not in any way be exhaustive."
        ),
    },
    "sectors": [],
    "company_size": [],
    "countries": [],
}

REPORT_TEMPLATE_DIR = "./templates/report/"

EMAIL_HOST = "localhost"
EMAIL_PORT = 25

# Logging mechanism
LOG_DIRECTORY = "./logs"
LOG_FILE = "django.log"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIRECTORY, LOG_FILE),
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

EOF


poetry run python manage.py collectstatic
poetry run python manage.py makemessages -a --keep-pot -e html,txt,py,json
poetry run python manage.py compilemessages


echo "--- Creating database… ---"
sudo -u postgres createuser $DB_USER
sudo -u postgres createdb $DB_NAME
sudo -u postgres psql -c "alter user $DB_USER with encrypted password '$DB_PASSWORD';"
sudo -u postgres psql -c "grant all privileges on database $DB_NAME to $DB_USER;"
poetry run python manage.py migrate


echo "--- Importing data… ---"
poetry run python manage.py import_questions $QUESTIONS_SET
poetry run python manage.py import_questions $CONTEXT_QUESTIONS_SET
