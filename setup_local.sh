#!/bin/bash

# DTB Website - Local Development Setup Script
# This script automates the local development environment setup

echo "🚀 DTB Website - Local Development Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    
    # Generate a secret key
    SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
    
    # Update .env with generated secret key
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/your-secret-key-here-generate-a-new-one/$SECRET_KEY/" .env
    else
        sed -i "s/your-secret-key-here-generate-a-new-one/$SECRET_KEY/" .env
    fi
    
    echo "✅ .env file created with generated SECRET_KEY"
else
    echo "ℹ️  .env file already exists, skipping..."
fi

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser prompt
echo ""
echo "👤 Would you like to create a superuser account? (y/n)"
read -r create_superuser

if [[ "$create_superuser" == "y" || "$create_superuser" == "Y" ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎉 Your development environment is ready!"
echo ""
echo "To start the development server:"
echo "  1. Activate virtual environment:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "     venv\\Scripts\\activate"
else
    echo "     source venv/bin/activate"
fi
echo "  2. Run the server:"
echo "     python manage.py runserver"
echo ""
echo "  3. Visit: http://127.0.0.1:8000/"
echo "  4. Admin panel: http://127.0.0.1:8000/admin/"
echo ""
echo "Happy coding! 💻"

