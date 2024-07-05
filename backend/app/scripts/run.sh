#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations users
python manage.py makemigrations api
python manage.py migrate --run-syncdb

uwsgi --socket :9000 --workers 2 --master --enable-threads --module config.wsgi