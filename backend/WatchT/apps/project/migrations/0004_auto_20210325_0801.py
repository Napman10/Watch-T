# Generated by Django 2.2.6 on 2021-03-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210323_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectstatistics',
            options={'verbose_name': 'Статистика о проекте', 'verbose_name_plural': 'Статистика о проектах'},
        ),
    ]
