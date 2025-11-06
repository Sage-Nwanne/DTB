import resend
from django.conf import settings
from django.template.loader import render_to_string
import os
import base64

def _set_resend_api_key():
    """Set the Resend API key from settings"""
    resend_api_key = getattr(settings, 'RESEND_API_KEY', '')
    if resend_api_key:
        resend.api_key = resend_api_key
    return resend_api_key

def send_contact_confirmation_email(contact_submission):
    """
    Send a simple confirmation email to the client letting them know
    we've received their message and will respond within 24 hours.
    """

    # Set Resend API key before sending
    api_key = _set_resend_api_key()
    if not api_key:
        print("✗ RESEND_API_KEY not configured")
        return False

    # Email subject and recipient
    subject = "We've Received Your Message"
    recipient_email = contact_submission.email

    # Prepare email context
    context = {
        'name': contact_submission.name,
    }

    # Render email body
    email_body = render_to_string('emails/contact_confirmation.html', context)

    # Send email via Resend
    try:
        response = resend.Emails.send({
            'from': settings.DEFAULT_FROM_EMAIL,
            'to': recipient_email,
            'subject': subject,
            'html': email_body,
        })
        print(f"✓ Confirmation email sent to {recipient_email}")
        return True
    except Exception as e:
        print(f"✗ Error sending email via Resend: {str(e)}")
        return False


def send_internal_notification_email(contact_submission):
    """
    Send an internal notification to the DTB team about a new contact submission
    """

    # Set Resend API key before sending
    api_key = _set_resend_api_key()
    if not api_key:
        print("✗ RESEND_API_KEY not configured")
        return False

    subject = f"New Contact Submission from {contact_submission.name}"

    context = {
        'name': contact_submission.name,
        'email': contact_submission.email,
        'company': contact_submission.company or 'Not provided',
        'service': contact_submission.get_service_display(),
        'budget': contact_submission.get_budget_display(),
        'message': contact_submission.message,
        'submitted_at': contact_submission.created_at,
    }

    email_body = render_to_string('emails/internal_notification.html', context)

    # Send email via Resend
    try:
        response = resend.Emails.send({
            'from': settings.DEFAULT_FROM_EMAIL,
            'to': settings.CONTACT_EMAIL,
            'subject': subject,
            'html': email_body,
        })
        print(f"✓ Internal notification sent to {settings.CONTACT_EMAIL}")
        return True
    except Exception as e:
        print(f"✗ Error sending internal notification via Resend: {str(e)}")
        return False

