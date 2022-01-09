from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product

class Cart(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created_time = models.DateTimeField(verbose_name='время', auto_now_add=True)


    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity


    @property
    def total_quantity(self):
        "return total quantity for user"
        _items = Cart.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        "return total cost for user"
        _items = Cart.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost