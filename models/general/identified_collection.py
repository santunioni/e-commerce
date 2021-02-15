class UniqueIdentifiedObjectCollection:

    def __init__(self, *args):
        self.__collection = dict()

    def __contains__(self, identified_object):
        return self.contains(identified_object)

    def __get__(self, identifier):
        return self.get(identifier)

    @property
    def collection(self):
        return self.__collection

    @collection.setter
    def collection(self, collection):
        self.__collection = collection

    def add(self, *args):
        for identified_object in args:
            if identified_object not in self:
                self.__collection[identified_object.identifier] = identified_object

    def remove(self, *args):
        for identified_object in args:
            if self.contains(identified_object):
                self.__collection.pop(identified_object.identifier, None)

    def contains(self, identified_object, /):
        return identified_object.identifier in self.__collection.keys()

    def get(self, identifier):
        if identifier in self.__collection.keys():
            return self.__collection['identifier']

    def search(self):
        # TODO: implement the search method()
        pass

    def merge(self):
        # TODO: implement the merge() method
        pass


class MultipleIdentifiedObjectCollection:

    def __init__(self, *args):
        self.__collection = dict()
        self.add(*args)

    def __add__(self, *args):
        self.add(*args)

    def __sub__(self, *args):
        self.remove(*args)
        
    def __contains__(self, identified_object):
        return self.contains(identified_object)

    def __iter__(self):
        return self.__collection

    def __len__(self):
        return len(self.__collection.keys())

    def add(self, *args):
        for identified_object in args:
            if identified_object in self:
                self.__collection[identified_object.identifier]['amount'] += 1
            else:
                self.__collection[identified_object.identifier] = {'amount': 1, 'object': identified_object}

    def remove(self, *args):
        for identified_object in args:
            if self.contains(identified_object):
                if self.__collection[identified_object.identifier]['amount'] > 1:
                    self.__collection[identified_object.identifier]['amount'] -= 1
                if self.__collection[identified_object.identifier]['amount'] == 0:
                    self.__collection.pop(identified_object.identifier, None)

    def contains(self, identified_object, /):
        return identified_object.identifier in self.__collection.keys()

