# Delete Blog Posts from Production

## Quick Guide

Since the sample blog posts still exist in your **Heroku database**, you need to delete them manually.

---

## Option 1: Using Heroku Console (Easiest)

1. Go to your Heroku dashboard: https://dashboard.heroku.com/
2. Click on your app: **dtb-website**
3. Click **"More"** → **"Run console"**
4. Paste this command:
   ```bash
   python manage.py shell
   ```
5. Then paste this code:
   ```python
   from main_app.models import BlogPost
   count = BlogPost.objects.count()
   BlogPost.objects.all().delete()
   print(f'Deleted {count} blog posts')
   exit()
   ```
6. Press Enter and the posts will be deleted!

---

## Option 2: Using Heroku CLI

If you have Heroku CLI installed:

```bash
heroku run python manage.py shell --app dtb-website
```

Then paste:
```python
from main_app.models import BlogPost
BlogPost.objects.all().delete()
exit()
```

---

## Option 3: Using Django Admin

1. Go to: https://dtbsolutions.tech/admin/
2. Log in with your admin credentials
3. Click **"Blog posts"**
4. Select all posts (checkbox at top)
5. Choose **"Delete selected blog posts"** from the dropdown
6. Click **"Go"**
7. Confirm deletion

---

## What Happens After Deletion

✅ Blog page will show: "No blog posts to display yet"  
✅ Categories will still be visible (AI & Automation, Business Growth, etc.)  
✅ Blog infrastructure remains intact  
✅ Ready to add real posts when you're ready  

---

## Adding Real Blog Posts Later

When you're ready to add real blog posts, you can:

1. **Use Django Admin** (easiest):
   - Go to https://dtbsolutions.tech/admin/
   - Click "Blog posts" → "Add blog post"
   - Fill in the details and publish

2. **Create a management command** (for bulk posts)
3. **Use the Django shell** (for quick testing)

---

## Current Status

- ✅ Sample blog post commands removed from codebase
- ✅ Procfile updated (no longer creates sample posts on deploy)
- ✅ Local database: 0 blog posts
- ❌ Production database: Still has 6 sample posts (delete using steps above)

---

**After you delete the posts from production, your blog page will be clean and ready for real content!** 🎉

