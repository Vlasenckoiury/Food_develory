from django.shortcuts import render
from .models import Pizza


def menu(request):
    pizza = Pizza.objects.all()
    return render(request, 'menu/all_menu.html', {'pizza':pizza})
