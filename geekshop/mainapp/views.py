from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from cartproductsapp.models import Cart
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


top_menu_links = [
    {"view_name": "index", "active_if": ["index"], "name": "Домой"},
    {
        "view_name": "products:index",
        "active_if": ["products:index", "products:category"],
        "name": "Продукты",
    },
    {"view_name": "contact", "active_if": ["contact"], "name": "Контакты"},
]


def get_hot_product():
    products = Product.objects.all()

    return random.choice(products)


# def get_same_products(hot_product):
#     same_products = Product.objects.filter(category=hot_product.category).order_by("id")
#     return same_products


def index(request):
    products = Product.objects.all()[:4]

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
    return render(
        request,
        "mainapp/contact.html",
        context={
            "top_menu_links": top_menu_links,
            "title": "контакты",
        },
    )


def products(request, pk=None, page=1):
    title = "продукты"
    categories_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
                }
            products = Product.objects.filter(is_active=True, \
                        category__is_active=True).order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, \
                        is_active=True, category__is_active=True).order_by('price')
        # paginator = Paginator(products, 2)
        # try:
        #     products_paginator = paginator.page(page)
        # except PageNotAnInteger:
        #     products_paginator = paginator.page(1)
        # except EmptyPage:
        #     products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'top_menu_links': top_menu_links,
            'categories_menu': categories_menu,
            'category': category,
            'products': products,
        }
        return render(request, 'mainapp/products_list.html', content)

    # if not pk:
    #     current_category = ProductCategory.objects.first()
    # else:
    #     current_category = get_object_or_404(ProductCategory, id=pk)
    # categories = ProductCategory.objects.all()
    # products = Product.objects.filter(category=current_category)
    if not pk:
        category = ProductCategory.objects.first()
    hot_product = get_hot_product()
    # paginator = Paginator(same_products, 3)
    # try:
    #     products_paginator = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paginator = paginator.page(1)
    # except EmptyPage:
    #     products_paginator = paginator.page(paginator.num_pages)
    # content = {
    #     "title": title,
    #     "menu_links": menu_links,
    #     "hot_product": hot_product,
    #     "categories": categories,
    #     "products": products_paginator,
    #     "current_category": current_category,
    # }
    same_products = Product.objects.all()[3:6]
    content = { 
        'title': title,
        'top_menu_links': top_menu_links,
        'categories_menu': categories_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'category': category,
        }
    return render(request, "mainapp/products.html", content)


def product(request, pk):
    title = "продукты"
    categories_menu = ProductCategory.objects.all()
    content = {
        "title": title,
        "top_menu_links": top_menu_links,
        "categories_menu": categories_menu,
        "product": get_object_or_404(Product, pk=pk),
    }
    return render(request, "mainapp/product.html", content)
