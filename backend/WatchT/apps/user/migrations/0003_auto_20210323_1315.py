# Generated by Django 2.2.6 on 2021-03-23 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userstatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatistics',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.EmployeeUser', verbose_name='Пользователь'),
        ),
    ]
