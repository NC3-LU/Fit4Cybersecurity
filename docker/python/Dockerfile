FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y

# Uncomment in case of usage apache server configuration.
#RUN apt-get install -y curl apache2 apache2-utils libapache2-mod-wsgi-py3
RUN apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client nodejs npm

WORKDIR /csskp
COPY ./poetry.lock ./pyproject.toml /csskp/
COPY ./package.json ./package-lock.json /csskp/
COPY . /csskp/
RUN mkdir /tmp/csskp

RUN npm install

RUN pip install "poetry"
RUN poetry install

RUN poetry run python manage.py compilemessages

# Uncomment in case of usage apache server configuration.
#RUN echo "ServerName fit4cybersecurity.docker" >> /etc/apache2/apache2.conf
#ADD ./docker/python/apache/fit4cybersecurity.conf /etc/apache2/sites-available/000-default.conf
#RUN virtual_env=$(cd /csskp && poetry --venv); sed -i -r "s|VIRTUAL_ENV|$virtual_env|g" "/etc/apache2/sites-available/000-default.conf"
#RUN chmod 777 -R /root
