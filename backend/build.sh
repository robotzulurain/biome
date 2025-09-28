#!/usr/bin/env bash
# build.sh

echo "=== Starting Django Deployment Build ==="

# Install dependencies
echo "1. Installing Python dependencies..."
pip install -r requirements.txt

# Make and run migrations
echo "2. Creating database migrations..."
python manage.py makemigrations || echo "No new migrations needed"

echo "3. Applying database migrations..."
python manage.py migrate

# Collect static files
echo "4. Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser (only if it doesn't exist)
echo "5. Creating admin user..."
python manage.py create_admin_user || echo "Admin user creation failed or already exists"

echo "=== Build completed successfully! ==="
