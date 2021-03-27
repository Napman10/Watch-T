# Generated by Django 2.2.6 on 2021-03-25 09:00

import WatchT.apps.abstract.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210325_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatistics',
            name='joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата присоединения к команде'),
        ),
        migrations.AlterField(
            model_name='userstatistics',
            name='tracked_minutes',
            field=models.IntegerField(default=0, validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.non_negative_int_validate], verbose_name='Затреканные минуты (всего)'),
        ),
    ]