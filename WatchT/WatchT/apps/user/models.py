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
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_photo_upload_to, default='default_user_pic.jpg')
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Роль', default=GUEST)

    def __str__(self):
        return self.user.username


class Team(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Команда сотрудников'
        verbose_name_plural = 'Команды сотрудников'

    name = models.CharField(max_length=65, verbose_name='Название', unique=True)
    description = models.CharField(max_length=255, verbose_name='Описание команды', null=True, blank=True)

    def __str__(self):
        return self.name


class User2Team(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Связка Пользователь -> Команда'
        verbose_name_plural = 'Связки Пользователь -> Команда'

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
