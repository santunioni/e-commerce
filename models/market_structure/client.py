from models.general.identified_collection import MultipleIdentifiedObjectCollection
from models.general.identified_person import IdentifiedPerson


class Client(IdentifiedPerson):

    def __init__(self, *, full_name: str, email: str):
        super().__init__(full_name=full_name, email=email)
        self.__kart = Kart()

    @property
    def kart(self):
        return self.__kart


class Kart(MultipleIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)
