# Heroku Deployment Fix - Tailwind CSS Build

## Problem
Heroku deployment was failing with:
```
Error: Unable to generate Django static files.
The 'python manage.py collectstatic --noinput' Django management command failed.
```

## Root Cause
Tailwind CSS needs to be compiled from source during the Heroku build process. The compiled CSS file (`theme/static/css/dist/styles.css`) is in `.gitignore` and wasn't being built on Heroku.

## Solution Implemented

### 1. Added Node.js Buildpack
Created `.buildpacks` file to tell Heroku to use both Node.js and Python buildpacks:
```
https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/nodejs.tgz
https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/python.tgz
```

### 2. Created Build Script
Created `build.sh` that:
- Installs Node.js dependencies
- Builds Tailwind CSS
- Collects Django static files

### 3. Updated Procfile
Added release phase to Procfile:
```
release: bash build.sh && python manage.py migrate
web: gunicorn config.wsgi --log-file -
```

The `release` phase runs once during deployment before the web dyno starts.

## What Happens During Deployment

1. **Build Phase**
   - Heroku detects Node.js (package.json in theme/static_src)
   - Heroku detects Python (requirements.txt)
   - Both buildpacks are applied

2. **Release Phase** (runs once)
   - `build.sh` executes:
     - `npm install` - Install Node dependencies
     - `npm run build` - Build Tailwind CSS
     - `python manage.py collectstatic` - Collect Django static files
   - `python manage.py migrate` - Run database migrations

3. **Web Phase** (runs continuously)
   - `gunicorn config.wsgi` - Start Django app

## How to Deploy Now

### Step 1: Verify Changes
```bash
cd /home/sage_nwanne/personal-work/DTB
git log --oneline -3
# Should show: "Add Heroku build configuration for Tailwind CSS"
```

### Step 2: Deploy from Heroku Dashboard
1. Go to https://dashboard.heroku.com/
2. Click your app
3. Click **Deploy** tab
4. Click **Deploy Branch**
5. Watch the build logs

### Step 3: Monitor Build
You should see:
```
-----> Building on the Heroku-20 stack
-----> Detecting buildpacks
-----> Node.js app detected
-----> Python app detected
-----> Installing Node.js
-----> Installing Python
-----> Installing dependencies with pip
-----> Installing dependencies with npm
-----> Building Tailwind CSS
-----> Collecting static files
-----> Build succeeded!
```

### Step 4: Run Migrations
```bash
heroku run python manage.py migrate
```

### Step 5: Test
```bash
heroku open
```

## Files Changed

1. **Procfile** - Added release phase
2. **build.sh** - New build script
3. **.buildpacks** - New buildpack configuration

## Troubleshooting

### If build still fails:

Check logs:
```bash
heroku logs --tail
```

Common issues:
- Missing `package.json` in `theme/static_src/` - Check it exists
- Node version mismatch - Heroku uses latest Node by default
- npm dependencies not installed - `npm install` should handle this

### If static files still 404:

```bash
# Manually collect static files
heroku run python manage.py collectstatic --noinput

# Check if files were collected
heroku run ls -la staticfiles/
```

### If CSS not loading:

Check that `theme/static/css/dist/styles.css` was built:
```bash
heroku run ls -la theme/static/css/dist/
```

## Next Steps

1. Deploy from Heroku dashboard
2. Monitor build logs
3. Run migrations
4. Test your app
5. Connect your domain

---

**The fix is ready! Deploy now from the Heroku dashboard.** 🚀

