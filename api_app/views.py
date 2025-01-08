from django.shortcuts import render

# Create your views here.
# api/views.py
from django.http import JsonResponse

from rest_framework import viewsets, permissions
from .models import Contact, Spam
from .serializers import ContactSerializer, SpamSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def home(request):
    return JsonResponse({"message": "Welcome to the Spam Detector API!"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    # Override the get_queryset method to filter contacts by the logged-in user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        contacts = Contact.objects.filter(name__icontains=query, user=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

class SpamViewSet(viewsets.ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def mark_spam(self, request):
        phone_number = request.data.get('phone_number')
        spam, created = Spam.objects.get_or_create(phone_number=phone_number)
        spam.marked_by.add(request.user)
        return Response({"status": "marked as spam"}, status=201)