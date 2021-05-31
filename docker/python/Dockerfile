FROM python:3.9-alpine

RUN apk update && \
  apk add \
  build-base \
  cargo \
  curl \
  freetype-dev \
  fribidi-dev \
  gcc \
  gettext \
  git \
  harfbuzz-dev \
  lcms2-dev \
  libffi-dev \
  libjpeg-turbo-dev \
  libpng-dev \
  libpq \
  libressl-dev \
  libwebp-dev \
  libxml2-dev \
  libxslt-dev \
  musl-dev \
  npm \
  openssl-dev \
  postgresql-client \
  postgresql-dev \
  python3-dev \
  tcl-dev \
  tk-dev \
  zlib \
  rust

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

RUN mkdir node_modules
RUN npm install
RUN mkdir -p static/npm_components
RUN cp -R node_modules/* static/npm_components/

RUN pip install poetry
RUN poetry install
