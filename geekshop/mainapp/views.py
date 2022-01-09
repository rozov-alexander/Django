from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from cartproductsapp.models import Cart
import random


menu_links = [
    {'view_name': 'index', 'active_if': ["index"], 'name': 'Домой'},
    {
        'view_name': 'products:index',
        'active_if': ['products:index', 'products:category'],
        'name': 'Продукты'
    },
    {'view_name': 'contact', 'active_if': ["contact"], 'name': 'Контакты'},
]

def get_cart(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.choice(products)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category)
    return same_products

def index(request):
    cart = get_cart(request.user)
    products = Product.objects.all()[:4]

    return render(request, 'mainapp/index.html', context={
        'menu_links': menu_links,
        'title': 'главная',
        'products': products,
        'cart': cart,
        })


def contact(request):
    cart = get_cart(request.user)

    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links,
        'title': 'контакты',
        'cart': cart,
        })


def products(request, pk=None):
    title = 'продукты'
    cart = get_cart(request.user)
    if not pk:
        current_category = ProductCategory.objects.first()
    else:
        current_category = get_object_or_404(ProductCategory, id=pk)
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=current_category)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = { 
        'title': title,
        'menu_links': menu_links,
        'hot_product': hot_product,
        'categories': categories,
        'products': products,
        'same_products': same_products,
        'cart': cart,
}
    
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'cart': get_cart(request.user),
    }
    return render(request, 'mainapp/product.html', content)
