# Generated by Django 2.2.12 on 2021-04-20 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0015_auto_20210420_2147'),
        ('user', '0010_auto_20210420_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Навык сотрудника', 'verbose_name_plural': 'Навыки сотрудников'},
        ),
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together={('employee', 'skill')},
        ),
    ]
