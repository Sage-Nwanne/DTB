from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    from django.utils import timezone
    title = models.CharField(max_length=100, verbose_name='Project Title')
    short_description = models.TextField(max_length=200, verbose_name='Short Description')
    full_description = models.TextField(verbose_name='Full Description')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, verbose_name='Project Image')
    technologies = models.CharField(max_length=200, verbose_name='Technologies')  # Comma-separated list of technologies
    developers = models.ManyToManyField(User, related_name='projects', verbose_name='Developers')
    assigned_at = models.DateTimeField(default=timezone.now, verbose_name='Assigned At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.title

class Profile(models.Model):
    from django.utils import timezone
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=100, blank=True, verbose_name='Name')
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    bio = models.TextField(blank=True, verbose_name='Bio')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, verbose_name='Profile Picture')
    certificate = models.ImageField(upload_to='certificates/', blank=True, null=True, verbose_name='Certificate')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, verbose_name='Resume')
    featured_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='featured_by', verbose_name='Featured Project')
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created At')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ContactSubmission(models.Model):
    SERVICE_CHOICES = [
        ('web', 'Web Design'),
        ('automation', 'Agentic Automation'),
        ('marketing', 'Marketing & Growth'),
        ('consulting', 'Consulting'),
        ('other', 'Other'),
    ]

    BUDGET_CHOICES = [
        ('less-2k', 'Less than $2K'),
        ('2-5k', '$2K - $5K'),
        ('5-10k', '$5K - $10K'),
        ('10-25k', '$10K - $25K'),
        ('25k+', '$25K+'),
    ]

    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    company = models.CharField(max_length=100, blank=True, verbose_name='Company')
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, verbose_name='Service Interest')
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, verbose_name='Budget Range')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')

    def __str__(self):
        return f"Contact from {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    """Blog post categories"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL Slug')
    description = models.TextField(blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_category', kwargs={'slug': self.slug})


class Tag(models.Model):
    """Blog post tags"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag Name')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_tag', kwargs={'slug': self.slug})


class BlogPost(models.Model):
    """Blog post model"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    # Basic Info
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL Slug')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Author')

    # Content
    excerpt = models.TextField(max_length=300, verbose_name='Excerpt/Summary', help_text='Short description for previews (300 chars max)')
    content = models.TextField(verbose_name='Content')
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name='Featured Image', help_text='Recommended: 1200x630px')

    # SEO
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='Meta Description', help_text='SEO description (160 chars max)')
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name='Meta Keywords', help_text='Comma-separated keywords')

    # Organization
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts', verbose_name='Category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Tags')

    # Status & Timing
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Status')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Published At')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    # Engagement
    views = models.PositiveIntegerField(default=0, verbose_name='Views')
    read_time = models.PositiveIntegerField(default=5, verbose_name='Read Time (minutes)', help_text='Estimated reading time')

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Auto-calculate read time based on content (average 200 words/min)
        if self.content:
            word_count = len(self.content.split())
            self.read_time = max(1, round(word_count / 200))

        # Auto-generate meta description from excerpt if not provided
        if not self.meta_description and self.excerpt:
            self.meta_description = self.excerpt[:160]

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def is_published(self):
        return self.status == 'published' and self.published_at is not None


class NewsletterSubscriber(models.Model):
    """Newsletter email subscription model"""
    email = models.EmailField(unique=True, verbose_name='Email Address')
    name = models.CharField(max_length=100, blank=True, verbose_name='Name')
    is_active = models.BooleanField(default=True, verbose_name='Active Subscription')
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name='Subscribed At')
    unsubscribed_at = models.DateTimeField(null=True, blank=True, verbose_name='Unsubscribed At')

    # Track engagement
    emails_sent = models.PositiveIntegerField(default=0, verbose_name='Emails Sent')
    emails_opened = models.PositiveIntegerField(default=0, verbose_name='Emails Opened')
    last_email_sent = models.DateTimeField(null=True, blank=True, verbose_name='Last Email Sent')

    # Source tracking
    source = models.CharField(max_length=50, default='blog', verbose_name='Subscription Source',
                             help_text='Where they subscribed from (blog, homepage, etc.)')

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'

    def __str__(self):
        return self.email

    def unsubscribe(self):
        """Unsubscribe user from newsletter"""
        self.is_active = False
        self.unsubscribed_at = timezone.now()
        self.save()
