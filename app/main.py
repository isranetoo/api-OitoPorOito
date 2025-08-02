from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import users, games, puzzles, tournaments, clubs
from .routes import ratings


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Chess API")

# CORS para permitir frontend acessar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(users.router)
app.include_router(games.router)
app.include_router(puzzles.router)
app.include_router(tournaments.router)
app.include_router(clubs.router)
app.include_router(ratings.router)

@app.get("/")
def root():
    return {"message": "Chess API is running!"}
