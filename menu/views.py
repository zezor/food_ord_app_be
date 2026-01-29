from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuListAPIView(ListAPIView):
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer

class CategoryListAPIView(ListAPIView):
    from .models import Category
    from .serializers import CategorySerializer

    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

class MenuByCategoryAPIView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return MenuItem.objects.filter(category_id=category_id, is_available=True)
