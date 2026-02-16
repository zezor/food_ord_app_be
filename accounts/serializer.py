from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'full_name', 'password', 'phone_number', 'department', 'is_staff', 'is_active')
        read_only_fields = ('id', 'is_staff', 'is_active')
