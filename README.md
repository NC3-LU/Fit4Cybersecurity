# Fit4Privacy

Fit4Privacy is a self-assessment tool by [CASES](https://www.cases.lu)
to help business owners implement a better data protection and privacy approach.

## Deployment

### Requirements

```bash
$ sudo apt install gettext postgresql
```


### Set up your Python environment

```bash
$ pyenv install 3.9.2 # install Python
$ pyenv global 3.9.2 # make this version default for the whole system
$ pyenv versions # check
```

### Install the application


```bash
$ git clone https://github.com/CASES-LU/fit4cybersecurity.git ./fit4privacy
$ cd fit4privacy/
$ git checkout fit4privacy
$ npm install
$ poetry install
```


### Configure and run the application

```bash
$ cp csskp/config_dev.py csskp/config_prod.py # configure production settings
$ poetry shell
$ python manage.py collectstatic # copy static files required by Django Admin
$ python manage.py compilemessages # compile the translations
$ python manage.py migrate # need to initialize before create the first user
$ python manage.py createsuperuser --username <username>
```

Run the application:

```bash
$ python manage.py runserver # not for production
```

For production you can use [Gunicorn](https://gunicorn.org) or mod_wsgi.



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
$ cd fit4privacy/
$ git pull origin master
$ poetry run python manage.py migrate
$ poetry run python manage.py compilemessages
```

If you want to update the translations, you must first run:

```bash
$ python manage.py makemessages -a --keep-pot # extract the translations
```

Then you can use a tool like
[poedit](https://poedit.net) to translate the strings and you can compile with
the previously mentioned command.



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)

Copyright (C) 2019-2021 SECURITYMADEIN.LU
