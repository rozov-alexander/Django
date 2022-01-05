from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from cartproductsapp.models import Cart


menu_links = [
    {'view_name': 'index', 'name': 'Домой'},
    {'view_name': 'products:index', 'name': 'Продукты'},
    {'view_name': 'contact', 'name': 'Контакты'},
]


def index(request):
    products = Product.objects.all()[:4]

    return render(request, 'mainapp/index.html', context={
        'menu_links': menu_links,
        'title': 'главная',
        'products': products,
        })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links,
        'title': 'контакты'
        })


def products(request, pk=None, id=None):
    if not pk:
        current_category = ProductCategory.objects.first()
    else:
        current_category = get_object_or_404(ProductCategory, id=pk)
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=current_category)
    cart = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    
    return render(request, 'mainapp/products.html', context={
        'menu_links': menu_links,
        'title': 'продукты',
        'categories': categories,
        'current_category': current_category,
        'products': products,
        'cart': cart,
        })

