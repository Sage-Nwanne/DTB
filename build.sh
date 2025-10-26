#!/bin/bash
# Build script for Heroku deployment
# This script builds Tailwind CSS and collects static files

set -e

echo "Building Tailwind CSS..."
cd theme/static_src
npm install
npm run build
cd ../..

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete!"

