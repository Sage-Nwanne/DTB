from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Make sure all models are defined here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    certificate = models.ImageField(upload_to='certificates/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Project(models.Model):
    PLANNING = 'PL'
    DESIGN = 'DE'
    DEVELOPMENT = 'DV'
    TESTING = 'TE'
    COMPLETE = 'CO'
    
    PHASE_CHOICES = [
        (PLANNING, 'Planning'),
        (DESIGN, 'Design'),
        (DEVELOPMENT, 'Development'),
        (TESTING, 'Testing'),
        (COMPLETE, 'Complete'),
    ]
    
    title = models.CharField(max_length=100, verbose_name='Project Title')
    short_description = models.TextField(max_length=200, verbose_name='Short Description')
    # Using description instead of full_description to match the database
    description = models.TextField(verbose_name='Full Description')  
    # project_url will be added in a migration
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, verbose_name='Project Image')
    technologies = models.CharField(max_length=200, verbose_name='Technologies')
    developers = models.ManyToManyField(User, related_name='projects', verbose_name='Developers')
    client = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='client_projects')
    current_phase = models.CharField(max_length=2, choices=PHASE_CHOICES, default=PLANNING)
    estimated_completion = models.DateField(blank=True, null=True)
    assigned_at = models.DateTimeField(default=timezone.now, verbose_name='Assigned At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    
    def get_progress_percentage(self):
        phases = [self.PLANNING, self.DESIGN, self.DEVELOPMENT, self.TESTING, self.COMPLETE]
        current_index = phases.index(self.current_phase)
        return int((current_index / (len(phases) - 1)) * 100)
    
    def __str__(self):
        return self.title

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    has_viewed_dashboard = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Client Profile: {self.user.username}"

class ClientFeedback(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedback')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_given')
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)
    responded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='responses')
    
    def __str__(self):
        return f"Feedback on {self.project.title} by {self.client.username}"

class ProjectUpdate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='update_images/', blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)
    preview_file = models.FileField(upload_to='update_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_updates')
    
    def __str__(self):
        return f"{self.title} - {self.project.title}"
