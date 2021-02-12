from ..user.models import EmployeeUser
from .exceptions import ReAuthRequiredException


# class UserSingle:
#
#     def __init__(self):
#         self.__user = None
#
#     @property
#     def user(self):
#         if self.__user is None:
#             raise ReAuthRequiredException
#         return self.__user
#
#     @user.setter
#     def user(self, new_user: EmployeeUser):
#         self.__user = new_user
#
#     def logout(self):
#         self.__user = None
#
#
# request_user = UserSingle()


def sanitize_query_params(dictionary: dict):
    return {k: v[0] for k, v in dictionary.items() if v[0]}
