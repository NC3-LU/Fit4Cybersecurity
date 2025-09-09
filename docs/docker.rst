## Deploy with a Dockerized environment (for development purposes)


- [Get started](https://docs.docker.com/get-started/);
- [Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/)


```bash
$ whitelabel={NameOfWhitelabel} docker compose up -d
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
