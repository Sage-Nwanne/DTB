# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Project, ContactSubmission
from .forms import ContactForm
from .email_utils import send_contact_confirmation_email, send_internal_notification_email

# Add these imports
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Define the home view function
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    return render(request, 'works.html')

def contact(request):
    form = ContactForm()

    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Save the contact submission
                contact_submission = form.save()

                # Send confirmation email to client
                send_contact_confirmation_email(contact_submission)

                # Send internal notification to DTB team
                send_internal_notification_email(contact_submission)

                # Show success message
                messages.success(request, 'Thank you for your message! We\'ve sent you a confirmation email. We\'ll be in touch within 24 hours.')

                # Redirect to contact page
                return redirect('contact')
        elif request.method == 'GET' and any(request.GET.get(field) for field in ['name', 'email', 'message']):
            # Handle GET requests with form data (for testing/debugging)
            form = ContactForm(request.GET)
            if form.is_valid():
                # Save the contact submission
                contact_submission = form.save()

                # Send confirmation email to client
                send_contact_confirmation_email(contact_submission)

                # Send internal notification to DTB team
                send_internal_notification_email(contact_submission)

                # Show success message
                messages.success(request, 'Thank you for your message! We\'ve sent you a confirmation email. We\'ll be in touch within 24 hours.')

                # Redirect to contact page
                return redirect('contact')
    except Exception as e:
        print(f"Error in contact view: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'contact.html', {'form': form})

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
