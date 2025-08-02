from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# ===== User & Rating =====
class RatingBase(BaseModel):
    mode: str
    rating: int
    highest_rating: Optional[int]

class Rating(RatingBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2

class UserBase(BaseModel):
    username: str
    email: str
    country_code: Optional[str]
    bio: Optional[str]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    last_login: Optional[datetime]
    ratings: List[Rating] = []

    class Config:
        from_attributes = True  # Pydantic v2

# ===== Game =====
class GameBase(BaseModel):
    white_player_id: int
    black_player_id: int
    mode: str
    time_control: Optional[str]
    status: Optional[str]
    result: Optional[str]

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    started_at: datetime
    finished_at: Optional[datetime]

    class Config:
        from_attributes = True  # Pydantic v2

# ===== Puzzle =====
class PuzzleBase(BaseModel):
    fen: str
    solution: str
    theme: Optional[str]
    difficulty: Optional[str]

class PuzzleCreate(PuzzleBase):
    pass

class Puzzle(PuzzleBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2

# ===== Tournament =====
class TournamentBase(BaseModel):
    name: str
    type: Optional[str]
    mode: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

class TournamentCreate(TournamentBase):
    pass

class Tournament(TournamentBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2

# ===== Club =====
class ClubBase(BaseModel):
    name: str
    description: Optional[str]
    owner_id: int

class ClubCreate(ClubBase):
    pass

class Club(ClubBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2
