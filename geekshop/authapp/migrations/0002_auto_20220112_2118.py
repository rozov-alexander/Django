# Generated by Django 3.2.10 on 2022-01-12 21:18

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopuser",
            name="activation_expiration_date",
            field=models.DateTimeField(
                default=authapp.models.default_key_expiration_date,
                verbose_name="дата протухания ключа активации",
            ),
        ),
        migrations.AddField(
            model_name="shopuser",
            name="activation_key",
            field=models.CharField(
                max_length=128, null=True, verbose_name="ключ активации"
            ),
        ),
    ]
