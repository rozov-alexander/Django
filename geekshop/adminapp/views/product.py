from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from mainapp.models import ProductCategory, Product
from adminapp.forms import ProductEditForm
from django.views.generic.detail import DetailView


def products(request, pk):
    title = "админка/продукт"
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by("name")
    content = {
        "title": title,
        "category": category,
        "objects": products_list,
    }
    return render(request, "adminapp/products.html", content)


def product_create(request, pk):
    title = "продукт/создание"

    category = get_object_or_404(ProductCategory, pk=pk).pk
    
    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("admin:products", args=[pk]))
    else:
        product_form = ProductEditForm(initial={"category": category})

    content = {"title": title, "update_form": product_form, "category": category}

    return render(request, "adminapp/product_update.html", content)


# Class Based View
class ProductDetailView(DetailView):
    model = Product
    template_name = "adminapp/product_read.html"


# Old view, without CBV (Function Based View)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     content = {'title': title, 'object': product,}

#     return render(request, 'adminapp/product_read.html', content)


def product_update(request, pk):
    title = "продукт/редактирование"

    edit_product = get_object_or_404(Product, pk=pk)
    category = edit_product.category.pk
    if request.method == "POST":
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(
                reverse("admin:product_update", args=[edit_product.pk])
            )
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {"title": title, "update_form": edit_form, "category": category}

    return render(request, "adminapp/product_update.html", content)


def product_delete(request, pk):
    title = "продукт/удаление"

    product = get_object_or_404(Product, pk=pk)
    category = product.category.pk
    pk = product.category.pk

    if request.method == "POST":
        # product.is_active = False
        # product.save()
        product.delete()
        return HttpResponseRedirect(reverse("admin:products", args=[pk]))

    content = {"title": title, "product_to_delete": product, "category": category}

    return render(request, "adminapp/product_delete.html", content)
