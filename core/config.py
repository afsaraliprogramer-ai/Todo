from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORITHM : str
    MINUTES : int
    DAYS : int
    API : str



    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")

settings = Settings()