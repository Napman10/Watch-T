# Generated by Django 2.2.6 on 2021-02-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeuser',
            name='first_name',
            field=models.CharField(blank=True, default='Name', max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employeeuser',
            name='last_name',
            field=models.CharField(blank=True, default='Surname', max_length=30, verbose_name='Фамилия'),
        ),
    ]
