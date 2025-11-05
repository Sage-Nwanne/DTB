# Deploying DTB Website with Squarespace Domain

This guide explains how to connect your Squarespace domain to your Django application hosted on an external server.

## 🎯 Overview

Since Squarespace doesn't support hosting Django applications directly, you'll need to:
1. Host your Django app on a separate hosting provider
2. Point your Squarespace domain to your hosting server using DNS records

## 📋 Prerequisites

- A domain purchased through Squarespace
- A hosting provider for your Django app (see options below)
- Access to Squarespace DNS settings

## 🏢 Step 1: Choose a Hosting Provider

### Recommended Options:

#### A. **DigitalOcean App Platform** (Easiest)
- **Cost**: ~$5-12/month
- **Pros**: Easy setup, managed service, automatic SSL
- **Best for**: Beginners

#### B. **Railway** (Developer-Friendly)
- **Cost**: Pay-as-you-go (~$5-10/month)
- **Pros**: Simple deployment, GitHub integration
- **Best for**: Quick deployment

#### C. **Render** (Free Tier Available)
- **Cost**: Free tier available, paid from $7/month
- **Pros**: Free SSL, automatic deployments
- **Best for**: Testing/small projects

#### D. **DigitalOcean Droplet** (Full Control)
- **Cost**: $6-12/month
- **Pros**: Full server control, scalable
- **Best for**: Advanced users

## 🚀 Step 2: Deploy Your Django App

### Option A: Deploy to Railway (Recommended for Beginners)

1. **Create a Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Prepare Your Project**
   ```bash
   cd DTB-website/DTB_website
   ```

3. **Create `Procfile`** (if not exists)
   ```
   web: gunicorn DTB_website.wsgi --log-file -
   ```

4. **Create `railway.json`**
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn DTB_website.wsgi",
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10
     }
   }
   ```

5. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

6. **Deploy on Railway**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add environment variables:
     - `DJANGO_SECRET_KEY`: (generate new one)
     - `DJANGO_SETTINGS_MODULE`: `DTB_website.settings_production`
     - `DOMAIN_NAME`: `yourdomain.com`
   - Railway will provide you with a URL like: `your-app.railway.app`

7. **Get Your Server IP or URL**
   - Note the Railway-provided URL (e.g., `your-app.railway.app`)

### Option B: Deploy to DigitalOcean App Platform

1. **Create DigitalOcean Account**
   - Go to [digitalocean.com](https://www.digitalocean.com)
   - Sign up and add payment method

2. **Create New App**
   - Click "Create" → "Apps"
   - Connect your GitHub repository
   - Select your repo and branch

3. **Configure App**
   - Detected as Python app
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn --worker-tmp-dir /dev/shm DTB_website.wsgi`

4. **Add Environment Variables**
   - `DJANGO_SECRET_KEY`
   - `DJANGO_SETTINGS_MODULE=DTB_website.settings_production`
   - `DOMAIN_NAME=yourdomain.com`

5. **Deploy**
   - Click "Create Resources"
   - Wait for deployment
   - Note your app URL

### Option C: Deploy to Render

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   - Name: `dtb-website`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn DTB_website.wsgi:application`

4. **Add Environment Variables**
   - `DJANGO_SECRET_KEY`
   - `DJANGO_SETTINGS_MODULE=DTB_website.settings_production`
   - `DOMAIN_NAME=yourdomain.com`
   - `PYTHON_VERSION=3.11.0`

5. **Deploy**
   - Click "Create Web Service"
   - Note your Render URL (e.g., `your-app.onrender.com`)

## 🌐 Step 3: Configure Squarespace DNS

Now that your app is hosted, connect your Squarespace domain:

### 1. Get Your Hosting Information

Depending on your hosting provider, you'll need either:
- **IP Address** (for A records) - if using VPS/Droplet
- **Domain/URL** (for CNAME records) - if using Railway/Render/App Platform

### 2. Access Squarespace DNS Settings

1. Log in to [Squarespace](https://www.squarespace.com)
2. Go to **Settings** → **Domains**
3. Click on your domain
4. Click **DNS Settings**

### 3. Configure DNS Records

#### If Your Host Provides an IP Address (A Record):

1. **Add A Record for Root Domain**
   - Host: `@`
   - Type: `A`
   - Data: `Your.Server.IP.Address`
   - TTL: `3600`

2. **Add A Record for WWW**
   - Host: `www`
   - Type: `A`
   - Data: `Your.Server.IP.Address`
   - TTL: `3600`

#### If Your Host Provides a URL (CNAME Record):

1. **Add CNAME Record for WWW**
   - Host: `www`
   - Type: `CNAME`
   - Data: `your-app.railway.app` (or your hosting URL)
   - TTL: `3600`

2. **Add CNAME Flattening for Root Domain**
   - Host: `@`
   - Type: `CNAME`
   - Data: `your-app.railway.app`
   - TTL: `3600`

   ⚠️ **Note**: Squarespace supports CNAME flattening, which allows CNAME records at the root domain.

### 4. Update Your Hosting Provider

#### For Railway:
1. Go to your Railway project
2. Click "Settings" → "Domains"
3. Click "Add Custom Domain"
4. Enter: `yourdomain.com` and `www.yourdomain.com`
5. Railway will automatically provision SSL certificates

#### For Render:
1. Go to your Render dashboard
2. Click your service → "Settings"
3. Scroll to "Custom Domains"
4. Add: `yourdomain.com` and `www.yourdomain.com`
5. Render will automatically provision SSL certificates

#### For DigitalOcean:
1. Go to your App
2. Click "Settings" → "Domains"
3. Click "Add Domain"
4. Enter your domain
5. Follow the verification steps

## ⏱️ Step 4: Wait for DNS Propagation

- DNS changes can take **15 minutes to 48 hours** to propagate
- Usually takes 1-4 hours
- Check status: [whatsmydns.net](https://www.whatsmydns.net)

## ✅ Step 5: Verify Deployment

1. **Test Your Domain**
   ```bash
   ping yourdomain.com
   ```

2. **Check HTTPS**
   - Visit `https://yourdomain.com`
   - Verify SSL certificate is valid

3. **Test All Pages**
   - Home page
   - Admin panel (`/admin`)
   - User authentication
   - File uploads

## 🔧 Troubleshooting

### Domain Not Resolving
- Wait longer (DNS propagation)
- Clear your DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)
- Check DNS records: `nslookup yourdomain.com`

### SSL Certificate Issues
- Most platforms auto-provision SSL (Let's Encrypt)
- May take 10-15 minutes after domain is added
- Ensure both `yourdomain.com` and `www.yourdomain.com` are added

### 400 Bad Request Error
- Update `ALLOWED_HOSTS` in `settings_production.py`
- Add your domain to the environment variable `DOMAIN_NAME`

### Static Files Not Loading
- Run: `python manage.py collectstatic --settings=DTB_website.settings_production`
- Ensure WhiteNoise is installed: `pip install whitenoise`
- Check `STATIC_ROOT` and `STATIC_URL` settings

### Database Issues
- For production, consider PostgreSQL instead of SQLite
- Railway/Render offer managed PostgreSQL databases

## 📊 Recommended DNS Configuration

```
Type    Host    Data                        TTL
A       @       Your.Server.IP.Address      3600
A       www     Your.Server.IP.Address      3600
```

OR (if using CNAME):

```
Type    Host    Data                        TTL
CNAME   @       your-app.railway.app        3600
CNAME   www     your-app.railway.app        3600
```

## 🎉 Success!

Your Django site should now be live at your Squarespace domain!

## 📞 Need Help?

- Railway Support: [docs.railway.app](https://docs.railway.app)
- Render Support: [render.com/docs](https://render.com/docs)
- Squarespace DNS: [support.squarespace.com](https://support.squarespace.com)

---

**Next Steps:**
- Set up automated backups
- Configure monitoring (e.g., Sentry)
- Set up email service (e.g., SendGrid)
- Enable CDN for static files (optional)

