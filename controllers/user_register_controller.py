from models.repositories.users_repository import user_repository
from models.entities.User import User 
from typing import Dict

class UserRegisterController:

    def register(self, new_user_data):
        try:
            new_user = self.__create_user_entity(new_user_data)
            self.__save(new_user)
            return self.__format_response(new_user_data)
        except:
            return { "success": False, "error": "An error ocurred" }

    def __create_user_entity(self, new_user_data: Dict):
        username = new_user_data["username"]
        telephone = new_user_data["telephone"]
        user_city_state = new_user_data["user_city_state"]

        user = User(username, telephone, user_city_state)
        return user
    
    def __save(self, new_user_data: Dict):
        user_repository.insert(new_user_data)
    
    def __format_response(self, new_user_data: Dict) -> Dict:
        return {
            "success": True,
            "data": {
                "username": new_user_data["username"],
                "telephone": new_user_data["telephone"],
                "user_city_state": new_user_data["user_city_state"]
            }
        }