from ..abstract.models import BaseModel
from django.db.models import Manager


class Task(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
