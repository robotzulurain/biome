import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser non-interactively'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment with defaults
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@biome.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword123')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser: {username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Superuser {username} already exists')
            )
