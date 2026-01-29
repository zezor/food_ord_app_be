from django.urls import path
from .views import (
    CreateOrderAPIView,
    MyOrdersAPIView,
    KitchenSummaryAPIView,
    FinancialSummaryAPIView
)

urlpatterns = [
    path('', CreateOrderAPIView.as_view()),
    path('my/', MyOrdersAPIView.as_view()),
    path('kitchen_summary/', KitchenSummaryAPIView.as_view()),
    path('financial_summary/', FinancialSummaryAPIView.as_view()),
]
