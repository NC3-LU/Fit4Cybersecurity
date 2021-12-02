#!/bin/ash
# wait-for-postgres.sh

shift

until (! command -v psql || PGPASSWORD=password psql -h db -U "postgres" -c '\q' )
do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
poetry run python manage.py compilemessages
poetry run python manage.py migrate
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=password
export DJANGO_SUPERUSER_EMAIL=admin@admin.localhost
poetry run python manage.py createsuperuser --noinput || echo "superuser already created"

poetry run python manage.py import_questions data/$1/questions.json
poetry run python manage.py import_translations data/$1/translations.json

# Can be used one of apache service or python server.
#apache2ctl -D FOREGROUND
poetry run python manage.py runserver 0.0.0.0:8000
