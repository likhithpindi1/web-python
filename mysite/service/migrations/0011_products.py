# Generated by Django 4.1.5 on 2023-03-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_register_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_img', models.ImageField(blank=True, upload_to='img/%Y/%m/%d')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
