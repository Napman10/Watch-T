from rest_framework.exceptions import APIException


class BufferWantTimeException(APIException):
    status_code = 400
    default_detail = 'Child want_time is bigger than parent buffer_want_time'


class NegativeGotTimeException(APIException):
    status_code = 400
    default_detail = 'got_time < 0'


class NotConfirmedPass(APIException):
    status_code = 400
    default_detail = 'password != confirm'


class OverTimeException(APIException):
    status_code = 400
    default_detail = 'overtime for today'
