from unittest.mock import MagicMock
import pytest
import os
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService
from setup_db import db




@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    g1 = Genre(id=1, name="Thriller")
    g2 = Genre(id=2, name="Drama")
    g3 = Genre(id=3, name="Comedy")
    g4 = Genre(id=4, name="Action")
    g5 = Genre(id=5, name="Drama")

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3, g4, g5])
    genre_dao.create = MagicMock(return_value=Genre(id=5))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {"id": 6, "name": "sus genre"}
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_update(self):
        self.genre_service.delete(1)

    def test_delete(self):
        genre_d = {"id": 6, "name": "sus genre"}
        self.genre_service.update(genre_d)


if __name__ == '__main__':
    os.system("pytest")


