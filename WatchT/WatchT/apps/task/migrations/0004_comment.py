# Generated by Django 2.2.6 on 2021-02-02 08:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210202_0816'),
        ('task', '0003_auto_20210202_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(db_column='Id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255, verbose_name='Текст комментария')),
                ('datetime', models.DateTimeField()),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User', verbose_name='Комментатор')),
            ],
            options={
                'verbose_name': 'Комментарий к задаче',
                'verbose_name_plural': 'Комментарии к задачам',
            },
        ),
    ]
