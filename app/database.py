from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Usando SQLite provisoriamente (cria chess.db na raiz do projeto)
DATABASE_URL = "sqlite:///./chess.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
