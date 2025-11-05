# 🚀 Deploy to Heroku - Resend Email Edition

**Status:** ✅ Code is ready! All changes committed to GitHub.

---

## 📋 Quick Deployment (7 Commands)

### Command 1: Install Heroku CLI

**Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

**Windows:** Download from https://devcenter.heroku.com/articles/heroku-cli

---

### Command 2: Login to Heroku

```bash
heroku login
```

*(Browser will open for authentication)*

---

### Command 3: Navigate to Project

```bash
cd /home/sage_nwanne/personal-work/DTB
```

---

### Command 4: Add Heroku Remote

```bash
heroku git:remote -a dtbsolutions
```

**⚠️ Replace `dtbsolutions` with your actual Heroku app name!**

---

### Command 5: Set Resend API Key

```bash
heroku config:set RESEND_API_KEY=re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b
```

---

### Command 6: Deploy to Heroku

```bash
git push heroku main
```

*(Wait 2-5 minutes for deployment)*

---

### Command 7: Verify Deployment

```bash
heroku logs --tail
```

*(Press Ctrl+C to exit)*

---

## ✅ Test Email Functionality

1. **Go to contact form:**
   ```
   https://dtbsolutions.tech/contact
   ```

2. **Fill out and submit form**

3. **Check your email** for confirmation

4. **Check admin panel:**
   ```
   https://dtbsolutions.tech/admin/main_app/contactsubmission/
   ```

---

## 🔍 Verify API Key is Set

```bash
heroku config:get RESEND_API_KEY
```

Should return: `re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b`

---

## 📧 Email Configuration

| Setting | Value |
|---------|-------|
| **Service** | Resend |
| **From Email** | inquire@dtbsolutions.tech |
| **API Key** | re_QQLs6gvV_DaVKDQfkFGuSyUuSXxqg7X6b |
| **Client Email** | Confirmation message |
| **Team Email** | Internal notification |

---

## 🐛 Troubleshooting

### Email not sending?
```bash
heroku logs --tail
```
Look for Resend API errors

### App won't start?
```bash
heroku logs --tail
```
Look for Python/Django errors

### Need to redeploy?
```bash
git push heroku main
```

---

## 📞 Useful Commands

```bash
# View logs
heroku logs --tail

# View config variables
heroku config

# Restart app
heroku restart

# Check app status
heroku ps

# Open app in browser
heroku open
```

---

## ✅ Deployment Checklist

- [ ] Install Heroku CLI
- [ ] Login to Heroku
- [ ] Add Heroku remote
- [ ] Set Resend API key
- [ ] Deploy to Heroku
- [ ] Verify deployment
- [ ] Test contact form
- [ ] Check email delivery
- [ ] Verify admin panel

---

## 🎉 You're Ready!

All code is committed and ready. Just run the 7 commands above to deploy!

**Questions?** See:
- `HEROKU_DEPLOYMENT_STEPS.md` - Detailed guide
- `DEPLOYMENT_READY.md` - Overview
- `RESEND_QUICK_REFERENCE.md` - Quick reference

---

**Let's go live! 🚀**

