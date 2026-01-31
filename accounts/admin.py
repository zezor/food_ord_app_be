from django.contrib import admin
from .models import CustomUser, CustomUserManager

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_active', 'date_joined', 'department')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
admin.site.register(CustomUser, UserAdmin)


