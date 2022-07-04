from unittest.mock import MagicMock
import pytest
import os

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService
from setup_db import db




@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    d1 = Director(id=1, name="Todd Phillips")
    d2 = Director(id=2, name="Quentin Tarantino")
    d3 = Director(id=3, name="Taika Waititi")
    d4 = Director(id=4, name="Chad Stahelski")
    d5 = Director(id=5, name="Benny Safdie")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3, d4, d5])
    director_dao.create = MagicMock(return_value=Director(id=5))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        movies = self.director_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {"id": 6, "name": "Vasya Pupkin"}
        movie = self.director_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        self.director_service.delete(1)

    def test_delete(self):
        movie_d = {"id": 6, "name": "Vasya Pupkin"}
        self.director_service.update(movie_d)


if __name__ == '__main__':
    os.system("pytest")


