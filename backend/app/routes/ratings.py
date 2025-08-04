from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/ratings", tags=["Ratings"])

class PlayerRating(BaseModel):
    rank: int
    name: str
    federation: str
    rating: int
    birth_year: int

    class Config:
        from_attributes = True

# Dados mockados com base na imagem
players_data = [
    {"rank": 1, "name": "Magnus Carlsen", "federation": "NOR", "rating": 2839, "birth_year": 1990},
    {"rank": 2, "name": "Hikaru Nakamura", "federation": "USA", "rating": 2807, "birth_year": 1987},
    {"rank": 3, "name": "Fabiano Caruana", "federation": "USA", "rating": 2784, "birth_year": 1992},
    {"rank": 4, "name": "Rameshbabu Praggnanandhaa", "federation": "IND", "rating": 2779, "birth_year": 2005},
    {"rank": 5, "name": "Arjun Erigaisi", "federation": "IND", "rating": 2776, "birth_year": 2003},
    {"rank": 6, "name": "Gukesh Dommaraju", "federation": "IND", "rating": 2776, "birth_year": 2006},
    {"rank": 7, "name": "Nodirbek Abdusattorov", "federation": "UZB", "rating": 2771, "birth_year": 2004},
    {"rank": 8, "name": "Alireza Firouzja", "federation": "FRA", "rating": 2766, "birth_year": 2003},
    {"rank": 9, "name": "Wei Yi", "federation": "CHN", "rating": 2753, "birth_year": 1999},
    {"rank": 10, "name": "Anish Giri", "federation": "NED", "rating": 2748, "birth_year": 1994}
]

@router.get("/", response_model=List[PlayerRating])
def get_ratings():
    return players_data
