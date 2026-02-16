from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser

    list_display = (
        "email",
        "full_name",
        "is_staff",
        "is_active",
        "date_joined",
        "department",
    )

    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("full_name", "phone_number", "department")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "full_name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)



admin.site.register(Group)
