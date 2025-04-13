# app/crud/flashcard.py

from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from datetime import datetime
from app.models.flashcard import FlashCardBase, FlashCardCreate, FlashCardUpdate

collection_name = "flashcards"

async def get_flashcards(db: AsyncIOMotorDatabase):
    return await db[collection_name].find().to_list(100)

async def get_flashcard(db: AsyncIOMotorDatabase, flashcard_id: str):
    return await db[collection_name].find_one({"_id": ObjectId(flashcard_id)})

async def create_flashcard(db: AsyncIOMotorDatabase, data: FlashCardCreate):
    now = datetime.utcnow()
    flashcard_dict = data.dict()
    flashcard_dict["createTime"] = now
    flashcard_dict["modifyTime"] = now
    result = await db[collection_name].insert_one(flashcard_dict)
    return await get_flashcard(db, str(result.inserted_id))

async def update_flashcard(db: AsyncIOMotorDatabase, flashcard_id: str, data: FlashCardUpdate):
    update_data = {**data.dict(exclude_unset=True), "modifyTime": datetime.utcnow()}
    await db[collection_name].update_one({"_id": ObjectId(flashcard_id)}, {"$set": update_data})
    return await get_flashcard(db, flashcard_id)

async def delete_flashcard(db: AsyncIOMotorDatabase, flashcard_id: str):
    return await db[collection_name].delete_one({"_id": ObjectId(flashcard_id)})
