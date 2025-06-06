from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Project Title')
    short_description = models.TextField(max_length=200, verbose_name='Short Description')
    full_description = models.TextField(verbose_name='Full Description')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, verbose_name='Project Image')
    technologies = models.CharField(max_length=200, verbose_name='Technologies')  # Comma-separated list of technologies
    developers = models.ManyToManyField(User, related_name='projects', verbose_name='Developers')
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name='Assigned At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=100, blank=True, verbose_name='Name')
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    bio = models.TextField(blank=True, verbose_name='Bio')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, verbose_name='Profile Picture')
    certificate = models.ImageField(upload_to='certificates/', blank=True, null=True, verbose_name='Certificate')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, verbose_name='Resume')
    featured_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='featured_by', verbose_name='Featured Project')
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
