# DTB Client Documents

This folder contains PDF templates that are automatically sent to clients when they submit the contact form.

## Folder Structure

```
documents/
├── contracts/
│   └── service_agreement.pdf          # Your service agreement/contract
├── intake_scope/
│   └── intake_and_scope_template.pdf  # Client intake & scope form
└── sop/
    └── standard_operating_procedures.pdf  # Your SOP documentation
```

## How It Works

When a client submits the contact form:

1. ✅ They receive a confirmation email immediately
2. ✅ All three PDF documents are automatically attached to their email
3. ✅ Your team receives an internal notification with their submission details
4. ✅ The submission is saved in the Django admin for your records

## Adding Your Documents

### Step 1: Prepare Your PDFs
- Create or export your documents as PDF files
- Recommended file sizes: 1-5 MB each
- Ensure they're properly formatted and professional

### Step 2: Upload to Correct Folders
- **Service Agreement**: `contracts/service_agreement.pdf`
- **Intake & Scope**: `intake_scope/intake_and_scope_template.pdf`
- **SOP**: `sop/standard_operating_procedures.pdf`

### Step 3: Test
- Submit the contact form on your website
- Check that emails are being sent (console output in development)
- Verify PDFs are attached

## Email Configuration

### Development (Current)
Emails print to console. Check your terminal output when testing.

### Production Setup
Update `config/settings.py` with your email provider:

```python
# Example: SendGrid
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = 'your-api-key'

# Example: Gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## Viewing Submissions

All contact form submissions are saved in the Django admin:
- URL: `/admin/main_app/contactsubmission/`
- You can view, search, and filter all submissions
- Export data for follow-up

## Email Templates

The confirmation emails are customized in:
- `main_app/templates/emails/contact_confirmation.html` - Client email
- `main_app/templates/emails/internal_notification.html` - Internal team email

Feel free to customize these templates to match your branding!

## Troubleshooting

**PDFs not attaching?**
- Verify file paths are correct
- Check file permissions
- Ensure PDF files exist in the correct folders

**Emails not sending?**
- In development, check console output
- In production, verify email credentials in settings.py
- Check spam/junk folders

**Need help?**
- Check Django email documentation: https://docs.djangoproject.com/en/5.2/topics/email/

