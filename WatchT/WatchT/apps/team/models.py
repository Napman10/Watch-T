from ..abstract.models import BaseModel
from ..user.models import CustomUser
from django.db.models import Manager
from django.db import models


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
