import json
from datetime import datetime
from app.database import SessionLocal, engine, Base
from app import models

# Criar tabelas se não existirem
Base.metadata.create_all(bind=engine)

def parse_datetime(value):
    """Converte string ISO para datetime ou retorna None."""
    if value and isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except Exception:
            return None
    return None

def seed_database():
    db = SessionLocal()

    # Ler JSON
    with open("seed_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # ===== USERS =====
    for user in data.get("users", []):
        db_user = models.User(
            id=user["id"],
            username=user["username"],
            email=user["email"],
            password_hash=user["password_hash"],
            profile_picture=user.get("profile_picture"),
            country_code=user.get("country_code"),
            bio=user.get("bio"),
            created_at=parse_datetime(user.get("created_at")),
            last_login=parse_datetime(user.get("last_login"))
        )
        db.merge(db_user)

    # ===== GAMES =====
    for game in data.get("games", []):
        db_game = models.Game(
            id=game["id"],
            white_player_id=game["white_player_id"],
            black_player_id=game["black_player_id"],
            mode=game["mode"],
            time_control=game.get("time_control"),
            status=game.get("status"),
            result=game.get("result"),
            started_at=parse_datetime(game.get("started_at")),
            finished_at=parse_datetime(game.get("finished_at"))
        )
        db.merge(db_game)

    # ===== PUZZLES =====
    for puzzle in data.get("puzzles", []):
        db_puzzle = models.Puzzle(
            id=puzzle["id"],
            fen=puzzle["fen"],
            solution=puzzle["solution"],
            theme=puzzle.get("theme"),
            difficulty=puzzle.get("difficulty")
        )
        db.merge(db_puzzle)

    # ===== TOURNAMENTS =====
    for t in data.get("tournaments", []):
        db_tournament = models.Tournament(
            id=t["id"],
            name=t["name"],
            type=t.get("type"),
            mode=t.get("mode"),
            start_date=parse_datetime(t.get("start_date")),
            end_date=parse_datetime(t.get("end_date"))
        )
        db.merge(db_tournament)

    # ===== CLUBS =====
    for club in data.get("clubs", []):
        db_club = models.Club(
            id=club["id"],
            name=club["name"],
            description=club.get("description"),
            owner_id=club["owner_id"],
            created_at=parse_datetime(club.get("created_at"))
        )
        db.merge(db_club)

    db.commit()
    db.close()
    print("✅ Banco SQLite populado com sucesso!")

if __name__ == "__main__":
    seed_database()
