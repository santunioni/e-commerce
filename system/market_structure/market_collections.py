# LOCAL APP IMPORTS
# classes from the GENERAL PURPOSE package
from system.general_purpose.identified_objects_collections import UniqueIdentifiedObjectCollection
from system.general_purpose.identified_objects_collections import MultipleIdentifiedObjectCollection
# importing for MYPY type hinting
from typing import Generator, Any


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
    def emails(self) -> Generator[str, None, None]:
        return (client_email for client_email in super().collection.keys())


class EmployeeCollection(UniqueIdentifiedObjectCollection):

    def __init__(self):
        super().__init__()

    @property
    def emails(self) -> Generator[str, None, None]:
        return (employee_email for employee_email in super().collection.keys())
