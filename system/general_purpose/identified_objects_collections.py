# imported only for MYPY type hinting
from system.general_purpose.identified_object import IdentifiedObject
from typing import Union


class UniqueIdentifiedObjectCollection:

    def __init__(self) -> None:
        self.__collection: dict = dict()

    def __contains__(self, identified_object: IdentifiedObject) -> bool:
        return self.contains(identified_object)

    def __getitem__(self, identifier: str) -> Union[IdentifiedObject, None]:
        if identifier in self.__collection.keys():
            return self.__collection[identifier]
        return None

    @property
    def collection(self) -> dict:
        return self.__collection

    @collection.setter
    def collection(self, collection):
        self.__collection = collection

    def add(self, *args: IdentifiedObject) -> None:
        for identified_object in args:
            if identified_object not in self:
                self.__collection[identified_object.identifier] = identified_object

    def remove(self, *args: IdentifiedObject) -> None:
        for identified_object in args:
            if self.contains(identified_object):
                self.__collection.pop(identified_object.identifier, None)

    def contains(self, identified_object: IdentifiedObject, /) -> bool:
        return identified_object.identifier in self.__collection.keys()

    def search(self):
        # TODO: implement the search() method
        pass

    def merge(self):
        # TODO: implement the merge() method
        pass


class MultipleIdentifiedObjectCollection:

    def __init__(self, *args: IdentifiedObject):
        self.__collection: dict = dict()
        self.add(*args)

    def __add__(self, *args: IdentifiedObject):
        self.add(*args)

    def __sub__(self, *args: IdentifiedObject):
        self.remove(*args)

    def __contains__(self, identified_object: IdentifiedObject) -> bool:
        return self.contains(identified_object)

    def __iter__(self):
        return iter(self.__collection.keys())

    def __len__(self) -> int:
        return len(self.__collection.keys())

    def add(self, *args: IdentifiedObject) -> None:
        for identified_object in args:
            if identified_object in self:
                self.__collection[identified_object.identifier]['amount'] += 1
            else:
                self.__collection[identified_object.identifier] = {'amount': 1, 'object': identified_object}

    def remove(self, *args: IdentifiedObject) -> None:
        for identified_object in args:
            if self.contains(identified_object):
                if self.__collection[identified_object.identifier]['amount'] > 1:
                    self.__collection[identified_object.identifier]['amount'] -= 1
                if self.__collection[identified_object.identifier]['amount'] == 0:
                    self.__collection.pop(identified_object.identifier, None)

    def contains(self, identified_object: IdentifiedObject, /) -> bool:
        return identified_object.identifier in self.__collection.keys()

    @property
    def collection(self):
        return self.__collection

    def amount_of(self, identified_object: IdentifiedObject) -> int:
        if identified_object in self:
            return self.__collection[identified_object.identifier]['amount']
        return 0

    def dict_form(self) -> dict:
        dictionary_var = dict()
        for obj_id in self.__collection:
            obj = self.__collection[obj_id]['object']
            public_attributes = (pb_att for pb_att in dir(self.__collection) if not pb_att.startswith('_'))
            dictionary_var[obj_id] = {pub_att: obj[pub_att] for pub_att in public_attributes}
        return dictionary_var
