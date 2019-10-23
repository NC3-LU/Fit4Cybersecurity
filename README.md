# Fit4Cybersecurity

Fit4Cybersecurity is a self-assessment tool by [CASES](https://www.cases.lu)
to help business owners implement a better cybersecurity strategy.

The official CASES instance is available [here](https://startup.cases.lu).


## Deploy with a Dockerized environment (for development purposes)

### Install Docker

- [Get started](https://docs.docker.com/get-started/);
- [Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/)


### Start the containers


```bash
$ docker-compose build
$ docker-compose up -d
```

The server will be listening at http://127.0.0.1:8000.


## Deploy manually

### Requirements

```bash
$ sudo apt install gettext postgresql
```


### Set up your Python environment

Before to begin you will need to install
[pipenv](https://github.com/pypa/pipenv).  
A convenient way to do so is to first install
[pyenv](https://github.com/pyenv/pyenv). With pyenv you will be able
to easily manage Python versions on your system and to install the latest
version of Python:

```bash
$ pyenv install 3.8.0 # install Python
$ pyenv global 3.8.0 # make this version default for the whole system
$ pyenv versions # check
```

Then install
[pipx](https://github.com/pipxproject/pipx).  
And finally install pipenv with pipx.

Later on, this Python environment can be used on production with for
example WSGI.


### Install the application


```bash
$ git clone https://github.com/CASES-LU/Fit4Cybersecurity.git
$ cd Fit4Cybersecurity/
$ npm install
$ pipenv install
```


### Configure and run the application

```bash
$ cp csskp/config_dev.py csskp/config_prod.py # configure production settings
$ pipenv shell
$ python manage.py collectstatic # copy static files required by Django Admin
$ python manage.py compilemessages # compile the translations
$ python manage.py createsuperuser --username <username>
```

Run the application:

```bash
$ python manage.py runserver # not for production
```

For production you can use mod_wsgi.

## Upgrading the application

### Updating the models

```bash
$ cd Fit4Cybersecurity/
$ git pull origin master
$ pipenv shell
$ python manage.py migrate
```


### Internationalization

Simply compile the new translations:

```bash
$ python manage.py compilemessages
```

If you want to update the translations, you must first run:

```bash
$ python manage.py makemessages # extract the translations
```

Then you can use a tool like
[poedit](https://poedit.net) to translate the strings and you can compile with
the previously mentioned command.



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)

* Copyright (C) 2019 SMILE gie securitymadein.lu
