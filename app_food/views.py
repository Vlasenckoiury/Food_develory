from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'app_food/all_food.html')


def menu(request):
    product = Product.objects.all()
    return render(request, 'app_food/all_menu.html', {'product':product})


def contact(request):
    return render(request, 'app_food/contact.html')
