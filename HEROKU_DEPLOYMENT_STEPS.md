# Heroku Deployment Steps - Complete Guide

## ✅ What's Been Done

Your code has been committed and pushed to GitHub main branch with all Resend email configuration ready for production.

**Commit:** `e7d7812` - "Configure Resend email service for production"

---

## 🚀 Deploy to Heroku (Step-by-Step)

### Step 1: Install Heroku CLI

**On Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**On Linux (Ubuntu/Debian):**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

**On Windows:**
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku

```bash
heroku login
```

This will open a browser to authenticate. Log in with your Heroku account.

### Step 3: Add Heroku Remote

```bash
cd /home/sage_nwanne/personal-work/DTB
heroku git:remote -a dtbsolutions
```

Replace `dtbsolutions` with your actual Heroku app name.

**Verify it worked:**
```bash
git remote -v
```

You should see:
```
heroku  https://git.heroku.com/dtbsolutions.git (fetch)
heroku  https://git.heroku.com/dtbsolutions.git (push)
origin  https://github.com/Sage-Nwanne/DTB-website.git (fetch)
origin  https://github.com/Sage-Nwanne/DTB-website.git (push)
```

### Step 4: Set Environment Variable

```bash
heroku config:set RESEND_API_KEY=re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b
```

**Verify it was set:**
```bash
heroku config:get RESEND_API_KEY
```

Should return: `re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b`

### Step 5: Deploy to Heroku

```bash
git push heroku main
```

This will:
- Build your app
- Install dependencies
- Run migrations
- Deploy to production

### Step 6: Verify Deployment

```bash
heroku logs --tail
```

Look for:
- ✅ `Starting development server` or similar
- ✅ No error messages
- ✅ App is running

### Step 7: Test Email Functionality

1. Go to your production site: `https://dtbsolutions.tech/contact`
2. Fill out the contact form
3. Submit it
4. Check your email inbox for confirmation
5. Check `inquire@dtbsolutions.tech` for internal notification

---

## 📋 Deployment Checklist

- [ ] Install Heroku CLI
- [ ] Login to Heroku (`heroku login`)
- [ ] Add Heroku remote (`heroku git:remote -a dtbsolutions`)
- [ ] Set API key (`heroku config:set RESEND_API_KEY=...`)
- [ ] Deploy (`git push heroku main`)
- [ ] Check logs (`heroku logs --tail`)
- [ ] Test contact form on production
- [ ] Verify emails are being sent
- [ ] Check admin panel for submissions

---

## 🔍 Troubleshooting

### "heroku: command not found"
- Install Heroku CLI (see Step 1 above)
- Restart your terminal after installation

### "fatal: 'heroku' does not appear to be a 'git' remote"
- Run: `heroku git:remote -a dtbsolutions`
- Replace `dtbsolutions` with your app name

### "API key is invalid" error
- Verify API key is set: `heroku config:get RESEND_API_KEY`
- Check it matches: `re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b`
- Redeploy: `git push heroku main`

### Emails not sending
- Check logs: `heroku logs --tail`
- Verify API key is set
- Check Resend dashboard for errors
- Verify domain is verified in Resend

### App won't start
- Check logs: `heroku logs --tail`
- Look for Python/Django errors
- Check database migrations ran
- Verify all dependencies installed

---

## 📊 Useful Heroku Commands

```bash
# View logs
heroku logs --tail

# View config variables
heroku config

# Set a config variable
heroku config:set KEY=value

# Get a specific config variable
heroku config:get RESEND_API_KEY

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Restart app
heroku restart

# View app info
heroku apps:info

# Open app in browser
heroku open

# View running processes
heroku ps
```

---

## 🎯 Your Heroku App Details

- **App Name:** dtbsolutions (or your custom name)
- **Domain:** https://dtbsolutions.tech
- **Git Remote:** heroku
- **Environment Variable:** RESEND_API_KEY

---

## 📧 Email Configuration (Production)

- **From:** inquire@dtbsolutions.tech
- **Service:** Resend
- **API Key:** re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b
- **Email Type:** Transactional confirmations

---

## ✅ After Deployment

1. **Test the contact form** on production
2. **Verify emails arrive** in your inbox
3. **Check admin panel** for submissions
4. **Monitor logs** for any errors
5. **Set up monitoring** (optional)

---

## 🔐 Security Notes

✅ API key is stored in Heroku environment variables (not in code)
✅ Never commit API key to git
✅ Use different keys for development and production (optional)
✅ Rotate API key periodically

---

## 📞 Support

- **Heroku Docs:** https://devcenter.heroku.com/
- **Resend Docs:** https://resend.com/docs
- **Django Docs:** https://docs.djangoproject.com/

---

## 🚀 Next Steps

1. Install Heroku CLI
2. Login to Heroku
3. Add Heroku remote
4. Set environment variable
5. Deploy to Heroku
6. Test email functionality
7. Monitor logs

You're ready to go live! 🎉

