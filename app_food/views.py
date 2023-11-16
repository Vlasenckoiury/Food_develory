from django.shortcuts import render


def index(request):
    return render(request, 'app_food/all_food.html')


def contact(request):
    return render(request, 'app_food/contact.html')
