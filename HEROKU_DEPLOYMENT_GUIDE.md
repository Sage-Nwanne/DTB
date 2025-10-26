# Heroku Deployment Guide for DTB

This guide will walk you through deploying your Django application to Heroku and connecting your custom domain.

## Prerequisites

1. **Heroku Account** - Sign up at https://www.heroku.com/
2. **Heroku CLI** - Install from https://devcenter.heroku.com/articles/heroku-cli
3. **Git** - Already installed on your system
4. **Your Domain** - You should own a domain name
5. **PostgreSQL Database** (optional but recommended for production)

## Step 1: Install Heroku CLI

```bash
# On Linux/macOS
curl https://cli-assets.heroku.com/install.sh | sh

# Verify installation
heroku --version
```

## Step 2: Login to Heroku

```bash
heroku login
```

This will open a browser window to authenticate. Follow the prompts.

## Step 3: Create a Heroku App

```bash
cd /home/sage_nwanne/personal-work/DTB

# Create a new Heroku app (replace 'your-app-name' with your desired app name)
heroku create your-app-name

# Or if you already have an app, add the remote:
heroku git:remote -a your-app-name
```

**Note:** Your app will be available at `https://your-app-name.herokuapp.com`

## Step 4: Set Environment Variables

```bash
# Set your Django secret key (generate a new one for production)
heroku config:set DJANGO_SECRET_KEY='your-secret-key-here'

# Set your domain name
heroku config:set DOMAIN_NAME='yourdomain.com'

# Set Django settings module to use production settings
heroku config:set DJANGO_SETTINGS_MODULE='config.settings_production'
```

**To generate a secure secret key:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Step 5: Configure Database (Optional but Recommended)

For production, use PostgreSQL instead of SQLite:

```bash
# Add PostgreSQL add-on (free tier available)
heroku addons:create heroku-postgresql:essential-0

# This automatically sets DATABASE_URL environment variable
```

If using PostgreSQL, update `config/settings_production.py`:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

And add to requirements.txt:
```
dj-database-url>=1.3.0
psycopg2-binary>=2.9.0
```

## Step 6: Collect Static Files

Create a `Procfile.local` for local testing (already exists as `Procfile`):

```bash
# The Procfile should contain:
# web: gunicorn config.wsgi --log-file -
```

## Step 7: Deploy to Heroku

```bash
# Make sure all changes are committed
git add .
git commit -m "Prepare for Heroku deployment"

# Push to Heroku
git push heroku main

# Run migrations on Heroku
heroku run python manage.py migrate

# Create a superuser (optional)
heroku run python manage.py createsuperuser
```

## Step 8: View Your App

```bash
# Open your app in the browser
heroku open

# Or visit: https://your-app-name.herokuapp.com
```

## Step 9: Connect Your Custom Domain

### Option A: Using Heroku's DNS (Recommended)

1. **Add your domain to Heroku:**
```bash
heroku domains:add yourdomain.com
heroku domains:add www.yourdomain.com
```

2. **Get the DNS target:**
```bash
heroku domains
```

You'll see output like:
```
yourdomain.com  ├─ DNS Target: your-app-name.herokuapp.com
www.yourdomain.com  ├─ DNS Target: your-app-name.herokuapp.com
```

3. **Update your domain registrar's DNS records:**

Go to your domain registrar (GoDaddy, Namecheap, etc.) and add:

**For yourdomain.com:**
- Type: CNAME
- Name: @ (or leave blank)
- Value: your-app-name.herokuapp.com

**For www.yourdomain.com:**
- Type: CNAME
- Name: www
- Value: your-app-name.herokuapp.com

**Note:** If your registrar doesn't allow CNAME for root domain (@), use:
- Type: ALIAS or ANAME
- Name: @
- Value: your-app-name.herokuapp.com

4. **Wait for DNS propagation (5-48 hours)**

```bash
# Check DNS status
heroku domains
```

### Option B: Using Heroku SSL Certificate

```bash
# Add automatic SSL certificate
heroku certs:auto:enable

# Check certificate status
heroku certs:auto
```

## Step 10: Verify Deployment

```bash
# Check app logs
heroku logs --tail

# Check app status
heroku ps

# View environment variables
heroku config
```

## Troubleshooting

### App crashes on startup
```bash
heroku logs --tail
```

### Static files not loading
```bash
heroku run python manage.py collectstatic --noinput
```

### Database errors
```bash
heroku run python manage.py migrate
```

### Clear Heroku cache
```bash
heroku builds:cancel
git commit --allow-empty -m "Rebuild"
git push heroku main
```

## Common Issues

| Issue | Solution |
|-------|----------|
| `DisallowedHost` error | Check `DOMAIN_NAME` env var and `ALLOWED_HOSTS` in settings |
| Static files 404 | Run `heroku run python manage.py collectstatic --noinput` |
| Database locked | Restart dynos: `heroku ps:restart` |
| Slow deployment | Check `requirements.txt` for unnecessary packages |

## Useful Heroku Commands

```bash
# View app info
heroku info

# Restart app
heroku ps:restart

# View config variables
heroku config

# Set config variable
heroku config:set KEY=value

# Remove config variable
heroku config:unset KEY

# View logs
heroku logs --tail

# Run one-off command
heroku run python manage.py shell

# Scale dynos
heroku ps:scale web=1

# Check app status
heroku status
```

## Next Steps

1. Test your app at `https://yourdomain.com`
2. Set up email notifications (optional)
3. Configure error tracking (Sentry, etc.)
4. Set up CI/CD pipeline for automatic deployments
5. Monitor app performance

## Support

- Heroku Documentation: https://devcenter.heroku.com/
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/
- Heroku Support: https://help.heroku.com/

---

**Last Updated:** October 26, 2025

