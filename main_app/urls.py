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

    # SEO URLs
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots'),

    # Blog URLs
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<slug:slug>/', views.blog_category, name='blog_category'),
    path('blog/tag/<slug:slug>/', views.blog_tag, name='blog_tag'),

    # Newsletter URLs
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter/unsubscribe/<str:email>/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),

    # Authentication URLs
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
