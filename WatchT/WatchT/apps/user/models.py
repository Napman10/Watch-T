from ..abstract.models import BaseModel
from django.db.models import Manager


class Task(BaseModel):
    objects = Manager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
