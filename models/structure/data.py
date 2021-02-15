from models.general.identified_collection import UniqueIdentifiedObjectCollection
from models.general.identified_collection import MultipleIdentifiedObjectCollection


class Inventory(MultipleIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)


class ProductsForSell(UniqueIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)


class ClientCollection(UniqueIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def emails(self):
        lista = []
        for client in super().collection:
            print(f"{client = }")
            lista.append(client.email)



class EmployeeCollection(UniqueIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)

    def list_emails(self):
        return self.email
