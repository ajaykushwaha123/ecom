# Generated by Django 5.1.4 on 2025-01-22 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_cartitems'),
        ('products', '0004_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon'),
        ),
    ]