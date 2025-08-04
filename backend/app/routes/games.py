from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/games", tags=["Games"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.Game])
def get_games(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("started_at"),
    order: str = Query("desc")
):
    valid_sort_fields = {"id": models.Game.id, "started_at": models.Game.started_at, "finished_at": models.Game.finished_at}
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Escolha entre: {list(valid_sort_fields.keys())}")

    sort_column = valid_sort_fields[sort_by]
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Game).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

@router.get("/player/{player_id}", response_model=list[schemas.Game])
def get_games_by_player(
    player_id: int,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("started_at"),
    order: str = Query("desc")
):
    valid_sort_fields = {"id": models.Game.id, "started_at": models.Game.started_at, "finished_at": models.Game.finished_at}
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Escolha entre: {list(valid_sort_fields.keys())}")

    sort_column = valid_sort_fields[sort_by]
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Game).filter(
        (models.Game.white_player_id == player_id) |
        (models.Game.black_player_id == player_id)
    ).order_by(sort_func(sort_column))

    return query.offset((page - 1) * limit).limit(limit).all()

# Buscar partidas por modo de jogo (blitz, bullet, rapid)
@router.get("/mode/{mode}", response_model=list[schemas.Game])
def get_games_by_mode(
    mode: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("started_at"),
    order: str = Query("desc")
):
    valid_modes = ["blitz", "bullet", "rapid"]
    if mode.lower() not in valid_modes:
        raise HTTPException(status_code=400, detail=f"Modo inválido. Escolha entre: {valid_modes}")

    valid_sort_fields = {"id": models.Game.id, "started_at": models.Game.started_at, "finished_at": models.Game.finished_at}
    sort_column = valid_sort_fields.get(sort_by, models.Game.started_at)
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Game).filter(models.Game.mode.ilike(mode)).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()
