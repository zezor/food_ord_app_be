from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, College
from .serializers import DepartmentSerializer, CollegeSerializer

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer