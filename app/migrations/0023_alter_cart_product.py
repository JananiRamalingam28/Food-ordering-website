# Generated by Django 5.0.1 on 2024-03-25 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pro'),
        ),
    ]
