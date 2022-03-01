from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from cartproductsapp.models import Cart
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings 
from django.core.cache import cache
from django.views.decorators.cache import cache_page


top_menu_links = [
    {"view_name": "index", "active_if": ["index"], "name": "Домой"},
    {
        "view_name": "products:index",
        "active_if": ["products:index", "products:category"],
        "name": "Продукты",
    },
    {"view_name": "contact", "active_if": ["contact"], "name": "Контакты"},
]

def get_links_menu():
    if settings.LOW_CACHE: 
        key = 'categories_menu'
        categories_menu = cache.get(key)
        if categories_menu is None:
            categories_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, categories_menu)
        return categories_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key) 
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category) 
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key) 
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}' 
        product = cache.get(key) 
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price(): 
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk): 
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}' 
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')


def get_hot_product():
    products = get_products()

    return random.choice(products)


# def get_same_products(hot_product):
#     same_products = Product.objects.filter(category=hot_product.category).order_by("id")
#     return same_products


def index(request):
    products = get_products()[:3]

    return render(
        request,
        "mainapp/index.html",
        context={
            "top_menu_links": top_menu_links,
            "title": "главная",
            "products": products,
        },
    )


def contact(request):
    title = 'о нас'

    return render(
        request,
        "mainapp/contact.html",
        context={
            "top_menu_links": top_menu_links,
            "title": title,
        },
    )

@cache_page(3600)
def products(request, pk=None, page=1):
    title = "продукты"
    categories_menu = get_links_menu()

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = get_products_orederd_by_price()
        else:
            category = get_category(pk)
            products = get_products_in_category_orederd_by_price(pk)

        content = {
            "title": title,
            "top_menu_links": top_menu_links,
            "categories_menu": categories_menu,
            "category": category,
            "products": products,
        }
        return render(request, "mainapp/products_list.html", content)

    if not pk:
        category = ProductCategory.objects.first()
    hot_product = get_hot_product()
    same_products = Product.objects.all()[3:6]
    content = {
        "title": title,
        "top_menu_links": top_menu_links,
        "categories_menu": categories_menu,
        "hot_product": hot_product,
        "same_products": same_products,
        "category": category,
    }
    return render(request, "mainapp/products.html", content)


def product(request, pk):
    title = "продукты"
    categories_menu = get_links_menu()
    content = {
        "title": title,
        "top_menu_links": top_menu_links,
        "categories_menu": categories_menu,
        "product": get_product(pk),
    }
    return render(request, "mainapp/product.html", content)


def products_ajax(request, pk=None, page=1):
    title = "продукты"
    categories_menu = get_links_menu()

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = get_products_orederd_by_price()
        else:
            category = get_category(pk)
            products = get_products_in_category_orederd_by_price(pk)

        content = {
            "title": title,
            "top_menu_links": top_menu_links,
            "categories_menu": categories_menu,
            "category": category,
            "products": products,
        }
        return render(request, "mainapp/includes/inc_products_list_content.html", content)

    if not pk:
        category = ProductCategory.objects.first()
    hot_product = get_hot_product()
    same_products = Product.objects.all()[3:6]
    content = {
        "title": title,
        "top_menu_links": top_menu_links,
        "categories_menu": categories_menu,
        "hot_product": hot_product,
        "same_products": same_products,
        "category": category,
    }
    return render(request, "mainapp/products.html", content)