from django.db import models

# Create your models here.
# api/models.py

from django.db import models
from django.contrib.auth.models import User

# Model to store contact information
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

# Model to store spam numbers
class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    marked_by = models.ManyToManyField(User, related_name='spam_marked_by')

    def __str__(self):
        return self.phone_number