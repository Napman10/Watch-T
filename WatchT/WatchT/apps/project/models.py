from ..abstract.models import BaseModel
from ..team.models import Team
from django.db.models import Manager
from django.db import models


class Project(BaseModel):
    object = Manager()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    short_name = models.CharField(max_length=16, verbose_name='Короткое название', unique=True)
    header = models.CharField(max_length=65, verbose_name='Заголовок', default='Не подписано')
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    team = models.ForeignKey(Team, verbose_name='Команда, работающая над проектом',
                             on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.short_name
