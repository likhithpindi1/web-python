# Generated by Django 4.1.5 on 2023-02-25 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_register_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Email_ID',
            field=models.EmailField(max_length=50),
        ),
    ]
