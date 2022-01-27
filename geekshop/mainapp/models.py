from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)
    is_active = models.BooleanField(verbose_name="активна", default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=128, unique=True)
    image = models.ImageField(upload_to="products_images", blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    short_desc = models.CharField(
        verbose_name="короткое описание", max_length=64, blank=True
    )
    price = models.DecimalField(
        verbose_name="цена", max_digits=8, decimal_places=2, default=0
    )
    price_with_discount = models.DecimalField(
        verbose_name="цена со скидкой", max_digits=8, decimal_places=2, default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество на складе", default=0
    )
    is_active = models.BooleanField(verbose_name="активный", default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    @property
    def total_cost(self):
        return self.price * self.quantity
