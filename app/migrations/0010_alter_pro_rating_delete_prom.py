# Generated by Django 5.0.1 on 2024-03-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_sou_description_alter_sou_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Prom',
        ),
    ]