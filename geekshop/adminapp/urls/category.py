import adminapp.views as adminapp
from django.urls import path

from adminapp.views import category


urlpatterns = [
    path(
        "categories/create/",
        category.ProductCategoryCreateView.as_view(),
        name="category_create",
    ),
    path("categories/read/", category.categories, name="categories"),
    path(
        "categories/update/<int:pk>/",
        category.ProductCategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        category.ProductCategoryDeleteView.as_view(),
        name="category_delete",
    ),
]
