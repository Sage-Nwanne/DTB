# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Project, ContactSubmission, BlogPost, Category, Tag, NewsletterSubscriber
from .forms import ContactForm, NewsletterSubscriptionForm
from .email_utils import send_contact_confirmation_email, send_internal_notification_email, send_newsletter_welcome_email

# Add these imports
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone

# Define the home view function
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    return render(request, 'works.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

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


def sitemap(request):
    """Generate XML sitemap for SEO"""
    domain = 'https://dtbsolutions.tech'

    urls = [
        {'loc': '/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'loc': '/services', 'priority': '0.9', 'changefreq': 'weekly'},
        {'loc': '/works', 'priority': '0.8', 'changefreq': 'weekly'},
        {'loc': '/about', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': '/reviews', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': '/contact', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': '/privacy', 'priority': '0.3', 'changefreq': 'yearly'},
        {'loc': '/terms', 'priority': '0.3', 'changefreq': 'yearly'},
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{domain}{url["loc"]}</loc>')
        xml.append(f'    <priority>{url["priority"]}</priority>')
        xml.append(f'    <changefreq>{url["changefreq"]}</changefreq>')
        xml.append('  </url>')

    xml.append('</urlset>')

    return HttpResponse('\n'.join(xml), content_type='application/xml')


def robots_txt(request):
    """Generate robots.txt for SEO"""
    lines = [
        'User-agent: *',
        'Allow: /',
        '',
        'Sitemap: https://dtbsolutions.tech/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


# Blog Views
def blog_list(request):
    """Display list of published blog posts"""
    posts = BlogPost.objects.filter(status='published', published_at__lte=timezone.now()).order_by('-published_at')
    categories = Category.objects.all()

    # Pagination
    paginator = Paginator(posts, 9)  # 9 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories,
        'current_category': None,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, slug):
    """Display single blog post"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')

    # Increment view count
    post.views += 1
    post.save(update_fields=['views'])

    # Get related posts (same category, exclude current)
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published',
        published_at__lte=timezone.now()
    ).exclude(id=post.id).order_by('-published_at')[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog_detail.html', context)


def blog_category(request, slug):
    """Display posts filtered by category"""
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(
        category=category,
        status='published',
        published_at__lte=timezone.now()
    ).order_by('-published_at')
    categories = Category.objects.all()

    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories,
        'current_category': category,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'blog_list.html', context)


def blog_tag(request, slug):
    """Display posts filtered by tag"""
    tag = get_object_or_404(Tag, slug=slug)
    posts = BlogPost.objects.filter(
        tags=tag,
        status='published',
        published_at__lte=timezone.now()
    ).order_by('-published_at')
    categories = Category.objects.all()

    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'categories': categories,
        'current_tag': tag,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'blog_list.html', context)


def newsletter_subscribe(request):
    """Handle newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if already subscribed
            existing = NewsletterSubscriber.objects.filter(email=email).first()

            if existing:
                if existing.is_active:
                    messages.info(request, "You're already subscribed to our newsletter!")
                else:
                    # Reactivate subscription
                    existing.is_active = True
                    existing.unsubscribed_at = None
                    existing.save()
                    messages.success(request, "Welcome back! Your subscription has been reactivated.")
            else:
                # Create new subscription
                subscriber = form.save(commit=False)
                subscriber.source = request.POST.get('source', 'blog')
                subscriber.save()

                # Send welcome email
                send_newsletter_welcome_email(subscriber)

                messages.success(request, "🎉 Success! You're now subscribed to DTB Insights. Check your email for a welcome message.")

            return redirect(request.META.get('HTTP_REFERER', 'blog_list'))
        else:
            messages.error(request, "Please enter a valid email address.")
            return redirect(request.META.get('HTTP_REFERER', 'blog_list'))

    return redirect('blog_list')


def newsletter_unsubscribe(request, token):
    """Handle newsletter unsubscription"""
    try:
        subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
        subscriber.unsubscribe()
        messages.success(request, "You've been unsubscribed from our newsletter. We're sorry to see you go!")
    except NewsletterSubscriber.DoesNotExist:
        messages.error(request, "Invalid unsubscribe link. Please contact us if you need assistance.")

    return render(request, 'newsletter_unsubscribe.html')
