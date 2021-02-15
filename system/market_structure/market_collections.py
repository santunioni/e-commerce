# LOCAL APP IMPORTS
# classes from the GENERAL PURPOSE package
from system.general_purpose.objects_identified_collection import UniqueIdentifiedObjectCollection
from system.general_purpose.objects_identified_collection import MultipleIdentifiedObjectCollection


class InventoryModel(MultipleIdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)


class ProductsForSell(UniqueIdentifiedObjectCollection):

    def __init__(self):
        super().__init__()


class ClientCollection(UniqueIdentifiedObjectCollection):

    def __init__(self):
        super().__init__()

    @property
    def emails(self):
        return (client_email for client_email in super().collection.keys())


class EmployeeCollection(UniqueIdentifiedObjectCollection):

    def __init__(self):
        super().__init__()

    @property
    def emails(self):
        return (employee_email for employee_email in super().collection.keys())
