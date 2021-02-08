from rest_framework.exceptions import APIException


class ReAuthRequiredException(APIException):
    status_code = 500
    default_detail = 'Требуется перезапустить учетную запись.'
