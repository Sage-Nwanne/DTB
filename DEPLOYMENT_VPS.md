# Deploying DTB Website on a VPS (DigitalOcean, Linode, AWS EC2)

This guide covers deploying your Django application on a Virtual Private Server with full control.

## 🎯 Overview

This deployment uses:
- **Ubuntu 22.04 LTS** server
- **Nginx** as reverse proxy
- **Gunicorn** as WSGI server
- **PostgreSQL** as database (optional, recommended)
- **Supervisor** for process management
- **Let's Encrypt** for SSL certificates

## 📋 Prerequisites

- VPS with Ubuntu 22.04 (DigitalOcean Droplet, Linode, AWS EC2, etc.)
- Domain name pointing to your server IP
- SSH access to your server
- Basic Linux command line knowledge

## 🚀 Step 1: Initial Server Setup

### 1. Connect to Your Server

```bash
ssh root@your_server_ip
```

### 2. Update System Packages

```bash
apt update && apt upgrade -y
```

### 3. Create a New User (Security Best Practice)

```bash
adduser dtbadmin
usermod -aG sudo dtbadmin
```

### 4. Set Up Firewall

```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
```

### 5. Switch to New User

```bash
su - dtbadmin
```

## 🔧 Step 2: Install Required Software

### 1. Install Python and Dependencies

```bash
sudo apt install python3.11 python3.11-venv python3-pip python3-dev -y
sudo apt install libpq-dev nginx curl git -y
```

### 2. Install PostgreSQL (Optional but Recommended)

```bash
sudo apt install postgresql postgresql-contrib -y
```

### 3. Configure PostgreSQL

```bash
sudo -u postgres psql

# In PostgreSQL prompt:
CREATE DATABASE dtb_website;
CREATE USER dtbuser WITH PASSWORD 'your_secure_password';
ALTER ROLE dtbuser SET client_encoding TO 'utf8';
ALTER ROLE dtbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE dtbuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dtb_website TO dtbuser;
\q
```

## 📦 Step 3: Deploy Your Application

### 1. Clone Your Repository

```bash
cd /home/dtbadmin
git clone <your-repository-url> dtb-site
cd dtb-site/DTB-website/DTB_website
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2-binary  # If using PostgreSQL
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
nano .env
```

Add:
```
DJANGO_SECRET_KEY=your-generated-secret-key
DJANGO_SETTINGS_MODULE=DTB_website.settings_production
DOMAIN_NAME=yourdomain.com
DATABASE_URL=postgresql://dtbuser:your_secure_password@localhost:5432/dtb_website
```

### 5. Update Production Settings for PostgreSQL

Edit `DTB_website/settings_production.py`:

```python
import dj_database_url

# Replace DATABASES section with:
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://dtbuser:password@localhost:5432/dtb_website',
        conn_max_age=600
    )
}
```

Install dj-database-url:
```bash
pip install dj-database-url
```

### 6. Run Migrations and Collect Static Files

```bash
python manage.py migrate --settings=DTB_website.settings_production
python manage.py collectstatic --noinput --settings=DTB_website.settings_production
python manage.py createsuperuser --settings=DTB_website.settings_production
```

### 7. Test Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 DTB_website.wsgi
```

Visit `http://your_server_ip:8000` to verify. Press Ctrl+C to stop.

## 🔄 Step 4: Configure Gunicorn with Supervisor

### 1. Create Gunicorn Systemd Service

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=gunicorn daemon for DTB Website
After=network.target

[Service]
User=dtbadmin
Group=www-data
WorkingDirectory=/home/dtbadmin/dtb-site/DTB-website/DTB_website
Environment="PATH=/home/dtbadmin/dtb-site/DTB-website/DTB_website/venv/bin"
Environment="DJANGO_SETTINGS_MODULE=DTB_website.settings_production"
EnvironmentFile=/home/dtbadmin/dtb-site/DTB-website/DTB_website/.env
ExecStart=/home/dtbadmin/dtb-site/DTB-website/DTB_website/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/dtbadmin/dtb-site/DTB-website/DTB_website/gunicorn.sock \
          DTB_website.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 2. Start and Enable Gunicorn

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

## 🌐 Step 5: Configure Nginx

### 1. Create Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/dtb_website
```

Add:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/dtbadmin/dtb-site/DTB-website/DTB_website/staticfiles/;
    }

    location /media/ {
        alias /home/dtbadmin/dtb-site/DTB-website/DTB_website/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/dtbadmin/dtb-site/DTB-website/DTB_website/gunicorn.sock;
    }
}
```

### 2. Enable the Site

```bash
sudo ln -s /etc/nginx/sites-available/dtb_website /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 Step 6: Set Up SSL with Let's Encrypt

### 1. Install Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Obtain SSL Certificate

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Follow the prompts. Certbot will automatically configure Nginx for HTTPS.

### 3. Test Auto-Renewal

```bash
sudo certbot renew --dry-run
```

## ✅ Step 7: Final Checks

### 1. Set Proper Permissions

```bash
sudo chown -R dtbadmin:www-data /home/dtbadmin/dtb-site
sudo chmod -R 755 /home/dtbadmin/dtb-site
```

### 2. Restart All Services

```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

### 3. Test Your Site

Visit `https://yourdomain.com` and verify:
- [ ] Homepage loads
- [ ] Static files (CSS, images) load
- [ ] Admin panel works (`/admin`)
- [ ] User authentication works
- [ ] File uploads work

## 🔧 Maintenance Commands

### Update Your Application

```bash
cd /home/dtbadmin/dtb-site/DTB-website/DTB_website
source venv/bin/activate
git pull origin main
pip install -r requirements.txt
python manage.py migrate --settings=DTB_website.settings_production
python manage.py collectstatic --noinput --settings=DTB_website.settings_production
sudo systemctl restart gunicorn
```

### View Logs

```bash
# Gunicorn logs
sudo journalctl -u gunicorn -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### Restart Services

```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

## 🔐 Security Hardening

1. **Set up automatic security updates**
   ```bash
   sudo apt install unattended-upgrades
   sudo dpkg-reconfigure --priority=low unattended-upgrades
   ```

2. **Configure fail2ban**
   ```bash
   sudo apt install fail2ban
   sudo systemctl enable fail2ban
   ```

3. **Regular backups**
   ```bash
   # Database backup
   pg_dump dtb_website > backup_$(date +%Y%m%d).sql
   
   # Media files backup
   tar -czf media_backup_$(date +%Y%m%d).tar.gz media/
   ```

## 🎉 Success!

Your Django application is now deployed on a VPS with:
- ✅ HTTPS enabled
- ✅ Automatic SSL renewal
- ✅ Process management
- ✅ Reverse proxy
- ✅ Production-ready database

---

**Need Help?**
- Nginx docs: [nginx.org/en/docs](https://nginx.org/en/docs/)
- Gunicorn docs: [docs.gunicorn.org](https://docs.gunicorn.org/)
- Django deployment: [docs.djangoproject.com/en/stable/howto/deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)

