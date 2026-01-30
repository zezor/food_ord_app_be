from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(),
        source='menu_item'  # <-- ensures menu_item_id maps to menu_item
    )
    class Meta:
        model = OrderItem
        fields = ['menu_item_id', 'quantity', 'price']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'total_amount', 'status', 'created_at']

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