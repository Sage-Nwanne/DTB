# Deploying DTB Website on Platform as a Service (PaaS)

Quick deployment guides for popular PaaS platforms: Railway, Render, and Heroku.

## 🚂 Railway (Recommended - Easiest)

### Why Railway?
- ✅ Extremely simple deployment
- ✅ GitHub integration
- ✅ Automatic SSL
- ✅ Free $5 credit monthly
- ✅ PostgreSQL database included

### Deployment Steps

1. **Sign Up**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Prepare Your Code**
   
   Ensure these files exist in `DTB-website/DTB_website/`:
   - `requirements.txt` ✅ (already created)
   - `Procfile` ✅ (already created)
   - `railway.json` ✅ (already created)
   - `runtime.txt` ✅ (already created)

3. **Push to GitHub**
   ```bash
   cd DTB-website/DTB_website
   git init
   git add .
   git commit -m "Initial commit for Railway deployment"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

4. **Create New Project on Railway**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Django

5. **Add Environment Variables**
   
   In Railway dashboard → Variables:
   ```
   DJANGO_SECRET_KEY=<generate-new-secret-key>
   DJANGO_SETTINGS_MODULE=DTB_website.settings_production
   DOMAIN_NAME=yourdomain.com
   ```

6. **Add PostgreSQL Database (Optional)**
   - Click "New" → "Database" → "PostgreSQL"
   - Railway automatically sets `DATABASE_URL`

7. **Add Custom Domain**
   - Go to Settings → Domains
   - Click "Add Custom Domain"
   - Enter: `yourdomain.com`
   - Update your DNS (see DEPLOYMENT_SQUARESPACE.md)

8. **Deploy**
   - Railway automatically deploys on git push
   - View logs in the dashboard

### Railway Commands

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link to project
railway link

# View logs
railway logs

# Run migrations
railway run python manage.py migrate

# Create superuser
railway run python manage.py createsuperuser
```

---

## 🎨 Render

### Why Render?
- ✅ Free tier available
- ✅ Automatic SSL
- ✅ Easy database setup
- ✅ Good documentation

### Deployment Steps

1. **Sign Up**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repo

3. **Configure Service**
   
   **Basic Settings:**
   - Name: `dtb-website`
   - Region: Choose closest to your users
   - Branch: `main`
   - Runtime: `Python 3`

   **Build Settings:**
   - Build Command:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput
     ```
   
   - Start Command:
     ```bash
     gunicorn DTB_website.wsgi:application
     ```

4. **Add Environment Variables**
   
   In Environment section:
   ```
   DJANGO_SECRET_KEY=<your-secret-key>
   DJANGO_SETTINGS_MODULE=DTB_website.settings_production
   DOMAIN_NAME=yourdomain.com
   PYTHON_VERSION=3.11.0
   ```

5. **Add PostgreSQL Database (Optional)**
   - Click "New +" → "PostgreSQL"
   - Name it `dtb-database`
   - Copy the Internal Database URL
   - Add to your web service as `DATABASE_URL`

6. **Add Custom Domain**
   - Go to Settings → Custom Domains
   - Click "Add Custom Domain"
   - Enter your domain
   - Update DNS records (see DEPLOYMENT_SQUARESPACE.md)

7. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically

### Render Build Script (Alternative)

Create `build.sh`:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Make it executable:
```bash
chmod +x build.sh
```

Update Build Command to: `./build.sh`

---

## 🟣 Heroku

### Why Heroku?
- ✅ Mature platform
- ✅ Extensive add-ons
- ✅ Good documentation
- ⚠️ No free tier anymore (starts at $5/month)

### Deployment Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku

   # Ubuntu
   curl https://cli-assets.heroku.com/install.sh | sh

   # Windows
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Prepare Your Project**
   
   Create `Procfile` (already exists):
   ```
   web: gunicorn DTB_website.wsgi --log-file -
   ```

   Update `requirements.txt` to include:
   ```
   dj-database-url
   psycopg2-binary
   ```

4. **Create Heroku App**
   ```bash
   cd DTB-website/DTB_website
   heroku create dtb-website
   ```

5. **Add PostgreSQL**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

6. **Set Environment Variables**
   ```bash
   # Generate secret key
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

   # Set variables
   heroku config:set DJANGO_SECRET_KEY='your-generated-key'
   heroku config:set DJANGO_SETTINGS_MODULE=DTB_website.settings_production
   heroku config:set DOMAIN_NAME=yourdomain.com
   ```

7. **Update settings_production.py for Heroku**
   
   Add at the top:
   ```python
   import dj_database_url
   ```

   Replace DATABASES:
   ```python
   DATABASES = {
       'default': dj_database_url.config(
           conn_max_age=600,
           conn_health_checks=True,
       )
   }
   ```

8. **Deploy to Heroku**
   ```bash
   git add .
   git commit -m "Configure for Heroku"
   git push heroku main
   ```

9. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

10. **Add Custom Domain**
    ```bash
    heroku domains:add yourdomain.com
    heroku domains:add www.yourdomain.com
    ```

11. **Enable SSL**
    ```bash
    heroku certs:auto:enable
    ```

### Heroku Useful Commands

```bash
# View logs
heroku logs --tail

# Open app in browser
heroku open

# Run Django shell
heroku run python manage.py shell

# Scale dynos
heroku ps:scale web=1

# Restart app
heroku restart
```

---

## 📊 Platform Comparison

| Feature | Railway | Render | Heroku |
|---------|---------|--------|--------|
| **Free Tier** | $5 credit/month | Yes (limited) | No |
| **Paid Plans** | From $5/month | From $7/month | From $5/month |
| **Ease of Use** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Auto SSL** | Yes | Yes | Yes |
| **Database** | PostgreSQL | PostgreSQL | PostgreSQL |
| **GitHub Integration** | Yes | Yes | Yes |
| **Custom Domains** | Yes | Yes | Yes |
| **Build Time** | Fast | Medium | Medium |
| **Best For** | Beginners | Small-Medium | Enterprise |

## 🎯 Recommendation

**For DTB Website, we recommend Railway because:**
1. Easiest setup process
2. Generous free tier ($5 credit/month)
3. Automatic deployments from GitHub
4. Built-in PostgreSQL
5. Excellent developer experience

## 🔧 Post-Deployment Checklist

After deploying to any platform:

- [ ] Test all pages load correctly
- [ ] Verify static files (CSS, images) work
- [ ] Test admin panel (`/admin`)
- [ ] Test user authentication
- [ ] Test file uploads (profile pictures, certificates)
- [ ] Check HTTPS is working
- [ ] Set up custom domain
- [ ] Create superuser account
- [ ] Add initial content
- [ ] Set up monitoring (optional)
- [ ] Configure backups

## 🚨 Common Issues

### Static Files Not Loading
```bash
# Ensure collectstatic runs in build
python manage.py collectstatic --noinput

# Check STATIC_ROOT in settings_production.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Database Connection Error
```bash
# Verify DATABASE_URL is set
# For Railway/Render, it's automatic
# For Heroku, check: heroku config
```

### 400 Bad Request
```bash
# Update ALLOWED_HOSTS
# Set DOMAIN_NAME environment variable
```

### Build Fails
```bash
# Check Python version in runtime.txt
# Verify all dependencies in requirements.txt
# Check build logs for specific errors
```

---

## 📞 Support Resources

- **Railway**: [docs.railway.app](https://docs.railway.app)
- **Render**: [render.com/docs](https://render.com/docs)
- **Heroku**: [devcenter.heroku.com](https://devcenter.heroku.com)

## 🎉 Next Steps

After successful deployment:
1. Set up monitoring (Sentry, LogRocket)
2. Configure email service (SendGrid, Mailgun)
3. Set up automated backups
4. Add analytics (Google Analytics)
5. Optimize performance (CDN, caching)

---

**Happy Deploying! 🚀**

