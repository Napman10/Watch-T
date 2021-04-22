from rest_framework.exceptions import APIException


class VeryYoungException(APIException):
    status_code = 400
    default_detail = "Недостаточно опыта для выполнения задачи с таким приоритетом!"


class OnlyDevUpLevel(APIException):
    status_code = 400
    default_detail = "Поднять уровень можно только разработчику!"


class IsSeniorNowException(APIException):
    status_code = 400
    default_detail = "Уже сеньор"


class NotAllChildDoneException(APIException):
    status_code = 400
    default_detail = 'Не все подзадачи завершены'


class NonDevGiveSkillException(APIException):
    status_code = 400
    default_detail = 'Нельзя дать навык не разработчику'


class DoesNotHaveQualificationException(APIException):
    status_code = 400
    default_detail = 'Задача не подходит по квалификации'


class BufferWantTimeException(APIException):
    status_code = 400
    default_detail = 'Сумма оценок выполнения подзадач выше родительской задачи!'


class NegativeGotTimeException(APIException):
    status_code = 400
    default_detail = 'Отрицательные трудозатраты'


class OverThreeInProgressException(APIException):
    status_code = 400
    default_detail = 'Нельзя назначить больше трех задач в статус проверка/в работе на одного сотрудника'


class NotConfirmedPass(APIException):
    status_code = 400
    default_detail = 'Пароли не совпадают!'


class OverTimeException(APIException):
    status_code = 400
    default_detail = 'Переработка!'
