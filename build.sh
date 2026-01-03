#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Run post-deploy setup (Create Superuser, Fix Site ID, Default Google App)
python render_setup.py
