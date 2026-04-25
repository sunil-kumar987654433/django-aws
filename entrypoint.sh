#!/bin/sh


echo "Applying migrations..."
python manage.py makemigrations --noinput


echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
    