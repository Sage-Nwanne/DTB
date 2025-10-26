# Deploy to Heroku - Quick Start

This is a quick reference to deploy your DTB app to Heroku right now.

## What You Need

1. **Heroku Account** - Sign up at https://www.heroku.com/ (free tier available)
2. **Heroku CLI** - Download from https://devcenter.heroku.com/articles/heroku-cli
3. **Your Domain Name** - The domain you own (e.g., yourdomain.com)

## Installation (One-Time Setup)

### 1. Install Heroku CLI

```bash
# On Linux/macOS
curl https://cli-assets.heroku.com/install.sh | sh

# Verify it worked
heroku --version
```

### 2. Login to Heroku

```bash
heroku login
```

A browser window will open. Click "Log In" and authenticate.

## Deployment (5 Minutes)

### Step 1: Create Your Heroku App

```bash
cd /home/sage_nwanne/personal-work/DTB

# Create app (replace 'dtb-website' with your desired name)
heroku create dtb-website
```

**Your app URL will be:** `https://dtb-website.herokuapp.com`

### Step 2: Generate Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the output (it's a long random string).

### Step 3: Set Environment Variables

```bash
# Replace 'your-secret-key' with the key you just generated
heroku config:set DJANGO_SECRET_KEY='your-secret-key'

# Replace 'yourdomain.com' with your actual domain
heroku config:set DOMAIN_NAME='yourdomain.com'

# Use production settings
heroku config:set DJANGO_SETTINGS_MODULE='config.settings_production'
```

### Step 4: Deploy Your App

```bash
# Make sure everything is committed
git add .
git commit -m "Deploy to Heroku"

# Push to Heroku
git push heroku main
```

Watch the logs as it deploys. Wait for "Verifying deploy... done"

### Step 5: Setup Database

```bash
# Run migrations
heroku run python manage.py migrate

# Create admin account (optional)
heroku run python manage.py createsuperuser
```

### Step 6: Test Your App

```bash
# Open in browser
heroku open

# Or visit: https://dtb-website.herokuapp.com
```

## Connect Your Domain (10 Minutes)

### Step 1: Add Domain to Heroku

```bash
heroku domains:add yourdomain.com
heroku domains:add www.yourdomain.com

# Get DNS target
heroku domains
```

You'll see something like:
```
yourdomain.com  ├─ DNS Target: dtb-website.herokuapp.com
www.yourdomain.com  ├─ DNS Target: dtb-website.herokuapp.com
```

### Step 2: Update Your Domain Registrar

Go to your domain registrar (GoDaddy, Namecheap, Bluehost, etc.):

1. **Find DNS Settings** (usually under "Manage Domain" or "DNS")

2. **Add/Update CNAME Records:**

   **For www.yourdomain.com:**
   - Type: CNAME
   - Name: www
   - Value: dtb-website.herokuapp.com

   **For yourdomain.com (root domain):**
   - Type: CNAME (or ALIAS if CNAME not available)
   - Name: @ (or leave blank)
   - Value: dtb-website.herokuapp.com

3. **Save Changes**

### Step 3: Wait for DNS Propagation

DNS changes take 5-48 hours to propagate. Check status:

```bash
# Check if DNS is updated
nslookup yourdomain.com

# Should show: dtb-website.herokuapp.com
```

### Step 4: Enable SSL Certificate

```bash
heroku certs:auto:enable
```

## Verify Everything Works

Once DNS propagates (usually within a few hours):

1. Visit `https://yourdomain.com` in your browser
2. Check for green lock (SSL certificate)
3. Test all functionality
4. Check logs for errors:
   ```bash
   heroku logs --tail
   ```

## Common Issues & Fixes

### "DisallowedHost" Error
```bash
# Make sure DOMAIN_NAME is set correctly
heroku config | grep DOMAIN_NAME

# Update if needed
heroku config:set DOMAIN_NAME='yourdomain.com'
```

### Static Files Not Loading
```bash
heroku run python manage.py collectstatic --noinput
```

### App Crashes
```bash
# Check logs
heroku logs --tail

# Restart app
heroku ps:restart
```

### DNS Not Working
```bash
# Check DNS records
nslookup yourdomain.com

# Verify Heroku domains
heroku domains

# Wait longer (can take up to 48 hours)
```

## Useful Commands

```bash
# View app info
heroku info

# View logs
heroku logs --tail

# View config variables
heroku config

# Restart app
heroku ps:restart

# Run Django command
heroku run python manage.py shell

# Check app status
heroku ps
```

## Next Steps

1. ✅ Deploy to Heroku
2. ✅ Connect your domain
3. Set up email (SendGrid, Mailgun)
4. Set up error tracking (Sentry)
5. Configure backups
6. Monitor performance

## Need Help?

- **Heroku Docs:** https://devcenter.heroku.com/
- **Django Deployment:** https://docs.djangoproject.com/en/5.2/howto/deployment/
- **Full Guide:** See `HEROKU_DEPLOYMENT_GUIDE.md`
- **Checklist:** See `HEROKU_DEPLOYMENT_CHECKLIST.md`

---

**Ready? Start with "Deployment (5 Minutes)" section above!**

