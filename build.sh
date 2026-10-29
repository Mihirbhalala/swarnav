#!/usr/bin/env bash
# Render build script: installs dependencies, collects static files,
# migrates the database and bootstraps first-run data.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Load the tour packages only into an empty database, so admin edits are never overwritten
python manage.py seed_data --if-empty

# Create the admin account on first deploy when DJANGO_SUPERUSER_USERNAME,
# DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD are set (skipped if it already exists)
if [[ -n "${DJANGO_SUPERUSER_USERNAME:-}" && -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]]; then
    python manage.py createsuperuser --noinput || echo "Superuser already exists, skipping."
fi
