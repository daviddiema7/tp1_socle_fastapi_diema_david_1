import os 
from dotenv import load_dotenv

class Settings:
    def __init__(self) -> None:
        load_dotenv()
        self.users_json_path = os.getenv("USERS_JSON_PATH", "data/users.json")