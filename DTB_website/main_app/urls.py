from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('works', views.works, name='works'),
    path('contact', views.contact, name='contact'),
    path('reviews', views.reviews, name='reviews'),
    path('devs', views.devs, name='devs'),
    path('profile', views.profile, name='profile'),
    path('profile/<str:username>', views.view_profile, name='your_profile'),
    path('add_project', views.add_project, name='add_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),

    # Authentication URLs
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Client dashboard URLs
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    path('client/project/<int:project_id>/', views.client_project_detail, name='client_project_detail'),
    
    # Developer project management URLs
    path('project/<int:project_id>/update/add/', views.add_project_update, name='add_project_update'),
    path('project/<int:project_id>/phase/update/', views.update_project_phase, name='update_project_phase'),
    path('feedback/<int:feedback_id>/respond/', views.respond_to_feedback, name='respond_to_feedback'),
]
