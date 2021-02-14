class UniqueIdentifiedObjectCollection():

    def __init__(self, *args):
        self.__collection = dict()
        self.add(args)

    def __add__(self, *args):
        self.add(args)

    def __sub__(self, *args):
        self.remove(args)

    def add(self, *args):
        for identified_object in args:
            if not self.contains(identified_object):
                self.__collection[identified_object.identifier] = identified_object

    def remove(self, *args):
        for identified_object in args:
            if self.contains(identified_object):
                self.__collection.pop(identified_object.identifier, None)

    def contains(self, identified_object, /):
        return identified_object.identifier in self.__collection.keys()

    def search(self):
        # TODO: implement the search method()
        pass

    def merge(self):
        # TODO: implement the merge() method
        pass


class MultipleIdentifiedObjectCollection():

    def __init__(self, *args):
        self.__collection = dict()
        self.add(args)

    def __add__(self, *args):
        self.add(args)

    def __sub__(self, *args):
        self.remove(args)

    def add(self, *args):
        for identified_object in args:
            if self.contains(identified_object):
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
