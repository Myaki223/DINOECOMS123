# Generated by Django 4.1.7 on 2023-05-05 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_rename_products_shoppingcart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='items',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]