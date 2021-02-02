from ..abstract.models import BaseModel
from ..user.models import User, Team
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


class Task(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    short_name = models.CharField(max_length=16, verbose_name='Короткое название', unique=True)
    header = models.CharField(max_length=65, verbose_name='Заголовок', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, verbose_name='Составил', on_delete=models.SET_NULL,
                               null=True, related_name='author_task')
    executor = models.ForeignKey(User, verbose_name='Выполняет', on_delete=models.SET_NULL,
                                 null=True, related_name='executor_task')

    def __str__(self):
        return self.short_name
