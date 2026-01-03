#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Fix for reused database: fake reset application migrations if needed
# (This ensures we can re-apply them correctly without conflict)
python manage.py migrate --fake application zero || true

# Apply database migrations
python manage.py migrate
