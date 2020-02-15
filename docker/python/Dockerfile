FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# Uncomment in case of usage apache server configuration.
#RUN apt-get install -y curl apache2 apache2-utils libapache2-mod-wsgi-py3
RUN apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /csskp
COPY ./Pipfile* /app/
COPY . /csskp/
RUN mkdir /tmp/csskp
RUN poetry install

RUN sed -i -r 's/#STATIC_ROOT/STATIC_ROOT/g' "/csskp/csskp/settings.py"
RUN poetry run python manage.py collectstatic --noinput
RUN sed -i -r 's/STATIC_ROOT/#STATIC_ROOT/g' "/csskp/csskp/settings.py"

RUN poetry run python manage.py compilemessages

# Uncomment in case of usage apache server configuration.
#RUN echo "ServerName fit4cybersecurity.docker" >> /etc/apache2/apache2.conf
#ADD ./docker/python/apache/fit4cybersecurity.conf /etc/apache2/sites-available/000-default.conf
#RUN virtual_env=$(cd /csskp && poetry --venv); sed -i -r "s|VIRTUAL_ENV|$virtual_env|g" "/etc/apache2/sites-available/000-default.conf"
#RUN chmod 777 -R /root
