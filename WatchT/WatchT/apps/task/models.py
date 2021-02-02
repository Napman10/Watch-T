from ..abstract.models import BaseModel
from ..user.models import CustomUser, Team
from django.db.models import Manager
from django.db import models
from ..abstract.validators import is_int_validate, bigger_than_zero_validate


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

    objects = Manager()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    short_name = models.CharField(max_length=16, verbose_name='Короткое название', unique=True)
    header = models.CharField(max_length=65, verbose_name='Заголовок', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(CustomUser, verbose_name='Составил', on_delete=models.SET_NULL,
                               null=True, related_name='author_task')
    executor = models.ForeignKey(CustomUser, verbose_name='Выполняет', on_delete=models.SET_NULL,
                                 null=True, related_name='executor_task')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=NORMAL, verbose_name='Приоритет')
    status = models.IntegerField(choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')
    want_minutes = models.IntegerField(validators=[is_int_validate, bigger_than_zero_validate], verbose_name='Оценка')
    got_minutes = models.IntegerField(validators=[is_int_validate, bigger_than_zero_validate], verbose_name='Затрачено')
    parent = models.ForeignKey('self', verbose_name='Родительская задача', null=True,
                               blank=True, on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='Уровень вложенности',
                                validators=[is_int_validate, bigger_than_zero_validate],
                                default=1)

    def __str__(self):
        return self.short_name


class Comment(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задачам'

    author = models.ForeignKey(CustomUser, verbose_name='Комментатор', on_delete=models.SET_NULL,
                               null=True)
    text = models.CharField(max_length=255, verbose_name='Текст комментария')
    datetime = models.DateTimeField()
    edited = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        string = f'{self.author} {self.datetime}'
        if self.edited:
            string += ' (ред.)'
        return string
