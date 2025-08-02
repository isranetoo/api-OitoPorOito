from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from datetime import datetime
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Tournament])
def get_tournaments(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("start_date"),
    order: str = Query("desc")
):
    valid_sort_fields = {"id": models.Tournament.id, "start_date": models.Tournament.start_date, "end_date": models.Tournament.end_date}
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Escolha entre: {list(valid_sort_fields.keys())}")

    sort_column = valid_sort_fields[sort_by]
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Tournament).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

@router.get("/active", response_model=list[schemas.Tournament])
def get_active_tournaments(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    now = datetime.utcnow()
    query = db.query(models.Tournament).filter(
        models.Tournament.start_date <= now,
        models.Tournament.end_date >= now
    )
    return query.offset((page - 1) * limit).limit(limit).all()

# Buscar torneios por tipo (arena, round_robin)
@router.get("/type/{tournament_type}", response_model=list[schemas.Tournament])
def get_tournaments_by_type(
    tournament_type: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("start_date"),
    order: str = Query("desc")
):
    valid_types = ["arena", "round_robin"]
    if tournament_type.lower() not in valid_types:
        raise HTTPException(status_code=400, detail=f"Tipo inválido. Escolha entre: {valid_types}")

    valid_sort_fields = {"id": models.Tournament.id, "start_date": models.Tournament.start_date, "end_date": models.Tournament.end_date}
    sort_column = valid_sort_fields.get(sort_by, models.Tournament.start_date)
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Tournament).filter(models.Tournament.type.ilike(tournament_type)).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

