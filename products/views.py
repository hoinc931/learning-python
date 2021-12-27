from django.shortcuts import render
from .models import products as products_model
from home.models import categories as categories_model

# Create your views here.

def first_read(request, id):
    list_products = products_model.objects.filter(category_id = id).order_by("product_id")
    category = categories_model.objects.get(category_id = id)
    return render(request, 'product.html', {'list_products': list_products, 'category': category})