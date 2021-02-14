
from models.collection import IdentifiedObjectCollection


class ProductCollection(IdentifiedObjectCollection):

    def __init__(self, *args):
        super().__init__(*args)

    def add(self, *args):
        pass
