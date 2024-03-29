# Generated by Django 2.2.6 on 2021-03-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectstatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstatistics',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='projectstatistics',
            name='tracked_minutes',
            field=models.IntegerField(default=0, verbose_name='Затреканные минуты (всего)'),
        ),
    ]
