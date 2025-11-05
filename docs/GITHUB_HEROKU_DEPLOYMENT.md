# Deploy from GitHub to Heroku - Step by Step

Now that you've connected your GitHub repo to Heroku, deployment is automatic! Here's how to deploy.

## Prerequisites ✅

- ✅ Heroku app created
- ✅ GitHub repo connected to Heroku
- ✅ Environment variables set on Heroku
- ✅ All code committed to GitHub

## Step 1: Verify GitHub Connection

### Check Heroku Dashboard

1. Go to https://dashboard.heroku.com/
2. Click on your app
3. Go to **Deploy** tab
4. Verify **GitHub** is connected under "Deployment method"
5. You should see your repository name

### Verify Branch

- Make sure the branch is set to `main` (or your default branch)
- You should see: "Connected to Sage-Nwanne/DTB-website"

## Step 2: Prepare Your Code

### Make sure everything is committed to GitHub

```bash
cd /home/sage_nwanne/personal-work/DTB

# Check status
git status

# If there are changes, commit them
git add .
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

### Verify on GitHub

1. Go to https://github.com/Sage-Nwanne/DTB-website
2. Make sure your latest commits are visible
3. Check that all files are there

## Step 3: Set Environment Variables on Heroku

### Via Heroku Dashboard

1. Go to https://dashboard.heroku.com/
2. Click on your app
3. Go to **Settings** tab
4. Click **Reveal Config Vars**
5. Add these variables:

| Key | Value |
|-----|-------|
| `DJANGO_SECRET_KEY` | Your secret key (generate new one) |
| `DOMAIN_NAME` | yourdomain.com |
| `DJANGO_SETTINGS_MODULE` | config.settings_production |

### Generate Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Via Heroku CLI

```bash
heroku config:set DJANGO_SECRET_KEY='your-secret-key'
heroku config:set DOMAIN_NAME='yourdomain.com'
heroku config:set DJANGO_SETTINGS_MODULE='config.settings_production'

# Verify
heroku config
```

## Step 4: Deploy from GitHub

### Option A: Manual Deploy (Recommended for Testing)

1. Go to https://dashboard.heroku.com/
2. Click on your app
3. Go to **Deploy** tab
4. Scroll down to "Manual deploy"
5. Click **Deploy Branch**
6. Watch the build logs

### Option B: Automatic Deploy (Optional)

1. Go to **Deploy** tab
2. Scroll to "Automatic deploys"
3. Click **Enable Automatic Deploys**
4. Now every push to `main` will auto-deploy

## Step 5: Monitor Deployment

### Watch Build Logs

```bash
# In terminal
heroku logs --tail
```

### Or in Dashboard

1. Go to your app on Heroku dashboard
2. Click **Activity** tab
3. Watch the build progress
4. Wait for "Build succeeded" message

### Expected Output

```
-----> Building on the Heroku-20 stack
-----> Using buildpack: heroku/python
-----> Python app detected
-----> Installing python-3.11.0
-----> Installing pip
-----> Installing dependencies with pip
...
-----> Collecting static files
-----> Compressing static files
-----> Build succeeded!
```

## Step 6: Run Migrations

### After successful build, run migrations

```bash
heroku run python manage.py migrate
```

### Or via Dashboard

1. Go to your app
2. Click **More** (top right)
3. Click **Run console**
4. Type: `python manage.py migrate`
5. Press Enter

## Step 7: Test Your App

### Open Your App

```bash
heroku open
```

### Or visit in browser

- https://your-app-name.herokuapp.com

### Check for Errors

```bash
heroku logs --tail
```

## Step 8: Connect Your Domain

### Add Domain to Heroku

```bash
heroku domains:add yourdomain.com
heroku domains:add www.yourdomain.com

# Get DNS target
heroku domains
```

### Update Domain Registrar

Go to your domain registrar (GoDaddy, Namecheap, etc.):

1. Find DNS settings
2. Add CNAME records:
   - **Name:** www | **Value:** your-app-name.herokuapp.com
   - **Name:** @ | **Value:** your-app-name.herokuapp.com

### Enable SSL

```bash
heroku certs:auto:enable
```

### Wait for DNS Propagation

- Usually 1-2 hours
- Can take up to 48 hours
- Check with: `nslookup yourdomain.com`

## Step 9: Verify Everything Works

### Test Your Domain

1. Visit https://yourdomain.com
2. Check for green lock (SSL)
3. Test all functionality
4. Check logs for errors

```bash
heroku logs --tail
```

## Future Deployments

### Now it's super easy!

**Option 1: Automatic (if enabled)**
- Just push to GitHub: `git push origin main`
- Heroku automatically deploys

**Option 2: Manual**
- Push to GitHub: `git push origin main`
- Go to Heroku dashboard
- Click **Deploy Branch**

## Troubleshooting

### Build Failed

```bash
# Check logs
heroku logs --tail

# Common issues:
# - Missing dependencies in requirements.txt
# - Syntax errors in code
# - Missing environment variables
```

### App Crashes After Deploy

```bash
# Check logs
heroku logs --tail

# Common issues:
# - Database migrations not run
# - Missing environment variables
# - Static files not collected
```

### Fix and Redeploy

```bash
# Fix the issue locally
# Commit changes
git add .
git commit -m "Fix deployment issue"

# Push to GitHub
git push origin main

# Heroku will auto-deploy (if enabled)
# Or manually deploy from dashboard
```

## Useful Commands

```bash
# View logs
heroku logs --tail

# View app info
heroku info

# View config variables
heroku config

# Restart app
heroku ps:restart

# Run Django command
heroku run python manage.py shell

# Check app status
heroku ps

# View recent builds
heroku builds
```

## Deployment Workflow

```
1. Make changes locally
   ↓
2. Test locally
   ↓
3. Commit to git
   git add .
   git commit -m "message"
   ↓
4. Push to GitHub
   git push origin main
   ↓
5. Heroku automatically deploys (if enabled)
   OR manually deploy from dashboard
   ↓
6. Monitor logs
   heroku logs --tail
   ↓
7. Run migrations if needed
   heroku run python manage.py migrate
   ↓
8. Test on live app
   https://yourdomain.com
```

## Quick Reference

| Task | Command |
|------|---------|
| Deploy | `git push origin main` |
| View logs | `heroku logs --tail` |
| Run migrations | `heroku run python manage.py migrate` |
| Restart app | `heroku ps:restart` |
| View config | `heroku config` |
| Set variable | `heroku config:set KEY=value` |
| Open app | `heroku open` |
| Check status | `heroku ps` |

## Next Steps

1. ✅ Make sure all code is pushed to GitHub
2. ✅ Set environment variables on Heroku
3. ✅ Deploy from GitHub (manual or automatic)
4. ✅ Run migrations
5. ✅ Test your app
6. ✅ Connect your domain
7. ✅ Enable SSL
8. ✅ Monitor with logs

---

**You're all set! Your app will now deploy automatically whenever you push to GitHub!** 🚀

