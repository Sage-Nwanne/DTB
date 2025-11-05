# Email Configuration Guide

## Current Status

✅ **Development Mode**: Emails print to console (for testing)
❌ **Production Mode**: Emails not yet configured

## How to Enable Real Email Sending

### Option 1: Gmail (Recommended for Testing)

#### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification

#### Step 2: Create App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer" (or your device)
3. Google will generate a 16-character password
4. Copy this password

#### Step 3: Set Environment Variables

**On Mac/Linux:**
```bash
export EMAIL_BACKEND=smtp
export EMAIL_HOST=smtp.gmail.com
export EMAIL_PORT=587
export EMAIL_USE_TLS=True
export EMAIL_HOST_USER=your-email@gmail.com
export EMAIL_HOST_PASSWORD=your-16-char-app-password
```

**On Windows (Command Prompt):**
```cmd
set EMAIL_BACKEND=smtp
set EMAIL_HOST=smtp.gmail.com
set EMAIL_PORT=587
set EMAIL_USE_TLS=True
set EMAIL_HOST_USER=your-email@gmail.com
set EMAIL_HOST_PASSWORD=your-16-char-app-password
```

#### Step 4: Restart Django Server
```bash
python manage.py runserver
```

#### Step 5: Test
1. Go to `/contact`
2. Submit the form
3. Check your email inbox (and spam folder)

---

### Option 2: SendGrid (Best for Production)

#### Step 1: Create SendGrid Account
1. Sign up at https://sendgrid.com
2. Create an API key

#### Step 2: Install Package
```bash
pip install sendgrid-django
```

#### Step 3: Update settings.py
```python
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
```

#### Step 4: Set Environment Variable
```bash
export SENDGRID_API_KEY=your-api-key
```

---

### Option 3: AWS SES (Enterprise)

#### Step 1: Create AWS Account
1. Set up AWS SES in your region
2. Verify your email address

#### Step 2: Install Package
```bash
pip install django-ses
```

#### Step 3: Update settings.py
```python
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
```

---

## For Heroku Deployment

### Step 1: Set Config Variables
```bash
heroku config:set EMAIL_BACKEND=smtp
heroku config:set EMAIL_HOST=smtp.gmail.com
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_USE_TLS=True
heroku config:set EMAIL_HOST_USER=your-email@gmail.com
heroku config:set EMAIL_HOST_PASSWORD=your-app-password
```

### Step 2: Deploy
```bash
git add .
git commit -m "Configure email for production"
git push heroku main
```

### Step 3: Test
Submit the contact form on your live site and check your email.

---

## Troubleshooting

### Emails not sending?

**Check 1: Environment Variables**
```bash
# Verify variables are set
echo $EMAIL_BACKEND
echo $EMAIL_HOST_USER
```

**Check 2: Gmail App Password**
- Make sure you used the 16-character app password, not your regular password
- Make sure 2FA is enabled

**Check 3: Firewall/Network**
- Some networks block SMTP port 587
- Try port 465 with SSL instead

**Check 4: Django Logs**
- Check for error messages in console output
- Look for "SMTPAuthenticationError" or similar

### Still not working?

1. Verify email credentials are correct
2. Check that the email account allows "Less secure apps" (Gmail)
3. Try sending a test email from Python directly:

```python
from django.core.mail import send_mail

send_mail(
    'Test Subject',
    'Test message',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

---

## Email Limits

- **Gmail**: 500 emails/day
- **SendGrid**: Depends on plan (free tier: 100/day)
- **AWS SES**: 50,000 emails/day (sandbox mode: 1 email/second)

For high volume, use SendGrid or AWS SES.

---

## Security Best Practices

✅ **DO:**
- Store credentials in environment variables
- Use app-specific passwords (not your main password)
- Enable 2FA on email account
- Use TLS/SSL encryption

❌ **DON'T:**
- Commit credentials to git
- Use your main email password
- Disable TLS
- Share API keys

---

## Next Steps

1. Choose your email provider (Gmail recommended for testing)
2. Follow the setup steps above
3. Set environment variables
4. Restart Django
5. Test the contact form
6. Verify email arrives in your inbox

