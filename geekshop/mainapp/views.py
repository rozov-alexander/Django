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
    products = [
        {'product_name': 'product1', 'img': 'img/product-11.jpg', 'desc': 'Стул повышенного качества'},
        {'product_name': 'product2', 'img': 'img/product-21.jpg', 'desc': 'Стул чёткий'},
        {'product_name': 'product3', 'img': 'img/product-31.jpg', 'desc': 'Стул третий'},
    ]
    return render(request, 'mainapp/products.html', context={'menu_links': menu_links, 'products': products, 'title': 'продукты'})
