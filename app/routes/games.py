from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/games", tags=["Games"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar jogo
@router.post("/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

# Listar todos os jogos
@router.get("/", response_model=list[schemas.Game])
def get_games(db: Session = Depends(get_db)):
    return db.query(models.Game).all()

# Buscar partidas por jogador
@router.get("/player/{player_id}", response_model=list[schemas.Game])
def get_games_by_player(player_id: int, db: Session = Depends(get_db)):
    games = db.query(models.Game).filter(
        (models.Game.white_player_id == player_id) |
        (models.Game.black_player_id == player_id)
    ).all()
    if not games:
        raise HTTPException(status_code=404, detail="Nenhuma partida encontrada para este jogador")
    return games
