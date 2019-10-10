FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /csskp
WORKDIR /csskp
COPY requirements.txt /csskp/
RUN pip install -r requirements.txt
COPY . /csskp/
