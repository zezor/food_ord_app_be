from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'name',
            'price',
            'is_available',
            'created_at',
            'updated_at',
            'category',
            'category_name',
            'menu_date'
        ]
        read_only_fields = ('created_at', 'updated_at')

class MenuItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'is_available', 'category', 'menu_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem.category.field.related_model
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')