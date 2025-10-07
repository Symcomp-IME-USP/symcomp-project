#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Waiting for database to be ready..."
python wait-for-db.py

# Apply database migrations (NOT RECOMMENDED TO PUT THE MAKEMIGRATIONS HERE)
# But haven't found any other workaround
echo "Creating and applying database migrations..."
python manage.py makemigrations
python manage.py migrate

if [ "$DJANGO_ENV" = "production" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

# Then exec the container's main process (what's set as CMD in the Dockerfile,
# or passed to the 'command' instruction in docker-compose.yml).
exec "$@"
