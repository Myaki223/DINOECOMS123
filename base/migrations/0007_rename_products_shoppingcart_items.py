# Generated by Django 4.1.7 on 2023-05-05 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_cartitem_alter_product_image_shoppingcart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='products',
            new_name='items',
        ),
    ]