from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryEditForm


def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
        }
    return render(request, 'adminapp/categories.html', content) 
    
    
def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES) 
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()
    
    content = {'title': title, 'update_form': category_form}
    
    return render(request, 'adminapp/category_update.html', content)


def category_update(request, pk):
    title = 'категории/редактирование'
    
    edit_category = get_object_or_404(ProductCategory, pk=pk) 
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES,instance=edit_category)
        
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk])) 
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}
    
    return render(request, 'adminapp/category_update.html', content)


def category_delete(request, pk): 
    title = 'категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST': 
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)
