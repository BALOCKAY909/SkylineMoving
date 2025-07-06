from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser for review management'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'skyline.moving.gp@gmail.com'
        password = 'SkylineAdmin2025!'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print(f'Superuser {username} created successfully!')
            print(f'Username: {username}')
            print(f'Password: {password}')
        else:
            print(f'Superuser {username} already exists.')
