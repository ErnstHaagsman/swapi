from dataclasses import dataclass
from datetime import datetime
from typing import List

import dateutil.parser
import requests

@dataclass
class StarWarsMovie:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: datetime
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    created: datetime
    edited: datetime
    url: str

    def __post_init__(self):
        if type(self.release_date) is str:
            self.release_date = dateutil.parser.parse(self.release_date)

        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)

        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)

if __name__ == '__main__':
    json = requests.get('https://swapi.co/api/films/1/').json()

    movie = StarWarsMovie(**json)