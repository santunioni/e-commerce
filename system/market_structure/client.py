from system.general_purpose.person_identified_collection import MultipleIdentifiedObjectCollection
from system.general_purpose.person_identified import IdentifiedPerson
from passlib.hash import pbkdf2_sha256 as cryp


class Client(IdentifiedPerson):

    def __init__(self, *, full_name: str, email: str, password: str):
        super().__init__(full_name=full_name, email=email)
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)
        self.__kart = Kart()

    @property
    def kart(self):
        return self.__kart

    def check_pass(self, password):
        return cryp.verify(password, self.__password)


class Kart(MultipleIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)
