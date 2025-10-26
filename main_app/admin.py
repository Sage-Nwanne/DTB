from django.contrib import admin
from .models import Project, Profile, ContactSubmission

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
