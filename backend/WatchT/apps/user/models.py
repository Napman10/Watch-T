from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth.models import User
from ..abstract.models import BaseModel
from ..abstract.validators import is_int_validate, non_negative_int_validate


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
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Роль', default=GUEST)

    objects = Manager()

    def __str__(self):
        return self.user.username


class UserStatistics(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Статистика о пользователе'
        verbose_name_plural = 'Статистика о пользователях'

    user = models.OneToOneField(EmployeeUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    joined = models.DateTimeField(verbose_name='Дата присоединения к команде', auto_now_add=True)
    tracked_minutes = models.IntegerField(verbose_name='Затреканные минуты (всего)', default=0,
                                          validators=[is_int_validate, non_negative_int_validate])
