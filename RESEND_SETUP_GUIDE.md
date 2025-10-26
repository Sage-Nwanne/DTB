# Resend Email Setup Guide

## ✅ What's Been Configured

Your DTB website is now set up to send emails via **Resend** - a modern email service perfect for developers.

### Features:
- ✅ Sends confirmation emails to clients with PDF attachments
- ✅ Sends internal notifications to your Zoho email
- ✅ Professional email templates with your branding
- ✅ Automatic PDF attachment handling
- ✅ Easy integration with Heroku

---

## 🚀 Getting Started with Resend

### Step 1: Create a Resend Account

1. Go to https://resend.com
2. Sign up with your email
3. Verify your email address

### Step 2: Get Your API Key

1. Log in to Resend dashboard
2. Go to **API Keys** section
3. Create a new API key
4. Copy the key (starts with `re_`)

### Step 3: Verify Your Domain

For production, you need to verify your domain:

1. In Resend dashboard, go to **Domains**
2. Add your domain: `dtbsolutions.tech`
3. Follow the DNS verification steps
4. Add the CNAME records to your domain provider

**For Development (Testing):**
- You can use the default `onboarding@resend.dev` domain
- This is perfect for testing before going live

### Step 4: Set Environment Variable (Local Development)

**On Mac/Linux:**
```bash
export RESEND_API_KEY=re_your_api_key_here
python manage.py runserver
```

**On Windows (Command Prompt):**
```cmd
set RESEND_API_KEY=re_your_api_key_here
python manage.py runserver
```

**On Windows (PowerShell):**
```powershell
$env:RESEND_API_KEY="re_your_api_key_here"
python manage.py runserver
```

### Step 5: Test Locally

1. Go to http://127.0.0.1:8000/contact
2. Fill out and submit the form
3. Check your email inbox (and spam folder)
4. You should receive the confirmation email with PDFs attached

---

## 📧 Email Configuration

### Sender Email
- **From:** `inquire@dtbsolutions.tech` (via Resend)
- **To Client:** Their email address
- **To Team:** `inquire@dtbsolutions.tech` (your Zoho email)

### Email Templates
Located in `main_app/templates/emails/`:
- `contact_confirmation.html` - Client confirmation email
- `internal_notification.html` - Internal team notification

### PDF Attachments
Automatically attached from:
- `main_app/static/documents/contracts/service_agreement.pdf`
- `main_app/static/documents/intake_scope/intake_and_scope_template.pdf`
- `main_app/static/documents/sop/standard_operating_procedures.pdf`

---

## 🌐 Production Deployment (Heroku)

### Step 1: Set Heroku Config Variable

```bash
heroku config:set RESEND_API_KEY=re_your_api_key_here
```

### Step 2: Verify Domain in Resend

1. In Resend dashboard, add your domain
2. Add the DNS records to your domain provider
3. Wait for verification (usually 5-10 minutes)

### Step 3: Deploy

```bash
git add .
git commit -m "Configure Resend email service"
git push heroku main
```

### Step 4: Test on Production

1. Go to your live site: https://dtbsolutions.tech/contact
2. Submit the form
3. Check your email

---

## 💰 Resend Pricing

- **Free Tier:** 100 emails/day
- **Paid Plans:** Starting at $20/month for unlimited emails
- **Perfect for:** Startups and small businesses

---

## 🔧 Troubleshooting

### Email not sending?

**Check 1: API Key**
```bash
echo $RESEND_API_KEY
```
Make sure it's set and starts with `re_`

**Check 2: Domain Verification**
- For production, your domain must be verified in Resend
- For testing, use the default `onboarding@resend.dev` domain

**Check 3: Logs**
- Check Django console for error messages
- Check Resend dashboard for failed emails

**Check 4: PDF Files**
- Verify PDFs exist in the correct folders
- Check file permissions

### Emails going to spam?

1. Verify your domain in Resend (adds SPF/DKIM records)
2. Use a professional domain (not Gmail)
3. Keep email content professional
4. Avoid spam trigger words

---

## 📊 Monitoring Emails

### In Resend Dashboard:
1. View all sent emails
2. Check delivery status
3. See bounce/complaint rates
4. Monitor API usage

### In Django Admin:
1. Go to `/admin/main_app/contactsubmission/`
2. View all contact submissions
3. See timestamps and details

---

## 🔐 Security Best Practices

✅ **DO:**
- Store API key in environment variables
- Never commit API key to git
- Use HTTPS for your website
- Verify your domain for production

❌ **DON'T:**
- Share your API key
- Commit API key to repository
- Use test API key in production
- Send emails to unverified addresses

---

## 📝 Email Customization

### Modify Email Templates:

**Client Email:** `main_app/templates/emails/contact_confirmation.html`
- Change colors, fonts, messaging
- Add your logo
- Customize the CTA button

**Internal Email:** `main_app/templates/emails/internal_notification.html`
- Customize notification format
- Add additional fields
- Change styling

### Modify Email Logic:

**File:** `main_app/email_utils.py`
- Add more attachments
- Change email recipients
- Add custom headers
- Modify subject lines

---

## 🚀 Next Steps

1. ✅ Create Resend account
2. ✅ Get API key
3. ✅ Set environment variable
4. ✅ Test locally
5. ✅ Verify domain (for production)
6. ✅ Deploy to Heroku
7. ✅ Test on production

---

## 📞 Support

- **Resend Docs:** https://resend.com/docs
- **Resend Support:** https://resend.com/support
- **Django Email:** https://docs.djangoproject.com/en/5.2/topics/email/

---

## Quick Reference

```bash
# Local development
export RESEND_API_KEY=re_your_key
python manage.py runserver

# Heroku production
heroku config:set RESEND_API_KEY=re_your_key
git push heroku main

# Check if key is set
echo $RESEND_API_KEY
```

