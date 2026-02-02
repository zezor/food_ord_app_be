from django.db import models
from django.conf import settings
from menu.models import MenuItem
from departments.models import Department, College
User = settings.AUTH_USER_MODEL

class Order(models.Model):
    ORDER_TYPES = (
        ("normal", "Normal"),
        ("bulk", "Bulk"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')],
        default='pending'
    )

    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPES,
        default="normal"
    )

    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    college = models.ForeignKey(
        College,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

