from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryEditForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def categories(request):
    title = "админка/категории"
    categories_list = ProductCategory.objects.all()
    content = {"title": title, "objects": categories_list}
    return render(request, "adminapp/categories.html", content)


# Class Based View
class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"


# Class Based View
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "категории/редактирование"

        return context


# Class Based View
class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("admin:categories")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# Old view, without CBV (Function Based View)
# def category_create(request):
#     title = 'категории/создание'

#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryEditForm()

#     content = {'title': title, 'update_form': category_form}

#     return render(request, 'adminapp/category_update.html', content)


# def category_update(request, pk):
#     title = 'категории/редактирование'

#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES,instance=edit_category)

#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)

#     content = {'title': title, 'update_form': edit_form}

#     return render(request, 'adminapp/category_update.html', content)


# def category_delete(request, pk):
#     title = 'категории/удаление'

#     category = get_object_or_404(ProductCategory, pk=pk)

#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin:categories'))

#     content = {'title': title, 'category_to_delete': category}

#     return render(request, 'adminapp/category_delete.html', content)
