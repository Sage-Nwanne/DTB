from django.core.management.base import BaseCommand
from main_app.models import BlogPost, Category

class Command(BaseCommand):
    help = 'Hide all blog posts (set to draft) while keeping categories visible'

    def handle(self, *args, **kwargs):
        # Set all blog posts to draft
        updated = BlogPost.objects.filter(status='published').update(status='draft')
        
        self.stdout.write(self.style.SUCCESS(f'✓ Hidden {updated} blog post(s) - set to draft status'))
        
        # Show categories count
        categories_count = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(f'✓ {categories_count} categories remain visible'))
        
        # Show current status
        total_posts = BlogPost.objects.count()
        draft_posts = BlogPost.objects.filter(status='draft').count()
        published_posts = BlogPost.objects.filter(status='published').count()
        
        self.stdout.write(self.style.WARNING(f'\nCurrent Status:'))
        self.stdout.write(f'  Total posts: {total_posts}')
        self.stdout.write(f'  Draft (hidden): {draft_posts}')
        self.stdout.write(f'  Published (visible): {published_posts}')
        self.stdout.write(f'  Categories (visible): {categories_count}')

