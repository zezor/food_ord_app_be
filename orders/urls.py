from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
# router.register(r'dashboard_metrics', OrderViewSet, basename='dashboard_metrics')

urlpatterns = [
    path('', include(router.urls)),
]
