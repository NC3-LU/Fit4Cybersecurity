# Fit4Cybersecurity

[![Python application basic tests](https://github.com/CASES-LU/Fit4Cybersecurity/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/CASES-LU/Fit4Cybersecurity/actions/workflows/pythonapp.yml)
[![Latest release](https://img.shields.io/github/release/CASES-LU/Fit4Cybersecurity.svg?style=flat-square)](https://github.com/CASES-LU/Fit4Cybersecurity/releases/latest)
[![License](https://img.shields.io/github/license/CASES-LU/Fit4Cybersecurity.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Translation status](https://translate.monarc.lu/widgets/Fit4Cybersecurity/-/fit4cybersecurity/svg-badge.svg)](https://translate.monarc.lu/engage/Fit4Cybersecurity/)


Fit4Cybersecurity is a self-assessment tool by [CASES](https://www.cases.lu)
to help business owners implement a better cybersecurity strategy.

This tool allows instantiation of the following self-assessment websites:

- [Fit4Cybersecurity](https://fit4cybersecurity.cases.lu),
- [Fit4Privacy](https://fit4privacy.cases.lu),
- [Fit4OperatorSurvey](https://fit4operatorsurvey.cases.lu),
- [Cyber4Africa](https://start.cyber4africa.org).


## Deployment

The following instructions are detailed in the
[installation script](INSTALL/INSTALL.sh).

### Requirements

```bash
$ sudo apt install gettext postgresql

$ sudo apt install make build-essential libssl-dev libbz2-dev \
    libreadline-dev libsqlite3-dev curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev libxml2-dev libxslt-dev libpq-dev python3-openssl

# Pillow prerequisites for Ubuntu 16.04 LTS - 20.04 LTS:
$ sudo apt install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# To install WeasyPrint inside a virtualenv using wheels
$ sudo apt install libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```


### Set up your Python environment

```bash
$ curl https://pyenv.run | bash
$ CONFIGURE_OPTS=--enable-shared pyenv install 3.10.0 # install latest stable Python with shared libraries support, only if you want to use mod_wsgi later.
$ pyenv global 3.10.0 # make this version default for the whole system
$ pyenv versions # check
$ curl -sSL https://install.python-poetry.org | python -
```

### Install the application


```bash
$ git clone https://github.com/CASES-LU/Fit4Cybersecurity.git
$ cd Fit4Cybersecurity
$ npm ci
$ poetry install --no-dev
```


### Configure application

Create and configure a file **csskp/config.py** based on **csskp/config_dev.py**.
Settings in the __CUSTOM__ dictionnary will be automatically discovered by the software
and can be used in HTML templates.


```bash
# Configure production settings:
$ cp csskp/config_dev.py csskp/config.py

# Create a virtualenv, collect static files and compile the translations:
$ poetry shell
$ python manage.py collectstatic # Copy static files required by Django Admin
$ python manage.py makemessages -a --keep-pot -e html,txt,py,json  # extract the translations
$ python manage.py compilemessages # Compile the translations

# Initialize the database:
$ sudo -u postgres createdb fit4cybersecurity  # Name of the database as in config.py
$ python manage.py migrate

# Import questions, answers and recommendations:
$ python manage.py import_questions data/fit4cybersecurity/questions.json
# Optionally, import the context questions (will be asked to the user before the survey start):
$ python manage.py import_questions data/fit4cybersecurity/context-questions.json

# Create a user for the admin interface:
$ python manage.py createsuperuser --username <username>
```

In the configuration file ```config.py``` , ensures that __PUBLIC_URL__ and the other
variables are configured for your instance.

You **must really** set **your** secret keys:

Here is an example for the Fernet hash key:

```bash
$ python
Python 3.10.0 (default, Oct  7 2021, 11:22:39) [GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from cryptography.fernet import Fernet
>>> Fernet.generate_key()
b'-MsdIsPZMnJ1eGhtnw0rYR1HH0N1iLxzcTO69ERbik0='
```

For the Django secret key, you can for example use ```from django.utils.crypto import get_random_string```,
at your convenience.


### Run the application

```bash
$ python manage.py runserver # not for production
```

For production you can use [Gunicorn](https://gunicorn.org) (an example file for use
with Nginx is provided in the contrib folder) or mod_wsgi and **turn off** the debug
mode in the configuration file.


### Configuration with Apache and mod_wsgi

```bash
$ sudo apt install apache2 apache2-dev # apxs2
$ wget https://github.com/GrahamDumpleton/mod_wsgi/archive/refs/tags/4.9.0.tar.gz
$ tar -xzvf 4.9.0.tar.gz
$ cd mod_wsgi-4.9.0/
$ ./configure --with-apxs=/usr/bin/apxs2 --with-python=/home/<user>/.pyenv/shims/python
$ make
$ sudo make install
```

Then in ```/etc/apache2/apache2.conf``` add the lines:

```bash
LoadFile /home/<user>/.pyenv/versions/3.10.0/lib/libpython3.10.so
LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
```

Restart Apache:

```bash
sudo systemctl restart apache2.service
```

Create an Apache VirtualHost, then configure HTTPS properly. Below is an
example:

```bash
sudo apt install certbot python3-certbot-apache
sudo certbot certonly --standalone -d fit4cybersecurity.example.org
sudo a2enmod rewrite
sudo systemctl restart apache2.service
```


## Deploy with a Dockerized environment (for development purposes)


- [Get started](https://docs.docker.com/get-started/);
- [Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/)


```bash
$ whitelabel={NameOfWhitelabel} docker-compose up -d
```
{NameOfWhitelabel} - is the launching site name (e.g. fit4cybersecurity).

The server will be listening at http://127.0.0.1:8000.

The login for the Django Admin interface will be *admin* and the password will
be *password*.


## Upgrading the application

```bash
$ cd Fit4Cybersecurity/
$ git pull origin master --tags
$ npm ci
$ poetry install --no-dev
$ poetry run python manage.py collectstatic
$ poetry run python manage.py migrate
$ poetry run python manage.py compilemessages
```

Restart Apache if needed.


## Updating the translations

If you want to update the translations (in the case **you have locally**
changed the source code), you must first run:

```bash
$ python manage.py makemessages -a --keep-pot -e html,txt,py,json # extract the translations
```

Then you can use a tool like
[poedit](https://poedit.net) to translate the strings and you can compile with
the previously mentioned command.

If you want to re-generate the .pot template file:

```bash
$ python manage.py makemessages -a --keep-pot
```

## Templates customization per site.

It is possible to customize specific templates for each available site. 
This can be done by creating a folder with the `site_name` config parameter value
and place it under the same directory as it is located under the original templates.   
The new template will be loaded automatically if exists,can inherit the parent template
and only override its specific blocks.


## Updating the OpenAPI Schema

If you have update the API, you can generate a new OpenAPI Schema:

```bash
$ python manage.py generateschema --file static/survey/api/openapi-schema.yml
```


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)

Copyright (C) 2019-2021 SECURITYMADEIN.LU
