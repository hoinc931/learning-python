from django.contrib import admin
from django.db import models
from .models import products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'category_id', 'image')
    search_fields = ['name', 'description']
    list_filter = ('product_id', 'name', 'description', 'category_id')

admin.site.register(products, ProductsAdmin)