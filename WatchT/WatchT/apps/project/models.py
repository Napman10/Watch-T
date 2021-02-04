from ..abstract.models import BaseModel
from django.db.models import Manager
from django.db import models
from ..user.models import CustomUser


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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Сотрудник')
