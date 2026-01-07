# Generated migration for adding unsubscribe_token field
import uuid
from django.db import migrations, models


def generate_unique_tokens(apps, schema_editor):
    """Generate unique tokens for existing subscribers"""
    NewsletterSubscriber = apps.get_model('main_app', 'NewsletterSubscriber')
    for subscriber in NewsletterSubscriber.objects.all():
        subscriber.unsubscribe_token = uuid.uuid4()
        subscriber.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_newslettersubscriber'),
    ]

    operations = [
        # Step 1: Add field without unique constraint
        migrations.AddField(
            model_name='newslettersubscriber',
            name='unsubscribe_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, verbose_name='Unsubscribe Token'),
        ),
        # Step 2: Populate unique values for existing records
        migrations.RunPython(generate_unique_tokens, reverse_code=migrations.RunPython.noop),
        # Step 3: Make field non-nullable and unique
        migrations.AlterField(
            model_name='newslettersubscriber',
            name='unsubscribe_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unsubscribe Token'),
        ),
    ]
