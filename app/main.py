from fastapi import FastAPI
from . import models, database
from .routes import users, games, puzzles, tournaments, clubs

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Chess API")

app.include_router(users.router)
app.include_router(games.router)
app.include_router(puzzles.router)
app.include_router(tournaments.router)
app.include_router(clubs.router)

@app.get("/")
def root():
    return {"message": "Chess API is running!"}
