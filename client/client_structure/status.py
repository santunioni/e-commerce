# project imports
from system.sys_functions.request import ClientCredentials


class ClientStatus:

    __client_object = None

    @classmethod
    def active_client(cls):
        return cls.__client_object

    @classmethod
    def logout(cls):
        cls.__client_object = None

    @classmethod
    def login(cls, email: str, password: str):
        cls.__client_object = ClientCredentials.login(email, password)

    @classmethod
    def sign_in(cls, full_name, email, password):
        cls.__client_object = ClientCredentials.sign_in(full_name, email, password)
