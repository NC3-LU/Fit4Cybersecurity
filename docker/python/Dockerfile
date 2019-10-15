# when building remember to add --build-arg user=<<USER>>

FROM python:3

ARG user

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev postgresql-client-common postgresql-client

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
RUN useradd -ms /bin/bash $user
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip3 install -r requirements.txt
COPY . /csskp/

<<<<<<< HEAD
RUN chown -R $user:$user /csskp
USER $user
RUN mkdir /tmp/csskp
=======
RUN mkdir /tmp/csskp

>>>>>>> 2470ca4f1cb88c85b47a93423089d06af24b47cf
RUN python3 manage.py compilemessages
