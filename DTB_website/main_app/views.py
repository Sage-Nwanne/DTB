# main_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Profile, Project, ProjectUpdate, ClientFeedback, ClientProfile
from .forms import ProjectForm, CustomUserCreationForm, ClientFeedbackForm, ClientProfileForm, ProjectUpdateForm
from django.contrib.auth.models import User
from .auth_backends import DevBackend
from django.utils import timezone
from django.http import Http404

# Add these helper functions
def is_admin_or_dev(user):
    """Check if user is an admin, staff, or developer"""
    if user.is_staff or user.is_superuser:
        return True
    
    # Check if user is in dev_keys
    dev_backend = DevBackend()
    dev_usernames = [dev['username'] for dev in dev_backend.dev_keys]
    return user.username in dev_usernames

def is_client(user):
    """Check if user is a client"""
    if not user.is_authenticated:
        return False
    
    # Check if user is not a developer or admin
    if is_admin_or_dev(user):
        return False
    
    # A user is a client if they're not a dev/admin
    # We'll create the client_profile if it doesn't exist
    if not hasattr(user, 'client_profile'):
        ClientProfile.objects.create(user=user)
    
    return True

# Define the home view function
def home(request):
    # eventually add testimonials, google reviews api blah blah
    
    # Get developers from the dev keys in auth_backends.py
    dev_backend = DevBackend()
    dev_usernames = [dev['username'] for dev in dev_backend.dev_keys]
    developers = []
    
    for username in dev_usernames:
        try:
            user = User.objects.get(username=username)
            if hasattr(user, 'profile'):
                developers.append(user)
        except User.DoesNotExist:
            # Create the user if they don't exist yet
            user = User.objects.create_user(username=username)
            Profile.objects.create(user=user)
            developers.append(user)
    
    # Get featured projects (latest 2 projects)
    try:
        featured_projects = Project.objects.all().order_by('-id')[:2]
    except Exception:
        # If there's a database error (like missing columns), return empty list
        featured_projects = []
    
    return render(request, 'home.html', {
    #    eventually add testimonials, google reviews api blah blah
        'developers': developers,
        'featured_projects': featured_projects
    })

def about(request):

    

    return render(request, 'about.html')
 

def works(request):
    try:
        projects = Project.objects.all()
    except Exception:
        # If there's a database error (like missing columns), return empty list
        projects = []
    return render(request, 'works.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def reviews(request):
    return render(request, 'reviews.html')

def devs(request):
    # Get developers from the dev keys in auth_backends.py
    dev_backend = DevBackend()
    dev_usernames = [dev['username'] for dev in dev_backend.dev_keys]
    developers = []
    
    for username in dev_usernames:
        try:
            user = User.objects.get(username=username)
            if hasattr(user, 'profile'):
                developers.append(user)
        except User.DoesNotExist:
            # Create the user if they don't exist yet
            user = User.objects.create_user(username=username)
            Profile.objects.create(user=user)
            developers.append(user)
    
    return render(request, 'devs.html', {'developers': developers})

def signup(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')

    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = CustomUserCreationForm(request.POST)

        # Validate the form
        if form.is_valid():
            # Save the user
            user = form.save()

            # Create a profile (for developers) and a client profile (for clients)
            Profile.objects.create(user=user)
            ClientProfile.objects.create(user=user)

            # Log the user in with the ModelBackend explicitly
            from django.contrib.auth import authenticate
            from django.contrib.auth.backends import ModelBackend
            
            # Set the backend attribute on the user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            
            # Redirect to client dashboard for new clients
            return redirect('client_dashboard')
    else:
        # Create an empty form
        form = CustomUserCreationForm()

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
        except ValidationError as e:
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

@login_required
def client_dashboard(request):
    """Main client dashboard view"""
    # Check if user is a client
    if not is_client(request.user):
        messages.error(request, "This area is for clients only.")
        return redirect('home')
    
    # Get or create client profile
    client_profile, created = ClientProfile.objects.get_or_create(user=request.user)
    
    # Get client's projects
    projects = Project.objects.filter(client=request.user)
    
    # For new clients with no projects, show waiting dashboard
    if not projects.exists():
        return render(request, 'client/waiting_dashboard.html', {
            'client_profile': client_profile,
            'projects': projects,  # Pass empty queryset for sidebar
        })
    
    # Check if client has any projects with updates
    has_projects_with_updates = projects.filter(updates__isnull=False).exists()
    
    if not has_projects_with_updates:
        # If projects exist but no updates, show waiting dashboard
        return render(request, 'client/waiting_dashboard.html', {
            'client_profile': client_profile,
            'projects': projects,  # Pass projects for sidebar
        })
    
    # Mark that client has viewed dashboard
    if not client_profile.has_viewed_dashboard:
        client_profile.has_viewed_dashboard = True
        client_profile.save()
    
    # Get recent updates across all projects
    recent_updates = ProjectUpdate.objects.filter(
        project__in=projects
    ).order_by('-created_at')[:5]
    
    # Get unresolved feedback
    unresolved_feedback = ClientFeedback.objects.filter(
        client=request.user,
        is_resolved=False
    )
    
    context = {
        'client_profile': client_profile,
        'projects': projects,
        'recent_updates': recent_updates,
        'unresolved_feedback': unresolved_feedback,
    }
    
    return render(request, 'client/dashboard.html', context)

@login_required
def client_project_detail(request, project_id):
    """View for client to see detailed project information"""
    # Check if user is a client
    if not is_client(request.user):
        messages.error(request, "This area is for clients only.")
        return redirect('home')
    
    # Get project and verify client has access
    project = get_object_or_404(Project, id=project_id, client=request.user)
    
    # Get project updates
    updates = project.updates.all().order_by('-timestamp')
    
    # Handle feedback form submission
    if request.method == 'POST':
        feedback_form = ClientFeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.project = project
            feedback.client = request.user
            feedback.save()
            messages.success(request, "Your feedback has been submitted.")
            return redirect('client_project_detail', project_id=project.id)
    else:
        feedback_form = ClientFeedbackForm()
    
    # Get project feedback
    feedback = project.feedback.filter(client=request.user).order_by('-timestamp')
    
    context = {
        'project': project,
        'updates': updates,
        'feedback': feedback,
        'feedback_form': feedback_form,
    }
    
    return render(request, 'client/project_detail.html', context)

@login_required
@user_passes_test(is_admin_or_dev)
def add_project_update(request, project_id):
    """View for developers to add project updates"""
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.project = project
            update.created_by = request.user
            update.save()
            
            # Notify client if they have viewed dashboard before
            if project.client and hasattr(project.client, 'client_profile'):
                if project.client.client_profile.has_viewed_dashboard:
                    # Here you would send an email notification
                    # For now, just add a message
                    messages.info(request, f"Client {project.client.username} will be notified of this update.")
            
            messages.success(request, "Project update added successfully.")
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectUpdateForm()
    
    context = {
        'form': form,
        'project': project,
    }
    
    return render(request, 'add_project_update.html', context)

@login_required
@user_passes_test(is_admin_or_dev)
def update_project_phase(request, project_id):
    """AJAX view to update project phase"""
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        new_phase = request.POST.get('phase')
        
        if new_phase in dict(Project.PHASE_CHOICES).keys():
            project.current_phase = new_phase
            project.save()
            
            # Create an automatic update for phase change
            phase_name = dict(Project.PHASE_CHOICES)[new_phase]
            ProjectUpdate.objects.create(
                project=project,
                title=f"Project entered {phase_name} phase",
                description=f"We've moved your project into the {phase_name} phase. " + 
                           f"Current progress: {project.get_progress_percentage()}%",
                created_by=request.user
            )
            
            return JsonResponse({
                'success': True,
                'progress': project.get_progress_percentage(),
                'phase': phase_name
            })
        
    return JsonResponse({'success': False}, status=400)

@login_required
@user_passes_test(is_admin_or_dev)
def respond_to_feedback(request, feedback_id):
    """View for developers to respond to client feedback"""
    feedback = get_object_or_404(ClientFeedback, id=feedback_id)
    
    if request.method == 'POST':
        response = request.POST.get('response', '').strip()
        if response:
            feedback.response = response
            feedback.responded_by = request.user
            feedback.response_timestamp = timezone.now()
            feedback.is_resolved = True
            feedback.save()
            
            messages.success(request, "Response sent to client.")
            return redirect('project_detail', project_id=feedback.project.id)
        else:
            messages.error(request, "Response cannot be empty.")
    
    context = {
        'feedback': feedback,
    }
    
    return render(request, 'respond_to_feedback.html', context)
