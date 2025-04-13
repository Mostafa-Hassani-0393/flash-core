from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


# Pydantic-compatible ObjectId for MongoDB
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Base shared flashcard model
class FlashcardBase(BaseModel):
    word: str
    clue: Optional[str] = None
    contextSentence: Optional[str] = None
    gerDict: str
    perDict: str
    engDict: str
    pluralForm: Optional[str] = None
    conjugation: Optional[str] = None
    partOfSpeech: Optional[str] = None  # noun, verb, etc.
    fullSentence: Optional[str] = None
    mnemonic: Optional[str] = None
    gender: Optional[str] = None  # "m", "f", "n"
    level: str  # A1, A2, B1, ...
    createTime: datetime = Field(default_factory=datetime.utcnow)
    modifyTime: datetime = Field(default_factory=datetime.utcnow)
    lastReviewedTime: Optional[datetime] = None
    learnedTime: Optional[datetime] = None
    archiveTime: Optional[datetime] = None
    deleteTime: Optional[datetime] = None
    reviewCount: int = 0
    correctCount: int = 0
    incorrectCount: int = 0
    tags: Optional[str] = None
    ipa: Optional[str] = None
    isArchived: bool = False


# Model used when creating a new flashcard (no ID yet)
class FlashcardCreate(FlashcardBase):
    pass


# Model used when updating an existing flashcard
class FlashcardUpdate(BaseModel):
    word: Optional[str] = None
    clue: Optional[str] = None
    contextSentence: Optional[str] = None
    gerDict: Optional[str] = None
    perDict: Optional[str] = None
    engDict: Optional[str] = None
    pluralForm: Optional[str] = None
    conjugation: Optional[str] = None
    partOfSpeech: Optional[str] = None
    fullSentence: Optional[str] = None
    mnemonic: Optional[str] = None
    gender: Optional[str] = None
    level: Optional[str] = None
    modifyTime: datetime = Field(default_factory=datetime.utcnow)
    lastReviewedTime: Optional[datetime] = None
    learnedTime: Optional[datetime] = None
    archiveTime: Optional[datetime] = None
    deleteTime: Optional[datetime] = None
    reviewCount: Optional[int] = None
    correctCount: Optional[int] = None
    incorrectCount: Optional[int] = None
    tags: Optional[str] = None
    ipa: Optional[str] = None
    isArchived: Optional[bool] = None


# Model used for returning data from DB (with ID)
class FlashcardResponse(FlashcardBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        orm_mode = True
