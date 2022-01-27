from django.urls import path

from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path("", views.products, name="index"),
    path("category/<int:pk>/", views.products, name="category"),
    path("page/<int:page>/", views.products, name="page"),
    path("product/<int:pk>/", views.product, name="product"),
]
