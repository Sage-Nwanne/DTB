# Deploy Now - GitHub Connected to Heroku

You've already connected GitHub to Heroku. Here's the fastest path to deployment.

## ⚡ 5-Minute Deployment

### Step 1: Push Your Code to GitHub

```bash
cd /home/sage_nwanne/personal-work/DTB

# Check what's changed
git status

# Add all changes
git add .

# Commit
git commit -m "Ready for Heroku deployment"

# Push to GitHub
git push origin main
```

**Verify on GitHub:** https://github.com/Sage-Nwanne/DTB-website

### Step 2: Set Environment Variables on Heroku

Go to https://dashboard.heroku.com/

1. Click your app
2. Click **Settings** tab
3. Click **Reveal Config Vars**
4. Add these 3 variables:

```
DJANGO_SECRET_KEY = [generate new key below]
DOMAIN_NAME = yourdomain.com
DJANGO_SETTINGS_MODULE = config.settings_production
```

**Generate Secret Key:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the output and paste it as `DJANGO_SECRET_KEY` value.

### Step 3: Deploy from GitHub

Go to https://dashboard.heroku.com/

1. Click your app
2. Click **Deploy** tab
3. Scroll down to **Manual deploy**
4. Click **Deploy Branch**
5. Watch the build logs

**Wait for:** "Build succeeded!" message

### Step 4: Run Migrations

```bash
heroku run python manage.py migrate
```

Or via dashboard:
1. Click **More** (top right)
2. Click **Run console**
3. Type: `python manage.py migrate`
4. Press Enter

### Step 5: Test Your App

```bash
heroku open
```

Or visit: https://your-app-name.herokuapp.com

**Check logs if there are errors:**
```bash
heroku logs --tail
```

---

## 🌐 10-Minute Domain Setup

### Step 1: Add Domain to Heroku

```bash
heroku domains:add yourdomain.com
heroku domains:add www.yourdomain.com

# Get DNS target
heroku domains
```

You'll see:
```
yourdomain.com  ├─ DNS Target: your-app-name.herokuapp.com
www.yourdomain.com  ├─ DNS Target: your-app-name.herokuapp.com
```

### Step 2: Update Domain Registrar

Go to your domain registrar (GoDaddy, Namecheap, Bluehost, etc.):

1. Find **DNS Settings** or **Manage DNS**
2. Add these CNAME records:

**For www.yourdomain.com:**
- Type: CNAME
- Name: www
- Value: your-app-name.herokuapp.com

**For yourdomain.com (root):**
- Type: CNAME (or ALIAS if CNAME not available)
- Name: @ (or leave blank)
- Value: your-app-name.herokuapp.com

3. Save changes

### Step 3: Enable SSL

```bash
heroku certs:auto:enable
```

### Step 4: Wait for DNS

DNS propagation takes 5-48 hours (usually 1-2 hours).

Check status:
```bash
nslookup yourdomain.com
```

Should show: `your-app-name.herokuapp.com`

### Step 5: Visit Your Domain

Once DNS propagates:
- https://yourdomain.com
- https://www.yourdomain.com

---

## 📋 Complete Checklist

### Pre-Deployment
- [ ] All code committed to GitHub
- [ ] GitHub connected to Heroku (already done ✅)
- [ ] Heroku app created (already done ✅)

### Deployment
- [ ] Push code to GitHub
- [ ] Set 3 environment variables on Heroku
- [ ] Deploy from GitHub dashboard
- [ ] Run migrations
- [ ] Test app

### Domain
- [ ] Add domain to Heroku
- [ ] Update DNS records at registrar
- [ ] Enable SSL
- [ ] Wait for DNS propagation
- [ ] Test domain

---

## 🔄 Future Deployments

Now it's super easy! Just:

```bash
# Make changes
# Test locally
# Commit
git add .
git commit -m "Your message"

# Push to GitHub
git push origin main

# Option 1: Auto-deploy (if enabled)
# Heroku automatically deploys

# Option 2: Manual deploy
# Go to Heroku dashboard → Deploy tab → Deploy Branch
```

---

## ⚠️ If Something Goes Wrong

### Check Logs
```bash
heroku logs --tail
```

### Common Issues

**DisallowedHost error:**
```bash
heroku config:set DOMAIN_NAME='yourdomain.com'
```

**Database errors:**
```bash
heroku run python manage.py migrate
```

**Static files 404:**
```bash
heroku run python manage.py collectstatic --noinput
```

**App crashes:**
```bash
heroku ps:restart
```

---

## 📞 Need Help?

- **Full Guide:** See `GITHUB_HEROKU_DEPLOYMENT.md`
- **Heroku Docs:** https://devcenter.heroku.com/
- **Django Docs:** https://docs.djangoproject.com/en/5.2/howto/deployment/

---

## 🚀 Ready? Start with Step 1 above!

**Total time: ~15 minutes (5 min deploy + 10 min domain)**

