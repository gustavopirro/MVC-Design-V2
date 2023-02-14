from models.repositories import users_repository

class User:

    def __init__(self, name: str, telephone: str, address_state: str) -> None:
        self.name = name
        self.telephone = telephone
        self.address_state = address_state