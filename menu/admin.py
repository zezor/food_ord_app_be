from django.contrib import admin
from .models import MenuItem, Category

# Register your models here.
class CustomAdminSite(admin.AdminSite):
    site_header = "Food Ordering App Admin"
    site_title = "Food Ordering App Admin Portal"
    index_title = "Welcome to Food Ordering App Admin"
admin_site = CustomAdminSite(name='custom_admin')

admin_site.index_title = "Welcome to Food Ordering App Admin Portal"    
admin_site.site_header = "Food Ordering App Administration"
admin_site.site_title = "Food Ordering App Admin"
admin.site = admin_site

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'category', 'created_at', 'updated_at')
    list_filter = ('is_available', 'category')
    search_fields = ('name',)
admin.site.register(MenuItem, MenuItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)