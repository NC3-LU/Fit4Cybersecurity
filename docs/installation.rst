Installation
============

Prerequisites
-------------

Generally speaking, requirements are the following:

- A GNU/Linux distribution (tested on Debian and Ubuntu);
- Python: version >= 3.8 (preferably use `pyenv <https://github.com/pyenv/pyenv>`_)
  and a dependency manager (for example `Poetry <https://python-poetry.org>`_);
- A PostgreSQL server >= 12.x: persistent storage.



Deployment
----------

The service can be deployed via several ways:

.. contents::
    :local:
    :depth: 1


From the source
~~~~~~~~~~~~~~~

The following instructions are detailed in the
`installation script <INSTALL/INSTALL.sh>`_.


System requirements
```````````````````

.. code-block:: bash

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


Set up your Python environment
``````````````````````````````

.. code-block:: bash

    $ curl https://pyenv.run | bash
    $ CONFIGURE_OPTS=--enable-shared pyenv install 3.10.0 # install latest stable Python with shared libraries support, only if you want to use mod_wsgi later.
    $ pyenv global 3.10.0 # make this version default for the whole system
    $ pyenv versions # check
    $ curl -sSL https://install.python-poetry.org | python -


Install the application
```````````````````````

.. code-block:: bash

    $ git clone https://github.com/NC3-LU/Fit4Cybersecurity.git
    $ cd Fit4Cybersecurity
    $ npm ci
    $ poetry install --only main


Configure the application
`````````````````````````

Create and configure a file **csskp/config.py** based on **csskp/config_dev.py**.
Settings in the __CUSTOM__ dictionnary will be automatically discovered by the software
and can be used in HTML templates.


.. code-block:: bash

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


In the configuration file ```config.py``` , ensures that __PUBLIC_URL__ and the other
variables are configured for your instance.

You **must really** set **your** secret keys:

Here is an example for the Fernet hash key:

.. code-block:: bash

    $ python
    Python 3.10.0 (default, Oct  7 2021, 11:22:39) [GCC 10.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from cryptography.fernet import Fernet
    >>> Fernet.generate_key()
    b'-MsdIsPZMnJ1eGhtnw0rYR1HH0N1iLxzcTO69ERbik0='


For the Django secret key, you can for example use ```from django.utils.crypto import get_random_string```,
at your convenience.


Run the application
```````````````````

.. code-block:: bash

    $ python manage.py runserver


For production you can use [Gunicorn](https://gunicorn.org) (an example file for use
with Nginx is provided in the contrib folder) or mod_wsgi and **turn off** the debug
mode in the configuration file.


Configuration with Apache and mod_wsgi
``````````````````````````````````````

.. code-block:: bash

    $ sudo apt install apache2 apache2-dev # apxs2
    $ wget https://github.com/GrahamDumpleton/mod_wsgi/archive/refs/tags/4.9.4.tar.gz
    $ tar -xzvf 4.9.4.tar.gz
    $ cd mod_wsgi-4.9.4/
    $ ./configure --with-apxs=/usr/bin/apxs2 --with-python=/home/<user>/.pyenv/shims/python
    $ make
    $ sudo make install


Then in ```/etc/apache2/apache2.conf``` add the lines:

.. code-block:: bash

    LoadFile /home/<user>/.pyenv/versions/3.10.0/lib/libpython3.10.so
    LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so


Restart Apache:

.. code-block:: bash

    sudo systemctl restart apache2.service


Create an Apache VirtualHost, then configure HTTPS properly. Below is an
example:

.. code-block:: bash

    sudo apt install certbot python3-certbot-apache
    sudo certbot certonly --standalone -d fit4cybersecurity.example.org
    sudo a2enmod rewrite
    sudo systemctl restart apache2.service






Docker
~~~~~~


.. code-block:: bash

    $ whitelabel={NameOfWhitelabel} docker-compose up -d

{NameOfWhitelabel} - is the launching site name (e.g. fit4cybersecurity).

The server will be listening at http://127.0.0.1:8000.

The login for the Django Admin interface will be *admin* and the password will
be *password*.
