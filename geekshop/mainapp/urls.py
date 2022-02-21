from django.urls import path, re_path
from django.views.decorators.cache import cache_page

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
    # re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'), 
    # re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    path("category/<int:pk>/", mainapp.products, name="category"),
    path("page/<int:page>/", mainapp.products, name="page"),
    path("product/<int:pk>/", mainapp.product, name="product"),

    path("category/<int:pk>/ajax/", cache_page(3600)(mainapp.products_ajax), name="products_ajax"),
    # path("category/<int:pk>/page/<int:page>/ajax/", cache_page(3600)(mainapp.products_ajax), name="page_ajax"),
]
