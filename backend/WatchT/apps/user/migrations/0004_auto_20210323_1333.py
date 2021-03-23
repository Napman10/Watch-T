# Generated by Django 2.2.6 on 2021-03-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210323_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatistics',
            name='joined',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата присоединения к команде'),
        ),
        migrations.AlterField(
            model_name='userstatistics',
            name='tracked_minutes',
            field=models.IntegerField(default=0, verbose_name='Затреканные минуты (всего)'),
        ),
    ]
