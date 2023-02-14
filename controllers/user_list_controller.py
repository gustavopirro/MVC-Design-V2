from models.repositories.users_repository import user_repository
from typing import List, Dict

class UserListController:
    
    def get_users(self, user_city_state=None) -> list: 
        user_list = user_repository.get_all()

        if user_city_state:
            user_list = user_repository.filter_by_state(user_city_state)
        try:
            response = self.__format_response(user_list)
            return response
        except:
            return { "success": False, "error": "An error ocurred" }
    
    
    def __format_response(self, users: List) -> Dict:
        formatted_users = []

        for user in users:
            formatted_users.append({
                "username": user.name,
                "telephone": user.telephone,
                "user_city_state": user.address_state
            })

        return {
            "success": True,
            "data": {
                "count": len(formatted_users),
                "users": formatted_users
            }
        }
