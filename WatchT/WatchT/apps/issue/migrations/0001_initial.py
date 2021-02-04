# Generated by Django 2.2.6 on 2021-02-04 06:14

import WatchT.apps.abstract.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=16, unique=True, verbose_name='Короткое название')),
                ('header', models.CharField(blank=True, max_length=65, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('priority', models.IntegerField(choices=[(0, 'Низкий'), (1, 'Обычный'), (2, 'Высокий'), (3, 'Критический')], default=1, verbose_name='Приоритет')),
                ('status', models.IntegerField(choices=[(0, 'Новая'), (1, 'Требуется уточнение'), (2, 'Назначена'), (3, 'В работе'), (4, 'Проверка'), (5, 'Готово')], default=0, verbose_name='Статус')),
                ('want_minutes', models.IntegerField(validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Оценка')),
                ('got_minutes', models.IntegerField(validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Затрачено')),
                ('level', models.IntegerField(default=1, validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Уровень вложенности')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_task', to='user.CustomUser', verbose_name='Составил')),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor_task', to='user.CustomUser', verbose_name='Выполняет')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issue.Issue', verbose_name='Родительская задача')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255, verbose_name='Текст комментария')),
                ('datetime', models.DateTimeField()),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.CustomUser', verbose_name='Комментатор')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issue.Issue')),
            ],
            options={
                'verbose_name': 'Комментарий к задаче',
                'verbose_name_plural': 'Комментарии к задачам',
            },
        ),
    ]
