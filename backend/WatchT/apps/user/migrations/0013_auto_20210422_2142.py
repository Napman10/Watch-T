# Generated by Django 2.2.12 on 2021-04-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_employeeuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeuser',
            name='level',
            field=models.IntegerField(choices=[(0, 'Стажер'), (1, 'Джуниор'), (2, 'Миддл'), (3, 'Сеньор')], default=0, verbose_name='Позиция'),
        ),
    ]
