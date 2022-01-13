from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def default_key_expiration_date():
    return timezone.now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=14, blank=True)
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    activation_key = models.CharField(verbose_name='ключ активации', max_length=128, null=True)
    activation_expiration_date = models.DateTimeField(
        verbose_name='дата протухания ключа активации', default=default_key_expiration_date)


    def is_activation_key_expired(self):
        return self.activation_expiration_date < timezone.now()