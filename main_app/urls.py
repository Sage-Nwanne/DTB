from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('works', views.works, name='works'),
    path('contact', views.contact, name='contact'),
    path('reviews', views.reviews, name='reviews'),
    path('devs', views.devs, name='devs'),
    path('profile', views.profile, name='profile'),
    path('profile/<str:username>', views.view_profile, name='your_profile'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    
    # Authentication URLs
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
