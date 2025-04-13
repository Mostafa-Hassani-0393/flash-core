# app/db/mongo.py

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from fastapi import Request
from functools import lru_cache
import os

from app.config import get_settings

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]

    def get_db(self):
        return self.db

@lru_cache
def get_mongo():
    settings = get_settings()
    return MongoDB(uri=settings.mongodb_uri, db_name=settings.mongodb_db)
