SHELL := /bin/bash

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default."
	@echo "Try 'make help'"

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	poetry install

activate:
	poetry shell

run:
	python manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

populate:
	python manage.py import_questions $(path)/questions.json

droptestdb:
	dropdb fit4cybersecurity1 ; createdb fit4cybersecurity1

inittestdb: droptestdb migrate populate
	@echo "Done"

superuser:
	python manage.py createsuperuser

generateschema:
	python manage.py generateschema --file $(schemapath)

generatepot:
	python manage.py makemessages -a --keep-pot

update:
	npm ci
	poetry install --no-dev
	python manage.py collectstatic
	python manage.py compilemessages
	python manage.py migrate

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
