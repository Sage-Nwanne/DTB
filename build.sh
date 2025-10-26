#!/bin/bash
# Build script for Heroku deployment
# This script builds Tailwind CSS and collects static files

set -e

echo "Building Tailwind CSS..."
cd theme/static_src
npm install
npm run build
cd ../..

echo "Verifying CSS file exists..."
ls -lh theme/static/css/dist/styles.css

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Checking collected static files..."
ls -lh staticfiles/css/dist/ 2>/dev/null || echo "CSS not found in staticfiles!"

echo "Build complete!"

