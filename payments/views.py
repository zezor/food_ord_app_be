from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Payment

# Create your views here.
class PaymentAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = None  # Replace with your Payment serializer