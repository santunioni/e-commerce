# project imports
from system.general_purpose.objects_identified_collection import UniqueIdentifiedObjectCollection
from system.general_purpose.objects_identified_collection import MultipleIdentifiedObjectCollection


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
        return (client_email for client_email in super().collection.keys())


class EmployeeCollection(UniqueIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)

    def list_emails(self):
        return self.email
