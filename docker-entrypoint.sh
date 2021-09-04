#!/usr/bin/env bash

echo -e "Wait for database\n"
POSTGRES_TCP=$(echo "$DATABASE_URL" | sed 's/^postgres/tcp/')
dockerize -wait "$POSTGRES_TCP" -timeout 20s

if [[ "$1" = "test" ]]; then
    echo -e "Running tests\n"
    ./manage.py test
else
    echo -e "Collecting static assets\n"
    ./manage.py collectstatic --noinput --verbosity 0

    echo -e "Migrating database\n"
    ./manage.py migrate

    echo -e "Starting server\n"
    gunicorn configuration.wsgi
fi
