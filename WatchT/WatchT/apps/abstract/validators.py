from django.core.exceptions import ValidationError


def is_int_validate(value):
    if not isinstance(value, int):
        raise ValidationError("Значение должно быть целочисленным")


def bigger_than_zero_validate(value):
    if value <= 0:
        raise ValidationError("Значение должно быть больше 0")
