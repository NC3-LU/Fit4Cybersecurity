#! /usr/bin/env bash


PYTHON_VERSION='3.10.0'

TOOL_NAME='Fit4Cybersecurity'
TOOL_DESCRIPTION='Description of the tool.'

SERVICE_HOST='0.0.0.0'
SERVICE_PORT='5005'
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
git clone https://github.com/CASES-LU/Fit4Cybersecurity.git
cd Fit4Cybersecurity/
npm ci
poetry install --no-dev


echo "--- Generation of the $TOOL_NAME configuration file… ---"
sudo -u ubuntu cat > csskp/config.py <<EOF
from django.utils.translation import gettext_lazy

PUBLIC_URL = ""
ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]
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

EOF


poetry run python manage.py collectstatic
poetry run python manage.py compilemessages


echo "--- Creating database… ---"
sudo -u postgres createuser $DB_USER
sudo -u postgres createdb $DB_NAME
sudo -u postgres psql -c "alter user $DB_USER with encrypted password '$DB_PASSWORD';"
sudo -u postgres psql -c "grant all privileges on database $DB_NAME to $DB_USER;"
echo "--- Initializaing database… ---"
poetry run python manage.py migrate


echo "--- Importing data… ---"
poetry run python manage.py import_questions data/fit4Cybersecurity/questions.json
