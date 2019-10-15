FROM python:3

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip3 install -r requirements.txt
COPY . /csskp/

RUN mkdir /tmp/csskp

RUN python3 manage.py compilemessages
