# Generated by Django 4.1.5 on 2023-02-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_register_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Email_ID',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
