from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .models import Order, OrderItem
from .serializers import OrderSerializer

class CreateOrderAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}


class MyOrdersAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class KitchenSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = (
            OrderItem.objects
            .values('menu_item__name')
            .annotate(total_quantity=Sum('quantity'))
        )
        return Response(data)


class FinancialSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_sales = Order.objects.aggregate(total=Sum('total_amount'))
        return Response(total_sales)
