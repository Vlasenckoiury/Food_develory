from django.shortcuts import render


def menu(request):
    return render(request, 'menu/all_menu.html')
