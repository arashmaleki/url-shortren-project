#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py create_superuser

gunicorn --bind :5000 url_shortener.wsgi:application
