# Generated by Django 2.2.6 on 2021-02-25 07:12

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=16, unique=True, verbose_name='Короткое название')),
                ('header', models.CharField(default='Не подписано', max_length=65, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Project2User',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.EmployeeUser', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Связка Проект -> Сотрудник',
                'verbose_name_plural': 'Связки Проект -> Сотрудник',
            },
        ),
    ]
