# LOCAL APP IMPORTS
# classes from the GENERAL PURPOSE package
from system.general_purpose.person import Person


class IdentifiedPerson(Person):

    def __init__(self, *, username: str = '', full_name: str, email: str):
        super().__init__(username=username, full_name=full_name, email=email)

    @property
    def identifier(self):
        return super().email

