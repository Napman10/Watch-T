from django.core.exceptions import ValidationError


def is_int_validate(value):
    if not isinstance(value, int):
        raise ValidationError("Значение должно быть целочисленным")


def non_negative_int_validate(value):
    if value < 0:
        raise ValidationError("Значение не должно быть отрицательным")


def positive_int_validate(value):
    if value <= 0:
        raise ValidationError("Значение должно быть положительным")
