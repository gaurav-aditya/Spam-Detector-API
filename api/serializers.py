# api/serializers.py

from rest_framework import serializers
from .models import Contact, Spam
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number']

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['phone_number']