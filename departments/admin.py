from django.contrib import admin
from .models import Department, College

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'contact_person', 'phone')
    search_fields = ('name', 'contact_person', 'phone')
    list_filter = ('college',)
admin.site.register(Department, DepartmentAdmin)

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

admin.site.register(College, CollegeAdmin)