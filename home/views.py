from django.shortcuts import render
from .models import categories as categories_model

# Create your views here.

def get_home(request):
    print('this is request: ', request)
    list_categories = categories_model.objects.filter().order_by('category_id') # = SELETC * FROM categories
    return render(request, 'home.html', {'list_categories': list_categories})