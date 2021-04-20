from rest_framework.exceptions import APIException


class NotAllChildDoneException(APIException):
    status_code = 400
    default_detail = 'Не все подзадачи завершены'


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
