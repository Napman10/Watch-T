# Generated by Django 2.2.12 on 2021-04-12 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0011_issuehistoryrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создано'),
            preserve_default=False,
        ),
    ]
