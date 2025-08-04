from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/puzzles", tags=["Puzzles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.Puzzle])
def get_puzzles(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("id"),
    order: str = Query("asc")
):
    valid_sort_fields = {"id": models.Puzzle.id, "difficulty": models.Puzzle.difficulty, "theme": models.Puzzle.theme}
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Escolha entre: {list(valid_sort_fields.keys())}")

    sort_column = valid_sort_fields[sort_by]
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Puzzle).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

@router.get("/difficulty/{difficulty}", response_model=list[schemas.Puzzle])
def get_puzzles_by_difficulty(
    difficulty: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("id"),
    order: str = Query("asc")
):
    valid_sort_fields = {"id": models.Puzzle.id, "difficulty": models.Puzzle.difficulty, "theme": models.Puzzle.theme}
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Escolha entre: {list(valid_sort_fields.keys())}")

    sort_column = valid_sort_fields[sort_by]
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Puzzle).filter(
        models.Puzzle.difficulty.ilike(difficulty)
    ).order_by(sort_func(sort_column))

    return query.offset((page - 1) * limit).limit(limit).all()

# Buscar puzzles por tema
@router.get("/theme/{theme}", response_model=list[schemas.Puzzle])
def get_puzzles_by_theme(
    theme: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("id"),
    order: str = Query("asc")
):
    valid_sort_fields = {"id": models.Puzzle.id, "difficulty": models.Puzzle.difficulty, "theme": models.Puzzle.theme}
    sort_column = valid_sort_fields.get(sort_by, models.Puzzle.id)
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Puzzle).filter(models.Puzzle.theme.ilike(theme)).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

