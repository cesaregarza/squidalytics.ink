#!/bin/bash

# Set your variables
REPO_URL="https://github.com/cesaregarza/squidalytics.ink.git"
TEMP_CLONE_DIR="/tmp/squidalytics_clone"
DJANGO_PROJECT_DIR="/home/cegarza/squidalytics"

# Backup the .env file
cp "$DJANGO_PROJECT_DIR/squidalytics/.env" /tmp/squidalytics_env_backup

# Clone the repository to a temporary location
git clone "$REPO_URL" "$TEMP_CLONE_DIR"

# Copy only the child directory containing the Django project to the actual Django project directory
rsync -av --delete --exclude=".env" "$TEMP_CLONE_DIR/squidalytics/" "$DJANGO_PROJECT_DIR/"

# Remove the temporary clone
rm -rf "$TEMP_CLONE_DIR"

# Restore the .env file
cp /tmp/squidalytics_env_backup "$DJANGO_PROJECT_DIR/squidalytics/.env"

# Make any migrations
cd "$DJANGO_PROJECT_DIR/"
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput

# Reload the web application
touch /var/www/squidalytics_ink_wsgi.py
