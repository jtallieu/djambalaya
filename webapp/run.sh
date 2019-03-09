#!/bin/bash
export DBNAME=${EEN_PG_DBNAME}

#until PGPASSWORD=$EEN_PG_PASSWORD psql -h "$EEN_PG_HOST" -U "$EEN_PG_USER" -d "$DBNAME" -c '\q'; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done

cd /usr/src/app
exec python manage.py runserver 0.0.0.0:8080