from django.db import models
from django.db.models import Manager

from ..abstract.models import BaseModel
from ..user.models import EmployeeUser


class Project(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    short_name = models.CharField(max_length=16, verbose_name='Короткое название', unique=True)
    header = models.CharField(max_length=65, verbose_name='Заголовок', default='Не подписано')
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.short_name


class Project2User(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Связка Проект -> Сотрудник'
        verbose_name_plural = 'Связки Проект -> Сотрудник'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    user = models.ForeignKey(EmployeeUser, on_delete=models.CASCADE, verbose_name='Сотрудник')


class ProjectStatistics(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Статистика о проектах'
        verbose_name_plural = 'Статистика о проекте'

    project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name='Проект')
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    tracked_minutes = models.IntegerField(verbose_name='Затреканные минуты (всего)', default=0)
