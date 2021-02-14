from models.general.person import Person


class IdentifiedPerson(Person):

    def __init__(self, *, username: str = '', full_name: str, email: str):
        super().__init__(username=username, full_name=full_name, email=email)
        self.__identifier = self.__email

    @property
    def identifier(self):
        return self.__identifier
