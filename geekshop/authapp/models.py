from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=14, blank=True)
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
