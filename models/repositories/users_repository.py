class __UserRepository:

    def __init__(self) -> None:
        self.__user_repository = []
    
    def insert(self, new_user):
        self.__user_repository.append(new_user)

        return new_user

    def get_all(self):
        return self.__user_repository

    def filter_by_state(self, address_state) -> list: 
        filtered_users = []
        for user in self.__user_repository:
            if user.address_state == address_state:
                filtered_users.append(user)

        return filtered_users

user_repository = __UserRepository()