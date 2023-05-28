#!/bin/bash
echo "Valid webhook received. Updating site..."

# Set your variables
REPO_URL="https://github.com/cesaregarza/squidalytics.ink.git"
TEMP_CLONE_DIR="/tmp/squidalytics_clone"
DJANGO_PROJECT_DIR="/home/cegarza/squidalytics"
MEDIA_DIR="$DJANGO_PROJECT_DIR/media"

# Backup the .env file
echo "Backing up .env file..."
cp "$DJANGO_PROJECT_DIR/squidalytics/.env" /tmp/squidalytics_env_backup

# Clone the repository to a temporary location
echo "Cloning repository to temporary location..."
git clone "$REPO_URL" "$TEMP_CLONE_DIR"

# Copy only the child directory containing the Django project to the actual Django project directory
echo "Copying files to actual Django project directory, ignoring media files..."
rsync -av --delete --exclude=".env" --exclude=$MEDIA_DIR "$TEMP_CLONE_DIR/squidalytics/" "$DJANGO_PROJECT_DIR/"

# Remove the temporary clone
echo "Removing temporary clone..."
rm -rf "$TEMP_CLONE_DIR"

# Restore the .env file
echo "Restoring .env file..."
cp /tmp/squidalytics_env_backup "$DJANGO_PROJECT_DIR/squidalytics/.env"

# Make any migrations
echo "Making migrations..."
cd "$DJANGO_PROJECT_DIR/"
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Reload the web application
echo "Reloading web application..."
touch /var/www/squidalytics_ink_wsgi.py

echo "Site updated successfully."
