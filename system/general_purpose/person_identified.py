# LOCAL APP IMPORTS
# classes from the GENERAL PURPOSE package
from system.general_purpose.person import Person
from system.general_purpose.identified_object import IdentifiedObject
import copy


class IdentifiedPerson(Person, IdentifiedObject):

    def __init__(self, *, full_name: str, email: str, username: str = ''):
        super().__init__(full_name=full_name, email=email, username=username)

    @property
    def identifier(self) -> str:
        return self.email

    @identifier.setter
    def identifier(self, identifier: str) -> None:
        self.email = identifier
