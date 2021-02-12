# Generated by Django 2.2.6 on 2021-02-12 14:08

import WatchT.apps.abstract.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255, verbose_name='Текст комментария')),
                ('datetime', models.DateTimeField(verbose_name='Дата создания')),
                ('edited', models.BooleanField(default=False, verbose_name='Редактировано')),
            ],
            options={
                'verbose_name': 'Комментарий к задаче',
                'verbose_name_plural': 'Комментарии к задачам',
            },
        ),
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
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='TrackTime',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('minutes', models.IntegerField(validators=[WatchT.apps.abstract.validators.is_int_validate, WatchT.apps.abstract.validators.bigger_than_zero_validate], verbose_name='Время в минутах')),
            ],
            options={
                'verbose_name': 'Затреканное время',
                'verbose_name_plural': 'Затреканное время',
            },
        ),
    ]
