from datetime import datetime
from typing import List

from pydantic import BaseModel, HttpUrl


class PersonResponse(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: HttpUrl
    films: List[HttpUrl]
    species: List[HttpUrl]
    vehicles: List[HttpUrl]
    starships: List[HttpUrl]
    created: datetime
    edited: datetime
    url: HttpUrl
