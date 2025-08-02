from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

# Dependency para abrir/fechar sessão no banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar usuário
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verifica se já existe usuário com mesmo e-mail
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")

    # Cria o usuário (por enquanto sem hash real)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=user.password,  # depois trocar para hash com passlib
        country_code=user.country_code,
        bio=user.bio
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Listar todos os usuários
@router.get("/", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Buscar usuário por ID
@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user
