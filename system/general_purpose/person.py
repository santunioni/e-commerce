class Person:

    def __init__(self, *, username: str = '', full_name: str, email: str):
        self.__username: str = username.lower()
        self.__full_name: str = full_name.title()
        self.__email: str = email

    @property
    def username(self):
        return self.__username

    @property
    def full_name(self):
        return self.__full_name

    @property
    def email(self):
        return self.__email
