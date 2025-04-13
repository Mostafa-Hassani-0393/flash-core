# app/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27018"
    mongodb_db: str = "flashcard_db"

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
