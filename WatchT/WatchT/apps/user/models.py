from ..abstract.models import BaseModel
from django.db.models import Manager
from django.db import models
from django.contrib.auth.models import User


def user_photo_upload_to(instance, filename):
    return f'user/{instance.id}/{filename}'


class CustomUser(BaseModel):
    objects = Manager()

    GUEST = 0
    DEVELOPER = 1
    ANALYST = 2
    LEAD = 3
    ADMINISTRATOR = 4

    ROLE_CHOICES = (
        (GUEST, 'Гость'),
        (DEVELOPER, 'Разработчик'),
        (ANALYST, 'Аналитик'),
        (LEAD, 'Тимлид'),
        (ADMINISTRATOR, 'Администратор сайта'),
    )

    class Meta:
        verbose_name = 'Расширение пользователя'
        verbose_name_plural = 'Расширения пользователей'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    photo = models.ImageField(upload_to=user_photo_upload_to, default='default_user_pic.jpg', verbose_name='Фото')
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Роль', default=GUEST)

    def __str__(self):
        return self.user.username
