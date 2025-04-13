from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
from uuid import UUID, uuid4


class FlashCardBase(BaseModel):
    deckId: UUID
    owner: UUID
    word: str
    clue: Optional[str] = None
    definition: Optional[str] = None
    contextSentence: Optional[str] = None
    pluralForm: Optional[str] = None
    mnemonic: Optional[str] = None
    certLevel: Optional[str] = None
    tags: Optional[Dict[str, Optional[str]]] = None
    ipa: Optional[str] = None


class FlashCardCreate(FlashCardBase):
    pass


class FlashCardDB(FlashCardBase):
    id: UUID = Field(default_factory=uuid4)
    createTime: datetime = Field(default_factory=datetime.utcnow)
    modifyTime: datetime = Field(default_factory=datetime.utcnow)
    archiveTime: Optional[datetime] = None
    archiveUserID: Optional[UUID] = None
    deleteTime: Optional[datetime] = None
    deleteUserID: Optional[UUID] = None

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),  # For Swagger/JSON serialization
        }
