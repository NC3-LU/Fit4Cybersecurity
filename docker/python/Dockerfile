# when building remember to add --build-arg user=<<USER>>

FROM python:3

ARG user=james-bond

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
RUN useradd -ms /bin/bash $user
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip3 install -r requirements.txt
COPY . /csskp/

RUN chown -R $user:$user /csskp
USER $user
RUN mkdir /tmp/csskp
RUN python3 manage.py compilemessages
