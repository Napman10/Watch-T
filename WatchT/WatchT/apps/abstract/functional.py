from ..user.models import EmployeeUser


class UserSingle:

    def __init__(self):
        self.__user = None

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user: EmployeeUser):
        self.__user = new_user

    def logout(self):
        self.__user = None


request_user = UserSingle()
