# Generated by Django 2.2.6 on 2021-02-02 11:40

import WatchT.apps.user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='default_user_pic.jpg', upload_to=WatchT.apps.user.models.user_photo_upload_to),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
