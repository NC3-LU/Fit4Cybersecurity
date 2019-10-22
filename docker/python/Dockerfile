FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y curl apache2 apache2-utils libapache2-mod-wsgi-py3 \
    && apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

RUN pip install pipenv

WORKDIR /csskp
COPY ./Pipfile* /app/
COPY . /csskp/
RUN mkdir /tmp/csskp
RUN pipenv install
RUN pipenv run python manage.py compilemessages

RUN echo "ServerName fit4cybersecurity.docker" >> /etc/apache2/apache2.conf

ADD ./docker/python/apache/fit4cybersecurity.conf /etc/apache2/sites-available/000-default.conf

RUN virtual_env=$(cd /csskp && pipenv --venv); sed -i -r "s|VIRTUAL_ENV|$virtual_env|g" "/etc/apache2/sites-available/000-default.conf"
RUN chmod 777 -R /root
