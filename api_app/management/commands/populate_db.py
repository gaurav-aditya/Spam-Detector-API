# api/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from api.models import Contact, Spam
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        for i in range(10):  # Create 10 users
            user = User.objects.create_user(username=f'user{i}', password='password')
            for j in range(5):  # Each user has 5 contacts
                Contact.objects.create(user=user, name=f'Contact {j}', phone_number=f'1234567{random.randint(0, 99)}')

        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))