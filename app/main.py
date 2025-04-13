# main.py

from fastapi import FastAPI
from app.routes import flashcard

app = FastAPI(
    title="Flashcard API",
    version="1.0.0"
)

app.include_router(flashcard.router)
