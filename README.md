# DTB — Design. Automate. Breakthrough.

A modern web studio website built with Django, Tailwind CSS, and Resend email service.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Virtual environment

### Local Setup

```bash
# Clone the repository
git clone https://github.com/Sage-Nwanne/DTB.git
cd DTB

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Start development server
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 🚀 Start a Local Server

### Step-by-Step Guide

#### 1. Navigate to Project Root
```bash
cd /path/to/DTB
```
Make sure you're in the root directory where `manage.py` is located.

#### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

#### 3. Install Dependencies (if not already done)
```bash
pip install -r requirements.txt
```

#### 4. Run Database Migrations
```bash
python manage.py migrate
```

#### 5. Start the Development Server
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### 6. Access the Website
Open your browser and visit:
- **Website:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`

### Common Issues & Solutions

**Issue: "No such file or directory: 'manage.py'"**
- **Solution:** Make sure you're in the `/DTB` root directory, not in a subdirectory
- **Check:** Run `ls manage.py` - it should show the file

**Issue: "ModuleNotFoundError: No module named 'django'"**
- **Solution:** Activate virtual environment and install dependencies
- **Run:** `source venv/bin/activate` then `pip install -r requirements.txt`

**Issue: "Port 8000 is already in use"**
- **Solution:** Use a different port
- **Run:** `python manage.py runserver 8001`

**Issue: "Database error" or "no such table"**
- **Solution:** Run migrations
- **Run:** `python manage.py migrate`

### Useful Development Commands

```bash
# Run server on different port
python manage.py runserver 8001

# Run server on all network interfaces
python manage.py runserver 0.0.0.0:8000

# Create a superuser for admin panel
python manage.py createsuperuser

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

### Project Structure Reminder

When running the server, Django uses:
- **`config/settings.py`** - Configuration settings
- **`config/urls.py`** - Main URL routing
- **`main_app/`** - Main application (views, models, templates)
- **`main_app/templates/`** - HTML templates
- **`main_app/static/`** - CSS, JavaScript, images
- **`theme/`** - Tailwind CSS styling

### Stopping the Server

Press `CTRL+C` in your terminal to stop the development server.

### Deactivate Virtual Environment

When you're done developing:
```bash
deactivate
```

## 📁 Project Structure

```
DTB/
├── config/                 # Django settings & configuration
│   ├── settings.py        # Development settings
│   ├── settings_production.py
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI config
│   └── asgi.py            # ASGI config
│
├── main_app/              # Main Django application
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL routing
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   └── email_utils.py     # Email sending (Resend)
│
├── theme/                 # Tailwind CSS theme app
│   ├── static/            # Compiled CSS
│   ├── static_src/        # Source CSS
│   └── templates/         # Theme templates
│
├── docs/                  # Documentation (33 files)
│   ├── DEPLOYMENT.md      # Deployment guide
│   ├── SETUP.md           # Setup instructions
│   ├── RESEND_EMAIL.md    # Email configuration
│   └── ...
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku deployment config
├── build.sh               # Build script
├── db.sqlite3             # SQLite database
└── venv/                  # Virtual environment
```

## 🛠️ Tech Stack

- **Django 5.2** - Web framework
- **Tailwind CSS** - Utility-first CSS
- **Resend** - Email service
- **PostgreSQL** - Production database
- **Heroku** - Deployment platform

## 📧 Email Configuration

The site uses **Resend** for transactional emails:

- **Contact form confirmations** - Sent to users
- **Internal notifications** - Sent to team
- **API Key** - Set via environment variable `RESEND_API_KEY`

See `docs/RESEND_EMAIL.md` for detailed setup.

## 🚀 Deployment

### Heroku Deployment

```bash
# Set environment variables
heroku config:set RESEND_API_KEY=your_api_key

# Deploy
git push heroku main
```

See `docs/DEPLOYMENT.md` for complete instructions.

## 📚 Documentation

All documentation is in the `docs/` folder:

- `docs/DEPLOYMENT.md` - Production deployment
- `docs/SETUP.md` - Local development setup
- `docs/RESEND_EMAIL.md` - Email configuration
- `docs/PROJECT_STRUCTURE_ANALYSIS.md` - Project structure explanation

## 🔧 Development

### Run Development Server
```bash
python manage.py runserver
```

### Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Access Admin Panel
Visit `http://127.0.0.1:8000/admin/`

## 📝 Environment Variables

Create a `.env` file in the root directory:

```
DEBUG=True
SECRET_KEY=your-secret-key
RESEND_API_KEY=your-resend-api-key
DATABASE_URL=postgresql://user:password@localhost/dtb
```

## 🌐 Pages

- **Home** (`/`) - Landing page with services
- **Services** (`/services`) - Service offerings
- **Works** (`/works`) - Portfolio/projects
- **About** (`/about`) - Team and company info
- **Reviews** (`/reviews`) - Client testimonials
- **Contact** (`/contact`) - Contact form with email
- **Admin** (`/admin`) - Django admin panel

## 📧 Contact Form

The contact form:
1. Collects user information
2. Saves to database
3. Sends confirmation email to user (via Resend)
4. Sends internal notification to team
5. Shows success message

## 🔐 Security

- CSRF protection on all forms
- Email validation
- Environment variables for secrets
- Secure password hashing
- SQL injection prevention (Django ORM)

## 📞 Support

For issues or questions:
1. Check `docs/` folder for documentation
2. Review Django documentation: https://docs.djangoproject.com/
3. Check Resend docs: https://resend.com/docs

## 👥 Team

- **Sage Nwanne** - Co-Founder & Lead Developer
- **Shawn Dullen** - Co-Founder & Solutions Architect
- **Adam Mohammed** - Product & UX Design

---

**Ready to get started?** See `docs/SETUP.md` for detailed setup instructions.

