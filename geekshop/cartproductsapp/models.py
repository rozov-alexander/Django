from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product

class Cart(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created_time = models.DateTimeField(verbose_name='время', auto_now_add=True)


