# Generated by Django 2.2.6 on 2021-02-02 09:41

import WatchT.apps.abstract.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20210202_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='got_minutes',
            field=models.IntegerField(validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Затрачено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='want_minutes',
            field=models.IntegerField(validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Оценка'),
        ),
    ]