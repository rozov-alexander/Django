from django.shortcuts import render


menu_links = [
        {'view_name': 'index', 'name': 'Домой'},
        {'view_name': 'products', 'name': 'Продукты'},
        {'view_name': 'contact', 'name': 'Контакты'},
    ]

def index(request):
    return render(request, 'mainapp/index.html', context={'menu_links': menu_links, 'title': 'главная'})


def contact(request):
    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links, 'title': 'контакты'})


def products(request):
    return render(request, 'mainapp/products.html', context={'menu_links': menu_links, 'title': 'продукты'})
