FROM python:3.10.2-buster

RUN apt-get update && \
  apt-get install -y \
  build-essential \
  npm \
  cargo \
  curl \
  freetype2-doc \
  libfribidi-dev \
  gcc \
  gettext \
  git \
  libharfbuzz-dev \
  liblcms2-utils \
  libffi-dev \
  libjpeg62-turbo \
  libpng-dev \
  libpq-dev \
  libssl-dev \
  libwebp-dev \
  libxml2-dev \
  libxslt-dev \
  musl-dev \
  postgresql-client \
  postgresql \
  openssl \
  python3-dev \
  tcl-dev \
  tk-dev \
  zlib1g-dev \
  rustc


WORKDIR csskp

COPY csskp csskp/
COPY locale locale/
COPY static static/
COPY stats stats/
COPY survey survey/
COPY templates templates/
COPY utils utils/
COPY README.md .
COPY manage.py .
COPY package.json .
COPY package-lock.json .
COPY pyproject.toml .
COPY poetry.lock .
COPY wait-for-postgres.sh .
RUN mkdir /tmp/csskp

RUN chmod +x ./wait-for-postgres.sh

RUN mkdir node_modules
RUN npm install
RUN mkdir -p static/npm_components
RUN cp -R node_modules/* static/npm_components/
RUN cp csskp/config_dev.py csskp/config.py

RUN pip install poetry
RUN poetry install
