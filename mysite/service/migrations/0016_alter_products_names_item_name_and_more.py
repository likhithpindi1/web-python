# Generated by Django 4.1.5 on 2023-03-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_products_names_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_names',
            name='item_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='products_names',
            name='price',
            field=models.CharField(max_length=250),
        ),
    ]
