# api_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContactViewSet, SpamViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'spams', SpamViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]