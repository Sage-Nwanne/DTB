from django.contrib import admin
from .models import Project, Profile

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
