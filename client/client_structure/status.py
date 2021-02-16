# LOCAL APP IMPORTS
from system.sys_functions.authenticator import ClientCredentials
# imported only for MYPY type hinting
from typing import Union, Literal
from system.market_structure.client import Client


class ClientStatus:

    __client_object: Union[Client, None] = None

    @classmethod
    def active_client(cls) -> Union[Client, None]:
        return cls.__client_object

    @classmethod
    def logout(cls) -> None:
        cls.__client_object = None

    @classmethod
    def login(cls, email: str, password: str) -> None:
        cls.__client_object = ClientCredentials.login(email, password)

    @classmethod
    def sign_in(cls, full_name: str, email: str, password: str) -> None:
        cls.__client_object = ClientCredentials.sign_in(full_name, email, password)
