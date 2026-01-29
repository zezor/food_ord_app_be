from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class MenuItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'is_available', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem.category.field.related_model
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')