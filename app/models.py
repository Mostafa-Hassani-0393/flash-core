from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime
from uuid import uuid4


class FlashCard(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    deckId: str
    owner: str
    word: str
    clue: Optional[str] = None
    definition: Optional[str] = None
    contextSentence: Optional[str] = None
    pluralForm: Optional[str] = None
    mnemonic: Optional[str] = None
    cefrLevel: Optional[str] = None
    tags: Optional[Dict[str, Optional[str]]] = None
    ipa: Optional[str] = None
    archiveTime: Optional[datetime] = None
    archiveUserId: Optional[str] = None
    deleteTime: Optional[datetime] = None
    deleteUserId: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
