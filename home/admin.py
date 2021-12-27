from django.contrib import admin
from .models import categories

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name')
    search_fields = ['name']
    list_filter = ('category_id', 'name')

admin.site.register(categories, CategoriesAdmin)