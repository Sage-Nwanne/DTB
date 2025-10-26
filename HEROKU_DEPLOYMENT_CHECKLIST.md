# Heroku Deployment Checklist

Follow these steps in order to deploy your DTB application to Heroku.

## Pre-Deployment Setup

- [ ] **Install Heroku CLI**
  ```bash
  curl https://cli-assets.heroku.com/install.sh | sh
  heroku --version
  ```

- [ ] **Login to Heroku**
  ```bash
  heroku login
  ```

- [ ] **Have your domain name ready**
  - You should own a domain (e.g., yourdomain.com)
  - Know your domain registrar (GoDaddy, Namecheap, etc.)

## Step 1: Prepare Your Application

- [ ] **Commit all changes to git**
  ```bash
  cd /home/sage_nwanne/personal-work/DTB
  git add .
  git commit -m "Prepare for Heroku deployment"
  ```

- [ ] **Verify requirements.txt is up to date**
  ```bash
  pip freeze > requirements.txt
  ```

- [ ] **Check Procfile exists**
  ```bash
  cat Procfile
  # Should show: web: gunicorn config.wsgi --log-file -
  ```

- [ ] **Verify runtime.txt**
  ```bash
  cat runtime.txt
  # Should show: python-3.11.0
  ```

## Step 2: Create Heroku App

- [ ] **Create a new Heroku app**
  ```bash
  heroku create your-app-name
  # Replace 'your-app-name' with your desired app name
  # Example: heroku create dtb-website
  ```

- [ ] **Verify Heroku remote was added**
  ```bash
  git remote -v
  # Should show heroku remote
  ```

## Step 3: Configure Environment Variables

- [ ] **Generate a new Django secret key**
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```

- [ ] **Set environment variables on Heroku**
  ```bash
  heroku config:set DJANGO_SECRET_KEY='your-generated-secret-key'
  heroku config:set DOMAIN_NAME='yourdomain.com'
  heroku config:set DJANGO_SETTINGS_MODULE='config.settings_production'
  ```

- [ ] **Verify environment variables**
  ```bash
  heroku config
  ```

## Step 4: Setup Database (Optional)

- [ ] **Add PostgreSQL add-on** (recommended for production)
  ```bash
  heroku addons:create heroku-postgresql:essential-0
  ```

- [ ] **Verify DATABASE_URL is set**
  ```bash
  heroku config | grep DATABASE_URL
  ```

## Step 5: Deploy to Heroku

- [ ] **Push code to Heroku**
  ```bash
  git push heroku main
  ```

- [ ] **Monitor deployment logs**
  ```bash
  heroku logs --tail
  ```

- [ ] **Wait for deployment to complete**
  - Watch for "Verifying deploy... done" message

## Step 6: Initialize Database

- [ ] **Run migrations**
  ```bash
  heroku run python manage.py migrate
  ```

- [ ] **Create superuser** (optional)
  ```bash
  heroku run python manage.py createsuperuser
  ```

- [ ] **Collect static files** (if needed)
  ```bash
  heroku run python manage.py collectstatic --noinput
  ```

## Step 7: Test Your App

- [ ] **Open your app**
  ```bash
  heroku open
  ```

- [ ] **Or visit in browser**
  - https://your-app-name.herokuapp.com

- [ ] **Check app logs for errors**
  ```bash
  heroku logs --tail
  ```

## Step 8: Connect Your Domain

### Get Heroku DNS Information

- [ ] **Add your domain to Heroku**
  ```bash
  heroku domains:add yourdomain.com
  heroku domains:add www.yourdomain.com
  ```

- [ ] **Get DNS target**
  ```bash
  heroku domains
  ```
  - Note the DNS Target (should be: your-app-name.herokuapp.com)

### Update Domain Registrar DNS Records

- [ ] **Login to your domain registrar**
  - GoDaddy, Namecheap, Bluehost, etc.

- [ ] **Add CNAME record for www subdomain**
  - Type: CNAME
  - Name: www
  - Value: your-app-name.herokuapp.com

- [ ] **Add CNAME or ALIAS record for root domain**
  - Type: CNAME (or ALIAS if CNAME not available)
  - Name: @ (or leave blank)
  - Value: your-app-name.herokuapp.com

- [ ] **Save DNS changes**

- [ ] **Wait for DNS propagation** (5-48 hours)
  ```bash
  # Check DNS status
  nslookup yourdomain.com
  # Should resolve to your-app-name.herokuapp.com
  ```

## Step 9: Enable SSL Certificate

- [ ] **Enable automatic SSL**
  ```bash
  heroku certs:auto:enable
  ```

- [ ] **Check certificate status**
  ```bash
  heroku certs:auto
  ```

## Step 10: Verify Everything Works

- [ ] **Visit your domain**
  - https://yourdomain.com
  - https://www.yourdomain.com

- [ ] **Check that SSL certificate is valid**
  - Look for green lock in browser

- [ ] **Test all functionality**
  - Navigation
  - Forms
  - Database queries
  - Static files (CSS, images)

- [ ] **Check app logs for errors**
  ```bash
  heroku logs --tail
  ```

## Post-Deployment

- [ ] **Set up monitoring**
  - Heroku dashboard
  - Error tracking (Sentry, etc.)

- [ ] **Configure email** (if needed)
  - SendGrid, Mailgun, etc.

- [ ] **Set up backups** (if using PostgreSQL)
  ```bash
  heroku pg:backups:schedule --at '02:00 UTC' DATABASE_URL
  ```

- [ ] **Monitor app performance**
  ```bash
  heroku ps
  heroku logs --tail
  ```

## Troubleshooting

If something goes wrong:

1. **Check logs**
   ```bash
   heroku logs --tail
   ```

2. **Restart app**
   ```bash
   heroku ps:restart
   ```

3. **Check config variables**
   ```bash
   heroku config
   ```

4. **Run migrations again**
   ```bash
   heroku run python manage.py migrate
   ```

5. **Rebuild app**
   ```bash
   git commit --allow-empty -m "Rebuild"
   git push heroku main
   ```

## Support

- Heroku Docs: https://devcenter.heroku.com/
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/
- Heroku Support: https://help.heroku.com/

---

**Ready to deploy? Start with Step 1!**

