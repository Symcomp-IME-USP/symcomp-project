#!/bin/bash
set -e

echo "Automatically generating migrations..."
python manage.py makemigrations --noinput

echo "Applying migrations to test database..."
python manage.py migrate --noinput

echo "Testing..."
pytest "$@"

echo "Finishing tests and terminating container"