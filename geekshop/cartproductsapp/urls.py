from django.urls import path

from . import views

app_name = "cartproductsapp"

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add/<int:pk>", views.add_to_cart, name="add_to_cart"),
    path("edit/<int:pk>/<int:quantity>/", views.cart_edit, name="edit"),
    path("remove/<int:pk>", views.remove_from_cart, name="remove_from_cart"),
]
