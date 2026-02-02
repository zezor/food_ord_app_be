from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, CollegeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'colleges', CollegeViewSet)


urlpatterns = [    path('', include(router.urls)),
]