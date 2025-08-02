from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/puzzles", tags=["Puzzles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar puzzle
@router.post("/", response_model=schemas.Puzzle)
def create_puzzle(puzzle: schemas.PuzzleCreate, db: Session = Depends(get_db)):
    db_puzzle = models.Puzzle(**puzzle.dict())
    db.add(db_puzzle)
    db.commit()
    db.refresh(db_puzzle)
    return db_puzzle

# Listar todos os puzzles
@router.get("/", response_model=list[schemas.Puzzle])
def get_puzzles(db: Session = Depends(get_db)):
    return db.query(models.Puzzle).all()

# Filtrar puzzles por dificuldade
@router.get("/difficulty/{difficulty}", response_model=list[schemas.Puzzle])
def get_puzzles_by_difficulty(difficulty: str, db: Session = Depends(get_db)):
    puzzles = db.query(models.Puzzle).filter(
        models.Puzzle.difficulty.ilike(difficulty)
    ).all()
    if not puzzles:
        raise HTTPException(status_code=404, detail="Nenhum puzzle encontrado para essa dificuldade")
    return puzzles
