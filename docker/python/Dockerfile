FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

RUN pip install pipenv

WORKDIR /csskp
COPY ./Pipfile* /app/
COPY . /csskp/
RUN mkdir /tmp/csskp
RUN pipenv install
RUN pipenv run python manage.py compilemessages
