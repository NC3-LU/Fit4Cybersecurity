FROM ubuntu:focal
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install wget python3-dev git python3-venv python3-pip npm
RUN pip3 install poetry

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

EXPOSE 8000
CMD ["./wait-for-postgres.sh", "db"]
