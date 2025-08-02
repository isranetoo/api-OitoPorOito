from fastapi import APIRouter, Depends
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

@router.post("/", response_model=schemas.Puzzle)
def create_puzzle(puzzle: schemas.PuzzleCreate, db: Session = Depends(get_db)):
    db_puzzle = models.Puzzle(**puzzle.dict())
    db.add(db_puzzle)
    db.commit()
    db.refresh(db_puzzle)
    return db_puzzle

@router.get("/", response_model=list[schemas.Puzzle])
def get_puzzles(db: Session = Depends(get_db)):
    return db.query(models.Puzzle).all()
