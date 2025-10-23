# 🚀 Deployment Checklist - DTB Website

## ✅ Pre-Deployment Checklist

### **Code Quality**
- [ ] All pages tested locally
- [ ] No console errors
- [ ] No 404 errors (except favicon)
- [ ] All links working
- [ ] Responsive design verified
- [ ] Performance acceptable

### **Git & GitHub**
- [ ] All changes committed
- [ ] Commit message descriptive
- [ ] Code pushed to GitHub
- [ ] Repository is public
- [ ] Branch is main

### **Environment Setup**
- [ ] `.env` file created with:
  - [ ] `DJANGO_SECRET_KEY` (new key generated)
  - [ ] `DEBUG = False`
  - [ ] `ALLOWED_HOSTS` set
  - [ ] `DOMAIN_NAME` set to your domain

### **Django Settings**
- [ ] `DEBUG = False` in production settings
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] `STATIC_ROOT` configured
- [ ] `MEDIA_ROOT` configured
- [ ] Database configured for production

### **Static Files**
- [ ] Run `python manage.py collectstatic`
- [ ] Verify CSS files compiled
- [ ] Verify images copied
- [ ] Verify fonts loaded

### **Database**
- [ ] Migrations run locally
- [ ] Database clean
- [ ] No test data in production

---

## 🚀 **Deployment Steps (Railway)**

### **Step 1: Create Railway Account**
- [ ] Go to https://railway.app
- [ ] Sign up with GitHub
- [ ] Authorize Railway

### **Step 2: Create New Project**
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Choose `Sage-Nwanne/DTB` repository
- [ ] Select main branch

### **Step 3: Configure Environment**
- [ ] Add environment variables:
  - [ ] `DJANGO_SECRET_KEY` (generate new)
  - [ ] `DJANGO_SETTINGS_MODULE=config.settings_production`
  - [ ] `DOMAIN_NAME=yourdomain.com`
  - [ ] `DEBUG=False`
  - [ ] `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`

### **Step 4: Add PostgreSQL Database**
- [ ] Click "Add Service"
- [ ] Select "PostgreSQL"
- [ ] Railway auto-configures `DATABASE_URL`

### **Step 5: Deploy**
- [ ] Click "Deploy"
- [ ] Wait for build to complete
- [ ] Check deployment logs
- [ ] Verify no errors

### **Step 6: Run Migrations**
- [ ] In Railway dashboard, open terminal
- [ ] Run: `python manage.py migrate`
- [ ] Run: `python manage.py collectstatic --noinput`

### **Step 7: Create Superuser (Optional)**
- [ ] Run: `python manage.py createsuperuser`
- [ ] Enter username, email, password

### **Step 8: Add Custom Domain**
- [ ] In Railway dashboard, go to Settings
- [ ] Click "Domains"
- [ ] Add custom domain: `yourdomain.com`
- [ ] Copy CNAME record

---

## 🌐 **Connect Squarespace Domain**

### **Step 1: Get CNAME Record**
- [ ] From Railway dashboard
- [ ] Copy the CNAME value
- [ ] Example: `yourdomain.railway.app`

### **Step 2: Update Squarespace DNS**
- [ ] Log in to Squarespace
- [ ] Go to Settings → Domains
- [ ] Select your domain
- [ ] Click "DNS Settings"
- [ ] Add CNAME records:
  ```
  Host: www
  Type: CNAME
  Data: yourdomain.railway.app
  
  Host: @
  Type: CNAME
  Data: yourdomain.railway.app
  ```

### **Step 3: Wait for DNS Propagation**
- [ ] DNS can take 1-48 hours
- [ ] Check status at https://whatsmydns.net
- [ ] Enter your domain
- [ ] Wait for all servers to show new IP

### **Step 4: Verify Connection**
- [ ] Visit `https://yourdomain.com`
- [ ] Verify site loads
- [ ] Check SSL certificate (should be automatic)
- [ ] Test all pages

---

## ✅ **Post-Deployment Checklist**

### **Functionality**
- [ ] Homepage loads
- [ ] All pages accessible
- [ ] Navigation works
- [ ] Links work
- [ ] Images load
- [ ] CSS loads
- [ ] No console errors

### **Performance**
- [ ] Page load time acceptable
- [ ] Images optimized
- [ ] CSS minified
- [ ] No 404 errors

### **Security**
- [ ] HTTPS enabled
- [ ] SSL certificate valid
- [ ] No sensitive data in code
- [ ] Environment variables secure

### **SEO**
- [ ] Meta tags present
- [ ] Title tags correct
- [ ] Descriptions present
- [ ] Robots.txt configured
- [ ] Sitemap.xml present

### **Monitoring**
- [ ] Set up error tracking
- [ ] Monitor performance
- [ ] Check logs regularly
- [ ] Set up alerts

---

## 🎯 **Testing After Deployment**

### **Desktop Testing**
- [ ] Test on Chrome
- [ ] Test on Firefox
- [ ] Test on Safari
- [ ] Test on Edge

### **Mobile Testing**
- [ ] Test on iPhone
- [ ] Test on Android
- [ ] Test on tablet
- [ ] Verify responsive

### **Functionality Testing**
- [ ] Click all links
- [ ] Test contact form
- [ ] Test portfolio filter
- [ ] Verify all pages load

---

## 📊 **Deployment Summary**

**Estimated Time**: 30-45 minutes

**Steps**:
1. Create Railway account (5 min)
2. Deploy from GitHub (10 min)
3. Configure environment (5 min)
4. Add database (5 min)
5. Run migrations (5 min)
6. Connect domain (5 min)
7. Wait for DNS (varies)
8. Test (5 min)

---

## 🎉 **You're Live!**

Once DNS propagates, your website will be live at:
- `https://yourdomain.com`
- `https://www.yourdomain.com`

---

## 📞 **Troubleshooting**

### **Site not loading?**
- Check Railway deployment logs
- Verify environment variables
- Check DNS propagation
- Verify domain in ALLOWED_HOSTS

### **CSS not loading?**
- Run `collectstatic` again
- Check static files configuration
- Verify WhiteNoise middleware

### **Database errors?**
- Check DATABASE_URL environment variable
- Run migrations again
- Check database connection

### **SSL certificate issues?**
- Railway auto-provisions SSL
- May take 5-10 minutes
- Check Railway dashboard

---

**Status**: Ready to deploy ✅

**Next**: Follow the deployment steps above!

