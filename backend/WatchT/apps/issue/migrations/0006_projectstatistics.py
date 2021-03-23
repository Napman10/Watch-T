# Generated by Django 2.2.6 on 2021-03-23 13:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('issue', '0005_tracktime_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatistics',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='Дата создания')),
                ('tracked_minutes', models.IntegerField(verbose_name='Затреканные минуты (всего)')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name': 'Статистика о проектах',
                'verbose_name_plural': 'Статистика о проекте',
            },
        ),
    ]
