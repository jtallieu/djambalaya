#!/bin/bash

set -e
export DBNAME=${PG_DBNAME}

until PGPASSWORD=$EEN_PG_PASSWORD psql -h "$PG_HOST" -U "$PG_USER" -d "$DBNAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate