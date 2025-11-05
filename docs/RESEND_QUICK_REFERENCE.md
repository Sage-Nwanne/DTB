# Resend Email - Quick Reference Card

## 🚀 Get Started in 5 Minutes

### 1. Create Resend Account
```
https://resend.com → Sign up → Verify email
```

### 2. Get API Key
```
Dashboard → API Keys → Create new key
Copy: re_xxxxxxxxxxxxxxxx
```

### 3. Set Environment Variable
```bash
# Mac/Linux
export RESEND_API_KEY=re_your_key_here

# Windows CMD
set RESEND_API_KEY=re_your_key_here

# Windows PowerShell
$env:RESEND_API_KEY="re_your_key_here"
```

### 4. Test Locally
```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/contact
# Submit form
# Check email
```

### 5. Deploy to Heroku
```bash
heroku config:set RESEND_API_KEY=re_your_key_here
git push heroku main
```

---

## 📧 Email Details

| Item | Value |
|------|-------|
| **From** | inquire@dtbsolutions.tech |
| **To Client** | Their email address |
| **To Team** | inquire@dtbsolutions.tech |
| **Service** | Resend |
| **Attachments** | 3 PDFs (auto-attached) |

---

## 📁 Important Folders

```
main_app/static/documents/
├── contracts/
│   └── service_agreement.pdf
├── intake_scope/
│   └── intake_and_scope_template.pdf
└── sop/
    └── standard_operating_procedures.pdf
```

**Add your PDFs here!**

---

## 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `config/settings.py` | Resend API key config |
| `main_app/email_utils.py` | Email sending logic |
| `main_app/forms.py` | Contact form |
| `main_app/views.py` | Form handling |
| `main_app/models.py` | ContactSubmission model |

---

## 📊 Admin Panel

```
URL: /admin/main_app/contactsubmission/
- View all submissions
- Search by name/email
- Filter by service/budget/date
- Export data
```

---

## 🐛 Debugging

### Check API Key
```bash
echo $RESEND_API_KEY
```

### Check Logs
```bash
# Local: Check console output
# Heroku: heroku logs --tail
```

### Test Email Sending
```python
# In Django shell
from main_app.email_utils import send_contact_confirmation_email
from main_app.models import ContactSubmission

submission = ContactSubmission.objects.first()
send_contact_confirmation_email(submission)
```

---

## 💡 Common Issues

| Issue | Solution |
|-------|----------|
| Email not sending | Check API key is set |
| PDFs not attached | Verify files exist in folders |
| Emails in spam | Verify domain in Resend |
| API key error | Make sure it starts with `re_` |

---

## 📞 Links

- **Resend Dashboard:** https://resend.com
- **Resend Docs:** https://resend.com/docs
- **Resend Support:** https://resend.com/support
- **Django Admin:** http://127.0.0.1:8000/admin

---

## ✅ Checklist

- [ ] Create Resend account
- [ ] Get API key
- [ ] Set environment variable
- [ ] Test locally
- [ ] Add PDF documents
- [ ] Verify domain (production)
- [ ] Deploy to Heroku
- [ ] Test on production
- [ ] Monitor email delivery

---

## 🎯 Email Flow

```
User submits form
    ↓
Form validated
    ↓
Saved to database
    ↓
Resend sends 2 emails:
├─ Client confirmation (with PDFs)
└─ Internal notification
    ↓
Success message shown
    ↓
Visible in admin panel
```

---

## 💰 Pricing

- **Free:** 100 emails/day
- **Pro:** $20/month (unlimited)
- **Enterprise:** Custom pricing

---

## 🔐 Security

✅ API key in environment variables
✅ No secrets in code
✅ CSRF protection on form
✅ Email validation
✅ Backend validation

---

## 📝 Email Templates

**Client Email:** `main_app/templates/emails/contact_confirmation.html`
- Confirmation message
- Next steps
- CTA button
- Professional styling

**Internal Email:** `main_app/templates/emails/internal_notification.html`
- Submission details
- Client info
- Message content
- Timestamp

---

## 🚀 Production Checklist

- [ ] Resend account created
- [ ] Domain verified in Resend
- [ ] API key set in Heroku
- [ ] PDFs uploaded
- [ ] Email templates customized
- [ ] Test form submitted
- [ ] Email received
- [ ] Admin panel working
- [ ] Monitoring set up

---

## 📞 Quick Support

**Resend not working?**
1. Check API key: `echo $RESEND_API_KEY`
2. Check console for errors
3. Visit https://resend.com/support

**Need to customize emails?**
1. Edit HTML templates in `main_app/templates/emails/`
2. Restart server
3. Test form

**Want to add more attachments?**
1. Edit `main_app/email_utils.py`
2. Add attachment logic
3. Restart server

---

## 🎓 Learn More

- Full setup guide: `RESEND_SETUP_GUIDE.md`
- Implementation summary: `RESEND_IMPLEMENTATION_SUMMARY.md`
- Contact form setup: `CONTACT_FORM_SETUP.md`

