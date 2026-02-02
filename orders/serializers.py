from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem
from departments.models import Department, College

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(),
        source='menu_item'  # <-- ensures menu_item_id maps to menu_item
    )
    class Meta:
        model = OrderItem
        fields = ['menu_item_id', 'quantity']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="department",
        required=False,
        allow_null=True
    )

    college = serializers.PrimaryKeyRelatedField(
        queryset=College.objects.all(),
        source="college",
        required=False,
        allow_null=True
    )

    

    class Meta:
            model = Order
            fields = [
                "id",
                "user",
                "college",
                "college_id"
                "department",
                "department_id",
                "total_amount",
                "status",
                "order_type",
                "note",
                "created_at",
                "items",
            ]
        

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user)
        total = 0
        for item in items_data:
            menu_item = item['menu_item']
            price = menu_item.price  # use DB price
            quantity = item['quantity']
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                price=price
            )
            total += price * quantity
        order.total_amount = total
        order.save()
        return order


    
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']