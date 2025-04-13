# app/routes/flashcard.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.flashcard import FlashcardInDB, FlashcardCreate, FlashcardUpdate
from app.db.mongo import get_mongo
from app.crud import flashcard as crud
from bson.errors import InvalidId

router = APIRouter(prefix="/flashcards", tags=["Flashcards"])

def get_db():
    return get_mongo().get_db()

@router.get("/", response_model=List[FlashcardInDB])
async def list_flashcards(db=Depends(get_db)):
    return await crud.get_flashcards(db)

@router.get("/{flashcard_id}", response_model=FlashcardInDB)
async def get_flashcard(flashcard_id: str, db=Depends(get_db)):
    try:
        card = await crud.get_flashcard(db, flashcard_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    if not card:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return card

@router.post("/", response_model=FlashcardInDB, status_code=status.HTTP_201_CREATED)
async def create_flashcard(flashcard: FlashcardCreate, db=Depends(get_db)):
    return await crud.create_flashcard(db, flashcard)

@router.put("/{flashcard_id}", response_model=FlashcardInDB)
async def update_flashcard(flashcard_id: str, flashcard: FlashcardUpdate, db=Depends(get_db)):
    card = await crud.update_flashcard(db, flashcard_id, flashcard)
    if not card:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return card

@router.delete("/{flashcard_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_flashcard(flashcard_id: str, db=Depends(get_db)):
    result = await crud.delete_flashcard(db, flashcard_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Flashcard not found")
