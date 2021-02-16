from system.general_purpose.identified_object import IdentifiedObject


class Person():

    def __init__(self, *, full_name: str, email: str, username: str = ''):
        self.__username: str = username.lower()
        self.__full_name: str = full_name.title()
        self.__email: str = email

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email
