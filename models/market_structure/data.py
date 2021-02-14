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
