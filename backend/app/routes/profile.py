from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from app.database import get_db
from app import models
from pydantic import BaseModel

router = APIRouter(prefix="/profile", tags=["Profile"])

# ======== MODELOS Pydantic para resposta ========
class RatingSchema(BaseModel):
    bullet: Optional[int] = None
    blitz: Optional[int] = None
    rapid: Optional[int] = None
    daily: Optional[int] = None

class GameHistorySchema(BaseModel):
    opponent: str
    mode: str
    result: str
    played_at: datetime

class UserProfileSchema(BaseModel):
    username: str
    name: Optional[str] = None
    email: str
    profile_picture: Optional[str] = None
    country_code: Optional[str] = None
    bio: Optional[str] = None
    ratings: RatingSchema
    game_history: List[GameHistorySchema]

# ======== ENDPOINT ========
@router.get("/{username}", response_model=UserProfileSchema)
def get_profile(username: str, db: Session = Depends(get_db)):
    # Buscar usuário
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Buscar ratings e converter para dict
    ratings_db = db.query(models.Rating).filter(models.Rating.user_id == user.id).all()
    ratings_dict = {r.mode: r.rating for r in ratings_db}

    # Buscar histórico de partidas (últimas 10)
    games = db.query(models.Game).filter(
        (models.Game.white_player_id == user.id) | (models.Game.black_player_id == user.id)
    ).order_by(models.Game.started_at.desc()).limit(10).all()

    history = []
    for g in games:
        opponent_id = g.black_player_id if g.white_player_id == user.id else g.white_player_id
        opponent = db.query(models.User).filter(models.User.id == opponent_id).first()
        history.append(GameHistorySchema(
            opponent=opponent.username if opponent else "Desconhecido",
            mode=g.mode,
            result=g.result,
            played_at=g.started_at
        ))

    return UserProfileSchema(
        username=user.username,
        name=getattr(user, "name", None),  # vai ser None se não tiver no modelo
        email=user.email,
        profile_picture=user.profile_picture,
        country_code=user.country_code,
        bio=user.bio,
        ratings=RatingSchema(**ratings_dict),
        game_history=history
    )
