class IdentifiedObject:

    def __init__(self, *, identifier: str):
        self.__identifier: str = identifier

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str) -> None:
        self.__identifier = identifier
