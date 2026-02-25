import json
from app.models.user_model import UserModel

class UsersFactory:
    
    def create_users(self, json_path: str) -> list[UserModel]:
       
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        if "users" not in data:
            raise ValueError("no users found")
            
        
        raw_users = data["users"]
        
        
        users_list = []
        for user_data in raw_users:
            user_obj = UserModel(**user_data) 
            users_list.append(user_obj)
            
        return users_list