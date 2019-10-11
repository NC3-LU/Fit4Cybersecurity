FROM python:3

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_9.x | bash - \
  && apt-get install -y nodejs \
  && curl -L https://www.npmjs.com/install.sh | sh

RUN apt-get install -y gettext

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip install -r requirements.txt
COPY . /csskp/

RUN npm install \
    && python manage.py compilemessages \
    && python manage.py makemessages
