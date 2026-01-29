from django.urls import path
from .views import PaymentAPIView


urlpatterns = [
    path('payments/', PaymentAPIView.as_view()),]