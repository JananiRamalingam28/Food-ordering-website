# Generated by Django 5.0.1 on 2024-03-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_chin_rating_alter_des_rating_alter_ital_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(default='', max_length=30)),
            ],
        ),
    ]