FROM python:3

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip install -r requirements.txt
COPY . /csskp/

RUN python manage.py compilemessages
