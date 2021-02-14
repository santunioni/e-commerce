class Product:

    def __init__(self, name: str, price: float, description: str = ""):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__tags = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) == str:
            self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) == str:
            self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) == float:
            self.__price = price

    @property
    def tags(self):
        return self.__tags

    # TODO: implement the add_tags and remove_tags methods


class IdentifiedProduct(Product):

    # TODO: refactor the way in which products are identified

    __id_number = 0

    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        self.__identifier = self.__id_number
        IdentifiedProduct.__id_number += 1

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier):
        self.__identifier = identifier


