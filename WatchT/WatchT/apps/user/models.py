from django.db import models, transaction
from django.db.models.manager import Manager
from django.contrib.auth.models import User
from ..abstract.models import BaseModel


def user_photo_upload_to(instance, filename):
    return f'user/{instance.id}/{filename}'


class EmployeeUser(BaseModel):
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
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_photo_upload_to, default='default_user_pic.jpg', verbose_name='Фото')
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Роль', default=GUEST)

    objects = Manager()

    def __str__(self):
        return self.user.username
