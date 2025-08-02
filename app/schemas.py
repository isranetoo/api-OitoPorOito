from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ========================= USERS =========================
class UserBase(BaseModel):
    username: str
    email: str
    password_hash: str
    profile_picture: Optional[str] = None
    country_code: Optional[str] = None
    bio: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True


# ========================= GAMES =========================
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
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ========================= PUZZLES =========================
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
        from_attributes = True


# ========================= TOURNAMENTS =========================
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
        from_attributes = True


# ========================= CLUBS =========================
class ClubBase(BaseModel):
    name: str
    description: Optional[str]
    owner_id: int

class ClubCreate(ClubBase):
    pass

class Club(ClubBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
