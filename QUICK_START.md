# 🚀 DTB Website - Quick Start Guide


## ⚡ Quick Start (5 Minutes)

### Option 1: Automated Setup (Recommended)

```bash
cd DTB-site
./setup_local.sh
```

That's it! The script will:
- Create virtual environment
- Install dependencies
- Run migrations
- Collect static files
- Prompt to create superuser

### Option 2: Manual Setup

```bash
# 1. Navigate to project
cd DTB-site

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Collect static files
python manage.py collectstatic

# 8. Run server
python manage.py runserver
```

### Access Your Site

- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🌐 Deploy to Production (Choose One)

### 🥇 Railway (Easiest - Recommended)

**Time**: ~10 minutes

1. Push code to GitHub
2. Sign up at [railway.app](https://railway.app)
3. Click "Deploy from GitHub"
4. Add environment variables
5. Add custom domain
6. Update Squarespace DNS

**Full Guide**: See `DEPLOYMENT_PAAS.md` → Railway section

**Note**: Update environment variable to `DJANGO_SETTINGS_MODULE=config.settings_production`

---

### 🥈 Render (Free Tier Available)

**Time**: ~15 minutes

1. Push code to GitHub
2. Sign up at [render.com](https://render.com)
3. Create new Web Service
4. Configure build/start commands
5. Add environment variables
6. Add custom domain
7. Update Squarespace DNS

**Full Guide**: See `DEPLOYMENT_PAAS.md` → Render section

---

### 🥉 VPS (Full Control)

**Time**: ~45 minutes

1. Get a VPS (DigitalOcean, Linode, etc.)
2. SSH into server
3. Install dependencies
4. Configure Nginx + Gunicorn
5. Set up SSL with Let's Encrypt
6. Update Squarespace DNS

**Full Guide**: See `DEPLOYMENT_VPS.md`

---

## 🔗 Connect Squarespace Domain

After deploying to any platform:

### 1. Get Your Server Info

- **Railway/Render**: Your app URL (e.g., `your-app.railway.app`)
- **VPS**: Your server IP address

### 2. Update Squarespace DNS

1. Log in to Squarespace
2. Go to **Settings** → **Domains** → **Your Domain** → **DNS Settings**
3. Add records:

**For Railway/Render (CNAME):**
```
Type: CNAME | Host: www | Data: your-app.railway.app
Type: CNAME | Host: @   | Data: your-app.railway.app
```

**For VPS (A Record):**
```
Type: A | Host: www | Data: Your.Server.IP
Type: A | Host: @   | Data: Your.Server.IP
```

### 3. Add Domain to Hosting Platform

- **Railway**: Settings → Domains → Add Custom Domain
- **Render**: Settings → Custom Domains → Add
- **VPS**: Already configured in Nginx

### 4. Wait for DNS Propagation

- Usually takes 1-4 hours
- Can take up to 48 hours
- Check status: [whatsmydns.net](https://www.whatsmydns.net)

**Full Guide**: See `DEPLOYMENT_SQUARESPACE.md`

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| `README.md` | Main documentation, local setup |
| `DEPLOYMENT_SQUARESPACE.md` | Connect Squarespace domain (START HERE) |
| `DEPLOYMENT_PAAS.md` | Deploy to Railway/Render/Heroku |
| `DEPLOYMENT_VPS.md` | Deploy to VPS (advanced) |
| `CLEANUP_VERIFICATION.md` | What was cleaned and why |
| `QUICK_START.md` | This file - quick reference |

---

## 🔐 Important Security Notes

### Before Deploying:

1. **Generate New Secret Key**
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **Update Environment Variables**
   - Copy `.env.example` to `.env`
   - Add your secret key
   - Add your domain name

3. **Change Developer Passwords**
   - Edit `main_app/auth_backends.py`
   - Update hardcoded passwords
   - Or move to environment variables

4. **Review Settings**
   - Check `settings_production.py`
   - Ensure `DEBUG = False`
   - Verify `ALLOWED_HOSTS`

---

## 🎯 Recommended Deployment Path

For your Squarespace domain, we recommend:

### **Railway** (Best for DTB Website)

**Why?**
- ✅ Easiest setup (10 minutes)
- ✅ Automatic SSL certificates
- ✅ GitHub auto-deploy
- ✅ Built-in PostgreSQL
- ✅ $5 free credit/month
- ✅ Perfect for small teams

**Steps:**
1. Read `DEPLOYMENT_PAAS.md` (Railway section)
2. Push code to GitHub
3. Deploy on Railway
4. Follow `DEPLOYMENT_SQUARESPACE.md` for DNS
5. Done! ✨

---

## 🆘 Troubleshooting

### Local Development Issues

**Virtual environment not activating?**
```bash
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**Dependencies not installing?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Database errors?**
```bash
python manage.py migrate
```

### Deployment Issues

**Static files not loading?**
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` in settings

**400 Bad Request?**
- Update `ALLOWED_HOSTS` in settings
- Set `DOMAIN_NAME` environment variable

**DNS not resolving?**
- Wait longer (can take hours)
- Check DNS records at [whatsmydns.net](https://www.whatsmydns.net)
- Verify records in Squarespace

---

## 📞 Need Help?

1. **Check the guides**: Most issues are covered in the deployment guides
2. **Review logs**: Check your hosting platform's logs
3. **Verify settings**: Double-check environment variables
4. **DNS issues**: Use [whatsmydns.net](https://www.whatsmydns.net) to check propagation

---

## ✅ Deployment Checklist

### Pre-Deployment
- [ ] Code pushed to GitHub
- [ ] New secret key generated
- [ ] Environment variables prepared
- [ ] Developer passwords updated

### Deployment
- [ ] Platform chosen (Railway/Render/VPS)
- [ ] App deployed successfully
- [ ] Environment variables set
- [ ] Database migrated
- [ ] Static files collected
- [ ] Superuser created

### Domain Connection
- [ ] DNS records added in Squarespace
- [ ] Custom domain added to hosting platform
- [ ] SSL certificate provisioned
- [ ] DNS propagation complete

### Testing
- [ ] Homepage loads
- [ ] Static files (CSS/images) work
- [ ] Admin panel accessible
- [ ] User authentication works
- [ ] File uploads work
- [ ] HTTPS enabled

---

## 🎉 You're Ready!

Your DTB website is:
- ✅ Clean (no redundant code)
- ✅ Documented (comprehensive guides)
- ✅ Configured (deployment files ready)
- ✅ Secure (production settings)

**Next Step**: Choose your deployment platform and follow the guide!

**Recommended**: Start with Railway + Squarespace DNS (easiest path)

---

**Good luck with your deployment! 🚀**

*Built with ❤️ by the DTB Team*

