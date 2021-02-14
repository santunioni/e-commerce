class Product:

    def __init__(self, name: str, price: float, tags: set[str] = set(), description: str = ""):
        self.__name = name
        self.__price = price
        self.__tags = tags
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        pass



    @property
    def price(self):
        return self.__price

class ProductCollection():

    def __init__(self):
        pass

    def add(self, *args):
        pass

