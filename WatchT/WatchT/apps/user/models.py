from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models, transaction

from ..abstract.models import BaseModel


def user_photo_upload_to(instance, filename):
    return f'user/{instance.id}/{filename}'


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password=password, **extra_fields)


class EmployeeUser(AbstractBaseUser, PermissionsMixin, BaseModel):
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

    email = models.EmailField(max_length=40, unique=True, verbose_name='Почта')
    username = models.CharField(max_length=40, unique=True, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя', default='Name')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия', default='Surname')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=user_photo_upload_to, default='default_user_pic.jpg', verbose_name='Фото')
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='Роль', default=GUEST)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        super(EmployeeUser, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.username
