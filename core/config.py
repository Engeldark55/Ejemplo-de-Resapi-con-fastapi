import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROYECT_NAME:str = "APIRest kuitol"
    PROYECT_VERSION:str = "1.0"
    URL_SQLITE = os.getenv('URL_SQLITE_DB')
    
setting = Settings()
