# Generated by Django 4.1.5 on 2023-02-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_register_delete_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
