from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'company', 'service', 'budget', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text placeholder-gray-500 focus:outline-none focus:border-accent transition',
                'placeholder': 'Your name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text placeholder-gray-500 focus:outline-none focus:border-accent transition',
                'placeholder': 'your@email.com',
                'required': True,
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text placeholder-gray-500 focus:outline-none focus:border-accent transition',
                'placeholder': 'Your company',
            }),
            'service': forms.Select(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text focus:outline-none focus:border-accent transition',
            }),
            'budget': forms.Select(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text focus:outline-none focus:border-accent transition',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-graphite border border-slate rounded-md px-4 py-3 text-text placeholder-gray-500 focus:outline-none focus:border-accent transition resize-none',
                'placeholder': 'What are you looking to build or automate?',
                'rows': 6,
                'required': True,
            }),
        }

