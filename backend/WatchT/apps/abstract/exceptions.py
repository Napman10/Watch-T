from rest_framework.exceptions import APIException


class BufferWantTimeException(APIException):
    status_code = 400
    default_detail = 'Child want_time is bigger than parent buffer_want_time'
