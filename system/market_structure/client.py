# PYTHON LIBRARIES IMPORTS
from passlib.hash import pbkdf2_sha256 as cryp

# LOCAL APP IMPORTS
# classes from the GENERAL PURPOSE package
from system.general_purpose.identified_objects_collections import MultipleIdentifiedObjectCollection
from system.general_purpose.person_identified import IdentifiedPerson


class Kart(MultipleIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)


class Client(IdentifiedPerson):

    def __init__(self, *, full_name: str, email: str, password: str):
        super().__init__(full_name=full_name, email=email)
        self.__password: str = cryp.hash(password, rounds=200000, salt_size=16)
        self.__kart: Kart = Kart()

    @property
    def kart(self) -> Kart:
        return self.__kart

    def check_pass(self, password: str) -> bool:
        return cryp.verify(password, self.__password)

    def close_order(self):
        # TODO: implement the close_order() method
        pass
