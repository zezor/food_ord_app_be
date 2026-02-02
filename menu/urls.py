from django.urls import path,include
from .views import MenuListAPIView
from .views import CategoryListAPIView
from .views import MenuByCategoryAPIView

urlpatterns = [
    path('', MenuListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/items/', MenuByCategoryAPIView.as_view()),
    
]
