from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializer import CustomUserSerializer


 # Allow unrestricted access for registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []  # Allow unrestricted access for registration
