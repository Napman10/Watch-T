# Generated by Django 2.2.6 on 2021-03-25 13:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0010_auto_20210325_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueHistoryRecord',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255, verbose_name='Описание')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issue.Issue', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'История задачи',
                'verbose_name_plural': 'Истории задач',
            },
        ),
    ]