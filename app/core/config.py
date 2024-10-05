from pydantic_settings import BaseSettings, SettingsConfigDict
import os

DOTENV = os.path.join(os.path.dirname(__file__), "..", ".env")

class Settings(BaseSettings):
    DATABASE_URL:str 
    SECRET_KEY:str 
    ALGORITHM:str 
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding='utf-8')

settings = Settings()


