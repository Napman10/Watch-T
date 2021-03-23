# Generated by Django 2.2.6 on 2021-03-23 13:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatistics',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('joined', models.DateTimeField(verbose_name='Дата присоединения к команде')),
                ('tracked_minutes', models.IntegerField(verbose_name='Затреканные минуты (всего)')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.EmployeeUser')),
            ],
            options={
                'verbose_name': 'Статистика о пользователях',
                'verbose_name_plural': 'Статистика о пользователе',
            },
        ),
    ]
