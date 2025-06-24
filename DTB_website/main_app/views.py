# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from email_validator import validate_email, EmailNotValidError
from .models import Profile, Project
from .forms import ProjectForm

# Add these imports
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Add this function to check if user is admin or dev
def is_admin_or_dev(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    projects = Project.objects.all()
    return render(request, 'works.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def reviews(request):
    return render(request, 'reviews.html')

def devs(request):
    return render(request, 'devs.html')

def signup(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        
        # Validate the form
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Update user profile with additional information
            user.email = request.POST.get('email', '')
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.save()
            
            # Create a customer profile
            Profile.objects.create(user=user)
            
            # Log the user in
            login(request, user)
            
            # Redirect to home page
            return redirect('home')
    else:
        # Create an empty form
        form = UserCreationForm()
    
    # Render the signup template with the form
    return render(request, 'registration/signup.html', {'form': form})

# Custom logout view that ensures redirection to home page
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except:
        profile = None
    
    # Check if profile is complete
    profile_complete = False
    if profile and profile.name and profile.title and profile.bio and profile.profile_picture and profile.certificate:
        profile_complete = True
    
    # Get user's projects
    projects = Project.objects.filter(developers=request.user) if hasattr(request.user, 'id') else []
    
    if request.method == 'POST':
        # Handle form submission
        if not profile:
            profile = Profile(user=request.user)
        
        # Update profile fields
        profile.name = request.POST.get('name', '')
        profile.title = request.POST.get('title', '')
        profile.bio = request.POST.get('bio', '')
        
        # Handle featured project
        featured_project_id = request.POST.get('featured_project')
        if featured_project_id:
            try:
                profile.featured_project = Project.objects.get(id=featured_project_id, developers=request.user)
            except Project.DoesNotExist:
                pass
        
        # Handle file uploads
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        if 'certificate' in request.FILES:
            profile.certificate = request.FILES['certificate']
        
        # Save profile
        profile.save()
        
        # Check if profile is now complete
        if profile.name and profile.title and profile.bio and profile.profile_picture and profile.certificate:
            profile.is_active = True
            profile.save()
            messages.success(request, 'Your profile is now complete and active!')
        else:
            messages.info(request, 'Profile updated, but some information is still missing.')
        
        return redirect('your_profile', profile.user.username)
    
    context = {
        'profile': profile,
        'profile_complete': profile_complete,
        'projects': projects,
    }
    
    return render(request, 'profile.html', context)


def view_profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return render(request, '404.html')
    
    projects = Project.objects.filter(developers__username=username)
    
    context = {
        'profile': profile,
        'projects': projects,
    }
    
    return render(request, 'your-profile.html', context)

def contact(request):
    error_message = None
    success_message = None

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()


        try:
            validate_email(email)

            success_message = "Your message has been submitted successfully. We will get back to you shortly."
        except EmailNotValidError as e:
            error_message = "Please enter a valid email address "
        else:
            # Send email
            success_message = "Your message has been submitted successfully. We will get back to you shortly."
    
    return render(request, 'contact.html', {'error_message': error_message, 'success_message': success_message})

@login_required
@user_passes_test(is_admin_or_dev)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            
            # Clean up technologies input (remove extra spaces)
            technologies = form.cleaned_data.get('technologies', '')
            if technologies:
                # Split by comma, strip whitespace, and rejoin
                tech_list = [tech.strip() for tech in technologies.split(',') if tech.strip()]
                project.technologies = ', '.join(tech_list)
                
            project.save()
            # Add the current user as a developer for this project
            project.developers.add(request.user)
            messages.success(request, 'Project added successfully!')
            return redirect('works')
    else:
        form = ProjectForm()
    
    return render(request, 'add_project.html', {'form': form})

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html')
    
    context = {
        'project': project,
    }
    
    return render(request, 'project_detail.html', context)

@login_required
@user_passes_test(is_admin_or_dev)
def edit_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            
            # Clean up technologies input (remove extra spaces)
            technologies = form.cleaned_data.get('technologies', '')
            if technologies:
                # Split by comma, strip whitespace, and rejoin
                tech_list = [tech.strip() for tech in technologies.split(',') if tech.strip()]
                project.technologies = ', '.join(tech_list)
                
            project.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'edit_project.html', {'form': form, 'project': project})
