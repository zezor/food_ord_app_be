from django.db.models import Sum, Count, F
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order, OrderItem
from menu.models import MenuItem
from .serializers import OrderSerializer, OrderStatusUpdateSerializer


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission: Only admins or the owner of the object can access/modify.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user


class OrderViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD for Orders + dashboard summary endpoint
    """
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff:
    #         return Order.objects.all().order_by('-created_at')
    #     return Order.objects.filter(user=user).order_by('-created_at')
    
    # @action(detail=False, methods=['post'])
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user, department=self.request.data.get('department_id'))

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=user).order_by('-created_at')

    # def perform_create(self, serializer):
    #     serializer.save(
    #         user=self.request.user,
    #         department_id=self.request.data.get("department"),
    #         college_id=self.request.data.get("college"),
    #     )

    


    @action(detail=True, methods=['patch'], serializer_class=OrderStatusUpdateSerializer)
    def update_status(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def dashboard_metrics(self, request):
        """
        Returns dashboard metrics similar to your existing function
        """
        today = timezone.now().date()
        month_start = today.replace(day=1)
        active_orders = Order.objects.exclude(status="canceled")

        total_sales = active_orders.aggregate(total=Sum("total_amount"))["total"] or 0
        today_sales = active_orders.filter(created_at__date=today).aggregate(total=Sum("total_amount"))["total"] or 0
        month_sales = active_orders.filter(created_at__date__gte=month_start).aggregate(total=Sum("total_amount"))["total"] or 0

        total_orders = Order.objects.count()
        completed_orders = Order.objects.filter(status="completed").count()
        pending_orders = Order.objects.filter(status="pending").count()
        canceled_orders = Order.objects.filter(status="canceled").count()
        avg_order_value = total_sales / completed_orders if completed_orders > 0 else 0
        credit_amount = Order.objects.filter(status="pending").aggregate(total=Sum("total_amount"))["total"] or 0
        collection_rate = (completed_orders / total_orders) * 100 if total_orders > 0 else 0

        top_items = (
            OrderItem.objects
            .values(name=F("menu_item__name"))
            .annotate(
                qty_sold=Sum("quantity"),
                revenue=Sum(F("quantity") * F("price"))
            )
            .order_by("-qty_sold")[:5]
        )

        return Response({
            "sales": {
                "total": total_sales,
                "today": today_sales,
                "month": month_sales,
                "avg_order_value": round(avg_order_value, 2),
            },
            "orders": {
                "total": total_orders,
                "completed": completed_orders,
                "pending": pending_orders,
                "canceled": canceled_orders,
            },
            "credit": {
                "outstanding_amount": credit_amount,
                "credit_orders": pending_orders,
                "collection_rate_percent": round(collection_rate, 1),
            },
            "top_items": list(top_items)
        })
