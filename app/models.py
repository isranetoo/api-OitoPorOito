from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

# ===== User =====
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100)) 
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    profile_picture = Column(Text)
    country_code = Column(String(2))
    federation = Column(String(3))  # <-- Código da federação FIDE
    global_rank = Column(Integer)   # <-- Posição no ranking mundial
    global_rating = Column(Integer) # <-- Rating global
    bio = Column(Text)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime)

    ratings = relationship("Rating", back_populates="user")

# ===== Rating =====
class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    mode = Column(String(20), nullable=False)  # bullet, blitz, rapid, puzzle
    rating = Column(Integer, default=1200)
    highest_rating = Column(Integer)
    updated_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="ratings")

# ===== Game =====
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    white_player_id = Column(Integer, ForeignKey("users.id"))
    black_player_id = Column(Integer, ForeignKey("users.id"))
    mode = Column(String(20), nullable=False)
    time_control = Column(String(20))
    status = Column(String(20), default="in_progress")
    result = Column(String(10))
    started_at = Column(DateTime, default=func.now())
    finished_at = Column(DateTime)

# ===== Puzzle =====
class Puzzle(Base):
    __tablename__ = "puzzles"

    id = Column(Integer, primary_key=True, index=True)
    fen = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)
    theme = Column(String(50))
    difficulty = Column(String(20))

# ===== Tournament =====
class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))
    mode = Column(String(20))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

# ===== Club =====
class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
