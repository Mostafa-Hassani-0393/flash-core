# Using motor instead of pymongo because of asynchronousity
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load ENV vars
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpassword@localhost:27018")
DB_NAME = "flashcard_db"

#Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
database=client[DB_NAME]
flashcards_collection = database["flashcards"]