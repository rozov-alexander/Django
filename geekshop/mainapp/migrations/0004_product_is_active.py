# Generated by Django 3.2.10 on 2022-01-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_productcategory_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="активный"),
        ),
    ]
