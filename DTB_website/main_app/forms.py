from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'project_url', 'short_description', 'full_description', 'technologies', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'full_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'project_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'technologies': forms.TextInput(attrs={
                'class': 'form-control tech-autocomplete',
                'placeholder': 'E.g., Django, React, PostgreSQL (comma-separated)',
                'data-role': 'tagsinput'
            }),
        }
