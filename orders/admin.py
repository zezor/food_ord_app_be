from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at', 'ordered_at', 'order_type', 'department')
    list_filter = ('status', 'order_type', 'created_at', 'department')
    search_fields = ('user__email', 'id')
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')
    search_fields = ('order__id', 'menu_item__name')
admin.site.register(OrderItem, OrderItemAdmin)
