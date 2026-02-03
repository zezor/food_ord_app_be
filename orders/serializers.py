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



# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)

#     college = serializers.SlugRelatedField(
#         queryset=College.objects.all(),
#         slug_field="name",
#         required=False,
#         allow_null=True
#     )

#     department = serializers.SlugRelatedField(
#         queryset=Department.objects.all(),
#         slug_field="name",
#         required=False,
#         allow_null=True
#     )

#     class Meta:
#         model = Order
#         fields = [
#             "id",
#             "user",
#             "college",
#             "department",
#             "total_amount",
#             "status",
#             "order_type",
#             "note",
#             "created_at",
#             "items",
#         ]
#         read_only_fields = ["user", "total_amount", "status", "created_at"]

#     def create(self, validated_data):
#         items_data = validated_data.pop("items")
#         user = self.context["request"].user

#         order = Order.objects.create( **validated_data)

#         total = 0
#         for item in items_data:
#             menu_item = item["menu_item"]
#             price = menu_item.price
#             quantity = item["quantity"]

#             OrderItem.objects.create(
#                 order=order,
#                 menu_item=menu_item,
#                 quantity=quantity,
#                 price=price,
#             )

#             total += price * quantity

#         order.total_amount = total
#         order.save()
#         return order

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    college = serializers.SlugRelatedField(
        queryset=College.objects.all(),
        slug_field="name"
    )

    department = serializers.SlugRelatedField(
        queryset=Department.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "college",
            "department",
            "total_amount",
            "status",
            "order_type",
            "note",
            "created_at",
            "items",
        ]

    # def create(self, validated_data):
    #     items_data = validated_data.pop("items")
    #     user = self.context["request"].user

    #     order = Order.objects.create( **validated_data)

    #     total = 0
    #     for item in items_data:
    #         menu_item = item["menu_item"]
    #         quantity = item["quantity"]
    #         price = menu_item.price

    #         OrderItem.objects.create(
    #             order=order,
    #             menu_item=menu_item,
    #             quantity=quantity,
    #             price=price
    #         )
    #         total += price * quantity

    #     order.total_amount = total
    #     order.save()
    #     return order
 
    def create(self, validated_data):
        items_data = validated_data.pop("items")
        request = self.context.get("request")
        user = request.user

        order = Order.objects.create(
            user=user,
            college=validated_data.get("college"),
            department=validated_data.get("department"),
            order_type=validated_data.get("order_type", "normal"),
            note=validated_data.get("note", ""),
        )

        total = 0

        for item in items_data:
            menu_item = item["menu_item"]
            quantity = item["quantity"]
            price = menu_item.price

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                price=price,
            )

            total += price * quantity

        order.total_amount = total
        order.save()

        return order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']