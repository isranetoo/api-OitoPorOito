from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/clubs", tags=["Clubs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Club)
def create_club(club: schemas.ClubCreate, db: Session = Depends(get_db)):
    db_club = models.Club(**club.dict())
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club

@router.get("/", response_model=list[schemas.Club])
def get_clubs(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("created_at"),
    order: str = Query("desc")
):
    valid_sort_fields = {"id": models.Club.id, "created_at": models.Club.created_at, "name": models.Club.name}
    sort_column = valid_sort_fields.get(sort_by, models.Club.created_at)
    sort_func = desc if order.lower() == "desc" else asc

    query = db.query(models.Club).order_by(sort_func(sort_column))
    return query.offset((page - 1) * limit).limit(limit).all()

@router.get("/owner/{owner_id}", response_model=list[schemas.Club])
def get_clubs_by_owner(owner_id: int, db: Session = Depends(get_db)):
    clubs = db.query(models.Club).filter(models.Club.owner_id == owner_id).all()
    if not clubs:
        raise HTTPException(status_code=404, detail="Nenhum clube encontrado para este dono")
    return clubs
