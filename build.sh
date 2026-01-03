#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# FORCE FIX: Delete the migration record so Django re-runs it
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute(\"DELETE FROM django_migrations WHERE app='application';\");" || true

# Apply database migrations
python manage.py migrate
python manage.py migrate
