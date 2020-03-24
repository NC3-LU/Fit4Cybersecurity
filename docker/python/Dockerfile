FROM python:3.8-alpine

RUN apk update && \
  apk add \
  build-base \
  curl \
  git \
  python-dev \
  gettext \
  freetype-dev \
  libffi-dev \
  openssl-dev \
  libxml2-dev \
  libxslt-dev \
  libpq \
  postgresql-client \
  postgresql-dev \
  npm

WORKDIR csskp

COPY csskp csskp/
COPY locale locale/
COPY static static/
COPY stats stats/
COPY survey survey/
COPY templates templates/
COPY utils utils/
COPY wtemps wtemps/
COPY README.md .
COPY manage.py .
COPY package.json .
COPY package-lock.json .
COPY pyproject.toml .
COPY poetry.lock .
COPY wait-for-postgres.sh .
RUN mkdir /tmp/csskp

RUN chmod +x ./wait-for-postgres.sh


RUN pip install poetry
RUN poetry install
RUN poetry run python manage.py compilemessages
