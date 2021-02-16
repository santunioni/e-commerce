# imported for MyPy type hinting only
from typing import Set


class Product:

    def __init__(self, name: str, price: float, description: str = ""):
        self.__name: str = name
        self.__price: float = float(price)
        self.__description: str = description
        self.__tags: Set = set()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if type(name) == str:
            self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        if type(description) == str:
            self.__description = description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if type(price) == float:
            self.__price = price

    @property
    def tags(self) -> Set:
        return self.__tags

    # TODO: implement the add_tags and remove_tags methods


class IdentifiedProduct(Product):

    # TODO: refactor the way in which products are identified

    __id_number: int = 0

    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        self.__identifier: int = self.__id_number
        IdentifiedProduct.__id_number += 1

    @property
    def identifier(self) -> int:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: int):
        self.__identifier = identifier
