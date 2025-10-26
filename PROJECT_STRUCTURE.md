# 📁 DTB Website - Project Structure Guide

## 🎯 New Clean Structure

Your project has been **restructured** for clarity and simplicity!

### **Before** (Confusing):
```
DTB-site/
└── DTB-website/
    └── DTB_website/
        └── DTB_website/    ← Three levels deep! 😵
```

### **After** (Clean):
```
DTB-site/                   ← You are here!
├── config/                 ← Django settings
├── main_app/               ← Your app
└── manage.py               ← Django commands
```

Much better! 🎉

---

## 📂 Complete Directory Structure

```
DTB-site/                           # Project root
│
├── 📁 config/                      # Django project configuration
│   ├── __init__.py
│   ├── settings.py                 # Development settings
│   ├── settings_production.py      # Production settings
│   ├── urls.py                     # Main URL routing
│   ├── wsgi.py                     # WSGI server config
│   └── asgi.py                     # ASGI server config
│
├── 📁 main_app/                    # Main Django application
│   ├── __init__.py
│   ├── models.py                   # Database models (Project, Profile)
│   ├── views.py                    # View functions (home, about, etc.)
│   ├── urls.py                     # App URL patterns
│   ├── admin.py                    # Admin panel configuration
│   ├── auth_backends.py            # Custom authentication
│   ├── apps.py                     # App configuration
│   ├── tests.py                    # Unit tests
│   │
│   ├── 📁 templates/               # HTML templates
│   │   ├── base.html               # Base template
│   │   ├── home.html               # Homepage
│   │   ├── about.html              # About page
│   │   ├── works.html              # Portfolio page
│   │   ├── contact.html            # Contact page
│   │   ├── reviews.html            # Reviews page
│   │   ├── devs.html               # Developers page
│   │   ├── profile.html            # User profile
│   │   ├── your-profile.html       # Public profile view
│   │   └── 📁 registration/        # Auth templates
│   │       ├── login.html
│   │       └── signup.html
│   │
│   ├── 📁 static/                  # Static files
│   │   ├── 📁 css/                 # Stylesheets
│   │   │   └── base.css
│   │   └── 📁 Images/              # Images
│   │       └── DTB_logo.png
│   │
│   └── 📁 migrations/              # Database migrations
│       ├── __init__.py
│       ├── 0001_initial.py
│       └── 0002_...py
│
├── 📁 media/                       # User uploaded files (production)
│   ├── 📁 certificates/            # Certificate uploads
│   ├── 📁 profile_pictures/        # Profile pictures
│   ├── 📁 project_images/          # Project images
│   └── 📁 resumes/                 # Resume uploads
│
├── 📁 staticfiles/                 # Collected static files (production)
│   └── (auto-generated)
│
├── 📁 certificates/                # Development certificate uploads
├── 📁 profile_pictures/            # Development profile pictures
│
├── 📁 venv/                        # Virtual environment (not in git)
│   ├── bin/
│   ├── lib/
│   └── ...
│
├── 📄 manage.py                    # Django management commands
├── 📄 requirements.txt             # Python dependencies
├── 📄 Procfile                     # Railway/Heroku process file
├── 📄 railway.json                 # Railway configuration
├── 📄 runtime.txt                  # Python version specification
├── 📄 setup_local.sh               # Automated local setup script
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore                   # Git ignore rules
├── 📄 db.sqlite3                   # SQLite database (development)
│
└── 📚 Documentation/
    ├── README.md                   # Main documentation
    ├── START_HERE.md               # Quick start guide
    ├── QUICK_START.md              # Quick reference
    ├── PROJECT_STRUCTURE.md        # This file
    ├── DEPLOYMENT_SQUARESPACE.md   # Domain connection guide
    ├── DEPLOYMENT_PAAS.md          # Railway/Render deployment
    ├── DEPLOYMENT_VPS.md           # VPS deployment
    ├── DEPLOYMENT_SUMMARY.md       # Complete overview
    └── CLEANUP_VERIFICATION.md     # Cleanup details
```

---

## 🗂️ Key Directories Explained

### **`config/`** - Django Project Settings
- **What it is**: Core Django configuration
- **Old name**: `DTB_website/`
- **Contains**: Settings, URLs, WSGI/ASGI configs
- **You'll edit**: Rarely (mostly done)

### **`main_app/`** - Your Main Application
- **What it is**: All your website functionality
- **Contains**: Models, views, templates, static files
- **You'll edit**: Often (add features, update content)

### **`media/`** - User Uploads (Production)
- **What it is**: Files uploaded by users
- **Contains**: Certificates, profile pictures, resumes
- **Auto-created**: When users upload files

### **`staticfiles/`** - Collected Static Files
- **What it is**: All CSS/JS/images in one place
- **Created by**: `python manage.py collectstatic`
- **Used in**: Production only

### **`venv/`** - Virtual Environment
- **What it is**: Isolated Python environment
- **Contains**: Django and all dependencies
- **Not in git**: Too large, recreate with `python3 -m venv venv`

---

## 🎯 Where Am I? Quick Reference

### **Working Directory Cheat Sheet**

```bash
# You should be here for most commands:
/home/sage_nwanne/code/projects/DTB-site

# Check where you are:
pwd

# Should output:
/home/sage_nwanne/code/projects/DTB-site
```

### **Common Commands from Root**

```bash
# Activate virtual environment
source venv/bin/activate

# Run development server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

---

## 📝 File Naming Convention

### **What Changed**

| Old Reference | New Reference |
|---------------|---------------|
| `DTB_website.settings` | `config.settings` |
| `DTB_website.urls` | `config.urls` |
| `DTB_website.wsgi` | `config.wsgi` |
| `DTB_website.settings_production` | `config.settings_production` |

### **Environment Variables**

**Old**:
```bash
DJANGO_SETTINGS_MODULE=DTB_website.settings_production
```

**New**:
```bash
DJANGO_SETTINGS_MODULE=config.settings_production
```

---

## 🚀 Quick Start Commands

### **Local Development**

```bash
# From anywhere, navigate to project root
cd /home/sage_nwanne/code/projects/DTB-site

# Automated setup
./setup_local.sh

# OR manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### **Deployment**

```bash
# From project root
cd /home/sage_nwanne/code/projects/DTB-site

# Push to GitHub
git add .
git commit -m "Your message"
git push origin main

# Railway will auto-deploy!
```

---

## 🔍 Finding Files

### **"Where is the settings file?"**
```
config/settings.py              # Development
config/settings_production.py   # Production
```

### **"Where are the HTML templates?"**
```
main_app/templates/
```

### **"Where is the CSS?"**
```
main_app/static/css/
```

### **"Where are the models?"**
```
main_app/models.py
```

### **"Where are the views?"**
```
main_app/views.py
```

### **"Where is the URL routing?"**
```
config/urls.py          # Main routing
main_app/urls.py        # App-specific routing
```

---

## ✅ Benefits of New Structure

1. **Clearer**: No more nested `DTB_website/DTB_website/DTB_website`
2. **Simpler**: Easier to navigate
3. **Standard**: Follows Django best practices
4. **Intuitive**: `config/` clearly indicates settings
5. **Less Confusing**: You always know where you are

---

## 🎓 Understanding Django Structure

```
DTB-site/                   # Project root (your workspace)
├── config/                 # Project-level settings (one per project)
└── main_app/               # Application (can have multiple apps)
```

**Think of it like:**
- **Project** = Your entire website
- **Config** = Website-wide settings
- **App** = A specific feature/section (you have one main app)

---

## 📚 Next Steps

1. **Familiarize yourself** with the new structure
2. **Update your mental model**: Root is now `DTB-site/`
3. **Use the guides**: They're all updated with new paths
4. **Deploy to Railway**: Everything is ready!

---

## 🆘 Common Questions

**Q: Where do I run commands?**  
A: From `/home/sage_nwanne/code/projects/DTB-site`

**Q: What happened to DTB_website?**  
A: Renamed to `config/` for clarity

**Q: Do I need to change my code?**  
A: No! All references are already updated

**Q: Will this work with Railway?**  
A: Yes! All deployment files are updated

**Q: Can I still use the old guides?**  
A: The guides are updated with new paths

---

**Your project is now cleaner and easier to navigate! 🎉**

