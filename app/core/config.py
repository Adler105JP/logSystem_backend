from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str =  "mysql://adler:$Marfil1$@68.183.227.119/log_system"
    SECRET_KEY:str = "$Marfil$105"
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 1440

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()


