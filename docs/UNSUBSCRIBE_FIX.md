# Newsletter Unsubscribe Fix

## Problem
Users were experiencing server errors when trying to unsubscribe from the newsletter. The issue was caused by email addresses being passed directly in the URL, which can contain special characters (`@`, `+`, `.`) that cause URL encoding issues.

## Solution
Implemented a **secure token-based unsubscribe system** using UUID tokens instead of email addresses in URLs.

---

## Changes Made

### 1. **Database Model** (`main_app/models.py`)
- Added `unsubscribe_token` field to `NewsletterSubscriber` model
- Uses UUID4 for unique, secure tokens
- Token is automatically generated when a subscriber is created

```python
unsubscribe_token = models.UUIDField(
    default=uuid.uuid4, 
    editable=False, 
    unique=True, 
    verbose_name='Unsubscribe Token'
)
```

### 2. **URL Pattern** (`main_app/urls.py`)
Changed from:
```python
path('newsletter/unsubscribe/<str:email>/', ...)
```

To:
```python
path('newsletter/unsubscribe/<uuid:token>/', ...)
```

### 3. **View Function** (`main_app/views.py`)
Updated to use token instead of email:
```python
def newsletter_unsubscribe(request, token):
    try:
        subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
        subscriber.unsubscribe()
        messages.success(request, "You've been unsubscribed...")
    except NewsletterSubscriber.DoesNotExist:
        messages.error(request, "Invalid unsubscribe link...")
```

### 4. **Email Templates**
Updated both email templates to use the token:
- `emails/newsletter_welcome.html`
- `emails/newsletter_blog_update.html`

Changed from:
```html
<a href="https://dtbsolutions.tech/newsletter/unsubscribe/{{ email }}/">
```

To:
```html
<a href="https://dtbsolutions.tech/newsletter/unsubscribe/{{ unsubscribe_token }}/">
```

### 5. **Email Utility Functions** (`main_app/email_utils.py`)
Added `unsubscribe_token` to email context:
```python
context = {
    'name': subscriber.name or 'there',
    'email': subscriber.email,
    'unsubscribe_token': subscriber.unsubscribe_token,  # Added
    ...
}
```

---

## Benefits

✅ **No URL encoding issues** - UUIDs are URL-safe
✅ **More secure** - Email addresses not exposed in URLs
✅ **Privacy-friendly** - Tokens can't be guessed
✅ **Reliable** - Works with all email addresses (including special characters)
✅ **Better error messages** - Clear feedback for invalid links

---

## Migration

A new migration was created: `0006_add_unsubscribe_token.py`

**To deploy:**
1. Commit and push changes
2. Migration will run automatically on Heroku (via `Procfile`)
3. Existing subscribers will get unique tokens automatically

---

## Testing

Example unsubscribe URL:
```
https://dtbsolutions.tech/newsletter/unsubscribe/5d2bd77b-c7bc-4c4c-a910-5072eaaa3db1/
```

Instead of:
```
https://dtbsolutions.tech/newsletter/unsubscribe/user@example.com/  ❌ (causes errors)
```

---

## Deployment Checklist

- [x] Add `unsubscribe_token` field to model
- [x] Create migration
- [x] Update URL pattern
- [x] Update view function
- [x] Update email templates
- [x] Update email utility functions
- [x] Test locally
- [ ] Commit and push to GitHub
- [ ] Deploy to Heroku
- [ ] Test on production

---

## Next Steps

After deploying:
1. Test unsubscribe functionality on production
2. Monitor for any errors in Heroku logs
3. Verify existing subscribers have tokens assigned

