# Blog Posts Hidden - Categories Visible

## Summary
All sample blog posts are now hidden (set to 'draft' status) while keeping the category buttons visible on the blog page.

---

## What Users See on Production

### ✅ Visible:
- **Category buttons**: AI & Automation, Business Growth, Digital Marketing, Web Design
- **Blog page header** and newsletter signup
- **"All Posts" button**

### ❌ Hidden:
- All 6 sample blog posts (set to draft status)
- No blog post cards will appear in the grid
- Blog posts are not accessible via direct URLs

---

## How It Works

The blog views (`blog_list`, `blog_category`, `blog_tag`) only show posts with:
```python
status='published'
```

Since all sample posts are set to `status='draft'`, they won't appear on the site.

---

## Management Commands

### 1. Hide All Blog Posts
```bash
python manage.py hide_all_blog_posts
```
Sets all published posts to draft status.

### 2. Create Sample Blog Posts (as Draft)
```bash
python manage.py create_sample_blog_posts
```
Creates 6 sample posts + 4 categories + 6 tags (all posts are draft by default).

---

## For Production (Heroku)

### Option 1: Run Command Manually
```bash
heroku run python manage.py hide_all_blog_posts --app your-app-name
```

### Option 2: Already Handled
The `create_sample_blog_posts` command (which runs on deployment via `Procfile`) now creates posts as **draft by default**, so they won't be visible.

---

## Current Status (Local)

```
Total posts: 6
Draft (hidden): 6
Published (visible): 0
Categories (visible): 4
```

---

## When You're Ready to Publish

You can publish individual posts from the Django admin:

1. Go to: `https://dtbsolutions.tech/admin/`
2. Click **Blog posts**
3. Select a post
4. Change **Status** from "Draft" to "Published"
5. Click **Save**

Or publish all at once:
```bash
heroku run python manage.py shell --app your-app-name
```

Then in the shell:
```python
from main_app.models import BlogPost
BlogPost.objects.all().update(status='published')
```

---

## Files Changed

- ✅ `main_app/management/commands/create_sample_blog_posts.py` - Creates posts as draft
- ✅ `main_app/management/commands/hide_all_blog_posts.py` - New command to hide posts
- ✅ `docs/BLOG_POSTS_HIDDEN.md` - This documentation

---

## What Happens on Next Deploy

When you deploy to Heroku:
1. ✅ Migration runs (adds unsubscribe tokens)
2. ✅ `create_sample_blog_posts` runs (creates categories + draft posts)
3. ✅ Categories appear on blog page
4. ✅ No blog posts are visible (all are draft)

Perfect for showing the blog structure without displaying placeholder content! 🎉

