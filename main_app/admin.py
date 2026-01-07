from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Profile, ContactSubmission, BlogPost, Category, Tag, NewsletterSubscriber

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_at', 'updated_at')
    list_filter = ('assigned_at', 'updated_at')
    search_fields = ('title', 'short_description', 'technologies')
    filter_horizontal = ('developers',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__username', 'name', 'title')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'budget', 'created_at')
    list_filter = ('service', 'budget', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at', 'message')
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company')
        }),
        ('Project Details', {
            'fields': ('service', 'budget', 'message')
        }),
        ('Submission', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'published_at', 'views', 'read_time')
    list_filter = ('status', 'category', 'tags', 'published_at', 'created_at')
    search_fields = ('title', 'content', 'excerpt', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at', 'views', 'read_time', 'preview_image')
    date_hierarchy = 'published_at'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'status')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image', 'preview_image')
        }),
        ('Organization', {
            'fields': ('category', 'tags')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('published_at',)
        }),
        ('Statistics', {
            'fields': ('views', 'read_time', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def preview_image(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 200px;" />', obj.featured_image.url)
        return "No image"
    preview_image.short_description = 'Image Preview'

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'subscribed_at', 'emails_sent', 'emails_opened', 'source')
    list_filter = ('is_active', 'source', 'subscribed_at')
    search_fields = ('email', 'name')
    readonly_fields = ('subscribed_at', 'unsubscribed_at', 'emails_sent', 'emails_opened', 'last_email_sent')
    date_hierarchy = 'subscribed_at'

    fieldsets = (
        ('Subscriber Information', {
            'fields': ('email', 'name', 'source')
        }),
        ('Subscription Status', {
            'fields': ('is_active', 'subscribed_at', 'unsubscribed_at')
        }),
        ('Engagement Metrics', {
            'fields': ('emails_sent', 'emails_opened', 'last_email_sent'),
            'classes': ('collapse',)
        }),
    )

    actions = ['export_emails']

    def export_emails(self, request, queryset):
        """Export email addresses as CSV"""
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="newsletter_subscribers.csv"'

        writer = csv.writer(response)
        writer.writerow(['Email', 'Name', 'Active', 'Subscribed At', 'Source'])

        for subscriber in queryset:
            writer.writerow([
                subscriber.email,
                subscriber.name,
                'Yes' if subscriber.is_active else 'No',
                subscriber.subscribed_at.strftime('%Y-%m-%d %H:%M'),
                subscriber.source
            ])

        return response

    export_emails.short_description = 'Export selected emails to CSV'
