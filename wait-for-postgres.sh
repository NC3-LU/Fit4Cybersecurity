#!/bin/sh
# wait-for-postgres.sh

set -e

shift

until (! command -v psql || PGPASSWORD=postgres psql -h db -U "postgres" -c '\q' )
do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
pipenv run python manage.py migrate
