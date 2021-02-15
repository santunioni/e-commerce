from system.general_purpose.person_identified import IdentifiedPerson


class Worker(IdentifiedPerson):

    def __init__(self, *, full_name: str, email: str):
        super().__init__(full_name=full_name, email=email)
