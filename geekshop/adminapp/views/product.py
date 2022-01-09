from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from mainapp.models import ProductCategory, Product
from adminapp.forms import ProductEditForm



def products(request, pk): 
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list,
        }
    return render(request, 'adminapp/products.html', content) 
    
    
def product_create(request, pk):
    title = 'продукт/создание'
     
    category = pk

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES) 
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[category]))
    else:
        product_form = ProductEditForm()
  
    content = {'title': title, 'update_form': product_form, 'category': category}
    
    return render(request, 'adminapp/product_update.html', content)



def product_read(request, pk): 
    pass


def product_update(request, pk): 
    title = 'продукт/редактирование'
    
    edit_product = get_object_or_404(Product, pk=pk)
    category = edit_product.category.pk
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES,instance=edit_product)
        
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[category])) 
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': category}
    
    return render(request, 'adminapp/product_update.html', content)


def product_delete(request, pk): 
    title = 'продукт/удаление'
    product = get_object_or_404(Product, pk=pk)
    category = product.category.pk

    if request.method == 'POST': 
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[category]))

    content = {'title': title, 'product_to_delete': product, 'category': category}

    return render(request, 'adminapp/product_delete.html', content)
