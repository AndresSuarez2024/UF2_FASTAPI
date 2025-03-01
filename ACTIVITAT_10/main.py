from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import random
from database import get_db
from models import Word
from schemas import ThemeResponse, WordResponse

app = FastAPI()

# Endpoint 1: Obtener lista de temáticas
@app.get("/penjat/tematica/opcions", response_model=list[ThemeResponse])
async def get_tematica_opcions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Word.theme).distinct())
    themes = result.scalars().all()
    return [{"option": theme} for theme in themes]

# Endpoint 2: Obtener una palabra aleatoria de una temática
@app.get("/penjat/tematica/{option}", response_model=list[WordResponse])
async def get_paraula(option: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Word.word).where(Word.theme == option))
    words = result.scalars().all()

    if not words:
        raise HTTPException(status_code=404, detail="Temática no encontrada")

    return [{"option": random.choice(words)}]
