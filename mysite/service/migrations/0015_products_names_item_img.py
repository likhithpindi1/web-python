# Generated by Django 4.1.5 on 2023-03-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_alter_products_names_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_names',
            name='item_img',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/%d'),
        ),
    ]