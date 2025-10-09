# DTB Website - DesignedToBreakthrough

A Django-based portfolio and project management website for the DesignedToBreakthrough team.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Local Development Setup](#local-development-setup)
- [Deployment Guide](#deployment-guide)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## ✨ Features

- **Portfolio Showcase**: Display team projects and work
- **Developer Profiles**: Individual developer profiles with certificates and resumes
- **Project Management**: Assign projects to developers and track progress
- **User Authentication**: Custom authentication system for developers and customers
- **Responsive Design**: Mobile-friendly interface
- **Admin Dashboard**: Django admin interface for content management

## 🛠 Tech Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite (development) / PostgreSQL (production recommended)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Pillow
- **Static Files**: WhiteNoise (production)
- **Server**: Gunicorn (production)

## 🚀 Local Development Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd DTB-site
```

### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or if using Pipenv:
```bash
cd ../  # Go to DTB-website directory
pipenv install
pipenv shell
cd DTB_website
```

### Step 4: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 6: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the site!

### Step 8: Access the Admin Panel

Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## 📁 Project Structure

```
DTB-site/
├── config/                       # Django project settings
│   ├── settings.py               # Development settings
│   ├── settings_production.py    # Production settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── main_app/                     # Main application
│   ├── models.py                 # Database models (Project, Profile)
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL patterns
│   ├── admin.py                  # Admin configuration
│   ├── auth_backends.py          # Custom authentication
│   ├── templates/                # HTML templates
│   └── static/                   # CSS, JS, Images
├── media/                        # User uploaded files
├── staticfiles/                  # Collected static files
├── certificates/                 # Certificate uploads
├── profile_pictures/             # Profile picture uploads
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── Procfile                      # Railway/Heroku config
├── railway.json                  # Railway configuration
├── runtime.txt                   # Python version
├── setup_local.sh                # Automated setup script
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── venv/                         # Virtual environment (not in git)
└── README.md                     # This file
```

## 🌐 Deployment Guide

### Preparing for Production

1. **Generate a New Secret Key**

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

2. **Create Environment File**

```bash
cp .env.example .env
```

Edit `.env` and add:
- Your generated secret key
- Your domain name
- Any other environment-specific settings

3. **Install Production Dependencies**

```bash
pip install -r requirements.txt
```

4. **Collect Static Files**

```bash
python manage.py collectstatic --settings=config.settings_production
```

5. **Run Migrations**

```bash
python manage.py migrate --settings=config.settings_production
```

### Deployment Options

#### Option 1: Traditional VPS (DigitalOcean, Linode, AWS EC2)

See [DEPLOYMENT_VPS.md](DEPLOYMENT_VPS.md) for detailed instructions.

#### Option 2: Platform as a Service (Heroku, Railway, Render)

See [DEPLOYMENT_PAAS.md](DEPLOYMENT_PAAS.md) for detailed instructions.

#### Option 3: Squarespace Domain with External Hosting

See [DEPLOYMENT_SQUARESPACE.md](DEPLOYMENT_SQUARESPACE.md) for detailed instructions on connecting your Squarespace domain.

### Security Checklist

- [ ] Change `SECRET_KEY` in production
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use HTTPS (SSL certificate)
- [ ] Set up proper database backups
- [ ] Review and update developer credentials in `auth_backends.py`
- [ ] Enable firewall on your server
- [ ] Set up monitoring and logging

## 🔐 Developer Authentication

The site includes a custom authentication backend for developers with predefined credentials.

**Default developer accounts** (defined in `main_app/auth_backends.py`):
- Username: `dev1`, Password: `dtbDev1!`
- Username: `dev2`, Password: `dtbDev2!`
- Username: `dev3`, Password: `dtbDev3!`

⚠️ **IMPORTANT**: Change these credentials before deploying to production!

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📝 License

[Add your license here]

## 📧 Contact

For questions or support, contact the DesignedToBreakthrough team.

---

**Built with ❤️ by the DTB Team**

