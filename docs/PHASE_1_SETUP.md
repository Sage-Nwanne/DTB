# Phase 1: Django Templates + Tailwind + htmx Setup

## 🎯 Goal
Set up the foundation for modern, interactive Django templates with Tailwind CSS and htmx.

---

## 📦 Step 1: Install Dependencies

Add to `requirements.txt`:
```
django-tailwind>=3.7.0
django-browser-reload>=1.12.0
```

Then install:
```bash
pip install -r requirements.txt
```

---

## 🎨 Step 2: Set Up Tailwind CSS

### Create Tailwind App
```bash
python manage.py tailwind init
```

This creates a `theme` app with Tailwind configuration.

### Update `config/settings.py`

Add to `INSTALLED_APPS`:
```python
'tailwind',
'django_browser_reload',
'theme',  # Created by tailwind init
```

Add to `MIDDLEWARE`:
```python
'django_browser_reload.middleware.BrowserReloadMiddleware',
```

### Configure Tailwind Colors

Edit `theme/static_src/tailwind.config.js`:

```javascript
module.exports = {
  content: [
    '../templates/**/*.html',
    '../../main_app/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        charcoal: '#0c0c0c',
        slate: '#141414',
        graphite: '#1a1a1a',
        accent: '#ff9f1a',
        'accent-dark': '#b35400',
        text: '#e9e9e9',
      },
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
```

### Add Google Fonts

In `main_app/templates/base.html` (head):
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## 🔄 Step 3: Install htmx

Add to `base.html` (before closing `</body>`):
```html
<script src="https://unpkg.com/htmx.org@1.9.10"></script>
```

Or install via npm:
```bash
npm install htmx.org
```

---

## 🏗️ Step 4: Create Base Template Structure

### `main_app/templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}DTB — Web + Agentic Automation Studio{% endblock %}</title>
    <meta name="description" content="{% block meta_description %}Design. Automate. Breakthrough.{% endblock %}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    {% tailwind_css %}
    
    {% block extra_css %}{% endblock %}
</head>
<body class="bg-charcoal text-text font-inter">
    <!-- Navigation -->
    {% include 'components/navbar.html' %}
    
    <!-- Main Content -->
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    {% include 'components/footer.html' %}
    
    <!-- htmx -->
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 🧩 Step 5: Create Component Templates

### `main_app/templates/components/navbar.html`
```html
<nav class="sticky top-0 z-50 bg-charcoal border-b border-slate">
    <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <div class="text-2xl font-poppins font-bold text-accent">DTB</div>
        <ul class="flex gap-8">
            <li><a href="/" class="hover:text-accent transition">Home</a></li>
            <li><a href="/services/" class="hover:text-accent transition">Services</a></li>
            <li><a href="/portfolio/" class="hover:text-accent transition">Portfolio</a></li>
            <li><a href="/about/" class="hover:text-accent transition">About</a></li>
            <li><a href="/reviews/" class="hover:text-accent transition">Reviews</a></li>
            <li><a href="/contact/" class="hover:text-accent transition">Contact</a></li>
        </ul>
        <a href="/contact/" class="bg-accent text-charcoal px-6 py-2 rounded-md font-bold hover:shadow-lg hover:shadow-accent/50 transition">
            Start a Project
        </a>
    </div>
</nav>
```

### `main_app/templates/components/footer.html`
```html
<footer class="bg-slate border-t border-graphite mt-20">
    <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-2 gap-8">
        <div>
            <h3 class="font-poppins font-bold text-lg mb-4">DTB</h3>
            <ul class="space-y-2 text-sm">
                <li><a href="/" class="hover:text-accent transition">Home</a></li>
                <li><a href="/services/" class="hover:text-accent transition">Services</a></li>
                <li><a href="/portfolio/" class="hover:text-accent transition">Portfolio</a></li>
            </ul>
        </div>
        <div>
            <h3 class="font-poppins font-bold text-lg mb-4">Company</h3>
            <ul class="space-y-2 text-sm">
                <li><a href="/about/" class="hover:text-accent transition">About</a></li>
                <li><a href="/reviews/" class="hover:text-accent transition">Reviews</a></li>
                <li><a href="/contact/" class="hover:text-accent transition">Contact</a></li>
            </ul>
        </div>
    </div>
    <div class="border-t border-graphite px-4 py-4 text-center text-sm text-gray-400">
        © 2025 DTB. All rights reserved.
    </div>
</footer>
```

---

## 🎨 Step 6: Create Reusable Components

### `main_app/templates/components/button.html`
```html
<a href="{{ url }}" class="inline-block px-6 py-2 rounded-md font-bold transition {% if primary %}bg-accent text-charcoal hover:shadow-lg hover:shadow-accent/50{% else %}border border-accent text-accent hover:bg-accent/10{% endif %}">
    {{ label }}
</a>
```

### `main_app/templates/components/service_card.html`
```html
<div class="bg-graphite p-6 rounded-lg hover:translate-y-[-4px] transition">
    <div class="text-3xl mb-4">{{ icon }}</div>
    <h3 class="font-poppins font-bold text-lg mb-2">{{ title }}</h3>
    <p class="text-sm text-gray-300 mb-4">{{ description }}</p>
    <a href="{{ link }}" class="text-accent hover:text-accent-dark transition text-sm font-bold">Learn more →</a>
</div>
```

---

## 🚀 Step 7: Run Development Server

```bash
# Terminal 1: Tailwind watcher
python manage.py tailwind start

# Terminal 2: Django dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and you should see Tailwind CSS working!

---

## ✅ Checklist

- [ ] Tailwind CSS installed and configured
- [ ] htmx added to base template
- [ ] Google Fonts loaded
- [ ] Custom colors defined in Tailwind config
- [ ] Base template created
- [ ] Navbar component created
- [ ] Footer component created
- [ ] Button component created
- [ ] Service card component created
- [ ] Dev server running with Tailwind watcher

---

## 📝 Next: Build Home Page

Once this is set up, we'll:
1. Create `home.html` with hero section
2. Add service cards
3. Add proof strip
4. Add testimonial slider (with htmx)
5. Add CTA sections

---

## 🔗 Useful Links

- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [django-tailwind](https://django-tailwind.readthedocs.io/)
- [htmx Docs](https://htmx.org/docs/)
- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)

