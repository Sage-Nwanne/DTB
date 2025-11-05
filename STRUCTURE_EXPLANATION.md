# 📚 Project Structure Explanation

## 🎯 Overview

Your DTB project is a **Django web application** with the following structure:

```
DTB/                          ← Project root
├── config/                   ← Django configuration
├── main_app/                 ← Main application
├── theme/                    ← Tailwind CSS theme
├── docs/                     ← Documentation
└── [other files]             ← Project files
```

---

## 📂 Directory Breakdown

### `config/` - Django Configuration
**Purpose:** Django project settings and URL routing

**Files:**
- `settings.py` - Development settings
- `settings_production.py` - Production settings
- `urls.py` - Main URL routing (maps URLs to views)
- `wsgi.py` - Web Server Gateway Interface (for production)
- `asgi.py` - Asynchronous Server Gateway Interface

**What it does:**
- Configures database connection
- Sets up installed apps
- Manages static files
- Handles security settings
- Routes all URLs to the right views

---

### `main_app/` - Main Django Application
**Purpose:** Core application logic (pages, forms, database)

**Key subdirectories:**
- `migrations/` - Database schema changes
- `static/` - CSS, JavaScript, images
- `templates/` - HTML files for pages

**Key files:**
- `models.py` - Database models (ContactSubmission, etc.)
- `views.py` - View functions (what happens when user visits a page)
- `urls.py` - App-specific URL routing
- `forms.py` - Django forms (contact form, etc.)
- `admin.py` - Django admin configuration
- `email_utils.py` - Email sending logic (Resend)

**What it does:**
- Handles all web pages (home, about, contact, etc.)
- Manages database records
- Processes form submissions
- Sends emails
- Renders HTML templates

---

### `theme/` - Tailwind CSS Theme
**Purpose:** Styling and CSS framework

**Subdirectories:**
- `static/` - Compiled CSS files
- `static_src/` - Source CSS files
- `templates/` - Theme templates

**What it does:**
- Provides Tailwind CSS styling
- Manages color scheme and design system
- Compiles CSS for production

---

### `docs/` - Documentation
**Purpose:** Guides and reference materials

**Contains 33 files including:**
- `DEPLOYMENT.md` - How to deploy to production
- `SETUP.md` - How to set up locally
- `RESEND_EMAIL.md` - Email configuration
- `PROJECT_STRUCTURE.md` - Project structure details
- And 29 more reference documents

**What it does:**
- Provides setup instructions
- Explains deployment process
- Documents email configuration
- Provides quick references

---

## 🔄 How It All Works Together

### When You Visit a Page

```
1. User visits: https://dtbsolutions.tech/contact
   ↓
2. Django receives request in config/urls.py
   ↓
3. URL pattern matches and routes to main_app/urls.py
   ↓
4. main_app/views.py handles the request
   ↓
5. View renders template from main_app/templates/
   ↓
6. HTML is sent back to user's browser
   ↓
7. Browser loads CSS from theme/static/
   ↓
8. User sees the page!
```

### When User Submits Contact Form

```
1. User fills out form and clicks submit
   ↓
2. Form data sent to main_app/views.py
   ↓
3. main_app/forms.py validates the data
   ↓
4. main_app/models.py saves to database
   ↓
5. main_app/email_utils.py sends emails via Resend
   ↓
6. Success message shown to user
```

---

## 📁 File Organization

### Root Level Files
```
README.md                      ← Project overview
requirements.txt               ← Python dependencies
manage.py                      ← Django management tool
Procfile                       ← Heroku deployment config
build.sh                       ← Build script
setup_local.sh                 ← Local setup script
db.sqlite3                     ← SQLite database
```

### Why This Structure?

✅ **Separation of Concerns** - Each folder has a specific purpose
✅ **Django Convention** - Follows Django best practices
✅ **Scalability** - Easy to add new apps if needed
✅ **Maintainability** - Clear where to find things
✅ **Collaboration** - Team members understand structure

---

## 🚀 Common Tasks & Where to Find Them

| Task | Location |
|------|----------|
| Add a new page | `main_app/views.py` + `main_app/templates/` |
| Change styling | `theme/static_src/` or `main_app/static/` |
| Modify database | `main_app/models.py` |
| Update contact form | `main_app/forms.py` |
| Change email logic | `main_app/email_utils.py` |
| Add new URL | `main_app/urls.py` |
| Configure Django | `config/settings.py` |
| Deploy to production | See `docs/DEPLOYMENT.md` |
| Set up locally | See `docs/SETUP.md` |

---

## 🔐 Important Files

### `config/settings.py`
- Database configuration
- Installed apps
- Email settings
- Security settings
- Static files configuration

### `main_app/models.py`
- Database schema
- Data validation
- Business logic

### `main_app/views.py`
- Page logic
- Form handling
- Email sending

### `main_app/templates/`
- HTML pages
- User interface

---

## 📊 App vs Project

**Project** (`config/`)
- Contains settings for entire application
- Manages URL routing
- Configures Django

**App** (`main_app/`)
- Contains specific functionality
- Has models, views, templates
- Can be reused in other projects

**Analogy:**
- Project = Restaurant
- App = Kitchen (handles food preparation)

---

## 🎯 Key Concepts

### Models
Database tables and data structure
```python
# Example: ContactSubmission model
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
```

### Views
Functions that handle requests and return responses
```python
# Example: contact view
def contact(request):
    if request.method == 'POST':
        # Handle form submission
    return render(request, 'contact.html')
```

### Templates
HTML files that display data
```html
<!-- Example: contact.html -->
<form method="POST">
    <input type="text" name="name">
    <textarea name="message"></textarea>
    <button type="submit">Send</button>
</form>
```

### URLs
Map web addresses to views
```python
# Example: urls.py
urlpatterns = [
    path('contact', views.contact, name='contact'),
]
```

---

## ✅ Structure Checklist

- ✅ `config/` - Django settings
- ✅ `main_app/` - Main application
- ✅ `theme/` - Styling
- ✅ `docs/` - Documentation
- ✅ `manage.py` - Django management
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Overview

---

## 🚀 Next Steps

1. **Understand the structure** - You're reading this! ✅
2. **Read README.md** - Project overview
3. **Check docs/SETUP.md** - Local development setup
4. **Explore main_app/** - See how pages are built
5. **Start developing** - Make changes!

---

**Your project is now properly organized and documented! 🎉**

