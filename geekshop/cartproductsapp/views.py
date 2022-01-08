from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from .models import Cart


def cart(request):
    content = {
        'cart_total': len(request.user.cart.all()),
    }
    return render(request, 'cartproductsapp/cart.html', content)


def add_to_cart(request, pk=None):
    product = get_object_or_404(Product, pk=pk)

    cart_product = request.user.cart.filter(id=pk).first()
    # import pdb; pdb.set_trace()
    if not cart_product:
        cart_product = Cart(user=request.user, product=product)

    cart_product.quantity += 1
    cart_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, pk):
    return render(request, 'cartproductsapp/cart.html')
