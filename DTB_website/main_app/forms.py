from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, ClientFeedback, ProjectUpdate, ClientProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change the label for username field to "Company Name"
        self.fields['username'].label = 'Company Name'
        self.fields['username'].help_text = 'Enter your company name. Letters, numbers, spaces, and @/./+/-/_ characters are allowed.'

        # Remove the default username validator that restricts characters
        self.fields['username'].validators = []

        # Add custom validation to allow more characters including spaces
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your company name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your company email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Company name is required.')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A company with this name already exists.')

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'short_description', 'description',  
                 'image', 'technologies', 'current_phase', 'estimated_completion']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'technologies': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E.g., Django, React, PostgreSQL (comma-separated)'
            }),
            'current_phase': forms.Select(attrs={'class': 'form-control'}),
            'estimated_completion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ClientFeedbackForm(forms.ModelForm):
    class Meta:
        model = ClientFeedback  # Make sure this model exists in your models.py
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectUpdate
        fields = ['title', 'content', 'image', 'preview_url', 'preview_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preview_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile  # Make sure this model exists in your models.py
        fields = ['company_name', 'industry', 'contact_email', 'phone_number']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
