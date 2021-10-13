# Fit4Cybersecurity -  Fitcyber4Africa

[![Translation status](https://translate.monarc.lu/widgets/Fit4Cybersecurity/-/fitcyber4africa/svg-badge.svg)](https://translate.monarc.lu/engage/Fit4Cybersecurity/)


Fitcyber4Africa is a self-assessment tool by [CASES](https://www.cases.lu)
to help business owners from Africa implement a better cybersecurity strategy.

The official instance is available [here](https://start.cyber4africa.org).


## Deployment

### Requirements

```bash
$ sudo apt install gettext postgresql
$ sudo apt install make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev libxml2-dev libxslt-dev libpq-dev python3-openssl
$ curl https://pyenv.run | bash
```


### Set up your Python environment

```bash
$ CONFIGURE_OPTS=--enable-shared pyenv install 3.10.0 # install latest stable Python with shared libraries support, only if you want to use mod_wsgi later.
$ pyenv global 3.10.0 # make this version default for the whole system
$ pyenv versions # check
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```


### Install the application

```bash
$ git clone https://github.com/CASES-LU/Fit4Cybersecurity.git Fitcyber4Africa
$ cd  Fitcyber4Africa/
$ git checkout fitcyber4africa
$ npm ci
$ poetry install --no-dev
```


### Configure the application

```bash
$ cp csskp/config_dev.py csskp/config_prod.py # configure production settings
$ poetry shell
$ python manage.py collectstatic # copy static files required by Django Admin
$ python manage.py compilemessages # compile the translations
$ python manage.py migrate # need to initialize before create the first user
$ python manage.py createsuperuser --username <username>
```

In the configuration file ```config_prod.py``` you **must** set **your** secret
keys:

Here is an example for the Fernet hash key:

```bash
$ python
Python 3.10.0 (default, Oct  7 2021, 11:22:39) [GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from cryptography.fernet import Fernet
>>> Fernet.generate_key()
b'-MsdIsPZMnJ1eGhtnw0rYR1HH0N1iLxzcTO69ERbik0='
```

For the Django secret key, you can for example use ```from django.utils.crypto import get_random_string```, at your convenience.


### Run the application

```bash
$ python manage.py runserver # not for production
```

For production you can use [Gunicorn](https://gunicorn.org) or mod_wsgi and turn
off the debug mode in the configuration file.


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
sudo certbot --standalone -d start.cyber4africa.org
sudo a2enmod rewrite
sudo systemctl restart apache2.service
```


## Deploy with a Dockerized environment (for development purposes)


- [Get started](https://docs.docker.com/get-started/);
- [Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/)


```bash
$ docker-compose up -d
```

The server will be listening at http://127.0.0.1:8000.

The login for the Django Admin interface will be *admin* and the password will
be *password*.



## Upgrading the application

```bash
$ cd Fitcyber4Africa/
$ git pull origin fitcyber4africa --tags
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
$ python manage.py makemessages -a --keep-pot # extract the translations
```

Then you can use a tool like
[poedit](https://poedit.net) to translate the strings and you can compile with
the previously mentioned command.

If you want to re-generate the .pot template file:

```bash
$ python manage.py makemessages --keep-pot
```


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)

Copyright (C) 2019-2021 SECURITYMADEIN.LU
