# Generated by Django 4.1.5 on 2023-02-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_service_re_enter_passwords'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=256)),
                ('Email_ID', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='service',
        ),
    ]
