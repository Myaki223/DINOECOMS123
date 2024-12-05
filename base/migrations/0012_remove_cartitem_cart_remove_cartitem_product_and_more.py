# Generated by Django 4.1.7 on 2023-05-06 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]