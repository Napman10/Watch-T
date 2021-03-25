from django.db import models
from django.db.models import Manager

from ..abstract.models import BaseModel
from ..abstract.validators import is_int_validate, non_negative_int_validate, positive_int_validate
from ..project.models import Project
from ..user.models import EmployeeUser
from .managers import IssueManager, TrackTimeManager


class Issue(BaseModel):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    CRITICAL = 3

    PRIORITY_CHOICES = (
        (LOW, 'Низкий'),
        (NORMAL, 'Обычный'),
        (HIGH, 'Высокий'),
        (CRITICAL, 'Критический'),
    )

    NEW = 0
    CORRECTION = 1
    ASSIGNED = 2
    IN_PROGRESS = 3
    CHECK = 4
    DONE = 5

    STATUS_CHOICES = (
        (NEW, 'Новая'),
        (CORRECTION, 'Требуется уточнение'),
        (ASSIGNED, 'Назначена'),
        (IN_PROGRESS, 'В работе'),
        (CHECK, 'Проверка'),
        (DONE, 'Готово'),
    )

    objects = IssueManager()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    short_name = models.CharField(max_length=16, verbose_name='Короткое название', unique=True)
    header = models.CharField(max_length=65, verbose_name='Заголовок', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(EmployeeUser, verbose_name='Составил', on_delete=models.SET_NULL,
                               null=True, related_name='author_task')
    executor = models.ForeignKey(EmployeeUser, verbose_name='Выполняет', on_delete=models.SET_NULL,
                                 null=True, related_name='executor_task', blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=NORMAL, verbose_name='Приоритет')
    status = models.IntegerField(choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')
    want_minutes = models.IntegerField(validators=[is_int_validate, non_negative_int_validate], verbose_name='Оценка')
    got_minutes = models.IntegerField(validators=[is_int_validate, non_negative_int_validate], verbose_name='Затрачено')
    want_buffer_minutes = models.IntegerField(validators=[is_int_validate, non_negative_int_validate],
                                              verbose_name='Буфер оценки')
    parent = models.ForeignKey('self', verbose_name='Родительская задача', null=True,
                               blank=True, on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='Уровень вложенности',
                                validators=[is_int_validate, positive_int_validate],
                                default=1)

    def __str__(self):
        return self.short_name


class Comment(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задачам'

    author = models.ForeignKey(EmployeeUser, verbose_name='Комментатор', on_delete=models.SET_NULL,
                               null=True)
    text = models.CharField(max_length=255, verbose_name='Текст комментария')
    datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name='Задача')

    def __str__(self):
        string = f'{self.author} {self.datetime}'
        return string


class TrackTime(BaseModel):
    objects = TrackTimeManager()

    class Meta:
        verbose_name = 'Затреканное время'
        verbose_name_plural = 'Затреканное время'

    minutes = models.IntegerField(validators=[is_int_validate, positive_int_validate],
                                  verbose_name='Время в минутах')
    executor = models.ForeignKey(EmployeeUser, verbose_name='Сотрудник', on_delete=models.SET_NULL,
                                 null=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name='Задача')
    text = models.CharField(max_length=255, verbose_name='Описание работы', blank=True, null=True)
    datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)


class IssueHistoryRecord(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'История задачи'
        verbose_name_plural = 'Истории задач'

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, verbose_name='Задача')
    text = models.CharField(max_length=255, verbose_name='Описание')
    datetime = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
