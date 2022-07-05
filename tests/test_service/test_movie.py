from unittest.mock import MagicMock
import pytest
import os
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db




@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    m1 = Movie(id=1, title="Joker",
               description="A mentally troubled stand-up comedian embarks on a downward spiral that leads to the creation of an iconic villain.",
               trailer="https://www.youtube.com/watch?v=zAGVQLHvwOY", year=2019, rating=8.4, genre_id=1, director_id=1)
    m2 = Movie(id=2, title="Once Upon a Time... In Hollywood",
               description="A faded television actor and his stunt double strive to achieve fame and success in the final years of Hollywood's Golden Age in 1969 Los Angeles.",
               trailer="https://www.youtube.com/watch?v=ELeMaP8EPAA", year=2019, rating=7.6, genre_id=2, director_id=2)
    m3 = Movie(id=3, title="What We Do in the Shadows",
               description="Viago, Deacon, and Vladislav are vampires who are struggling with the mundane aspects of modern life, like paying rent, keeping up with the chore wheel, trying to get into nightclubs, and overcoming flatmate conflicts.",
               trailer="https://www.youtube.com/watch?v=IAZEWtyhpes", year=2014, rating=7.6, genre_id=3, director_id=3)
    m4 = Movie(id=4, title="John Wick: Chapter 3 - Parabellum",
               description="John Wick is on the run after killing a member of the international assassins' guild, and with a $14 million price tag on his head, he is the target of hit men and women everywhere.",
               trailer="https://www.youtube.com/watch?v=M7XM597XO94", year=2019, rating=7.4, genre_id=4, director_id=4)
    m5 = Movie(id=5, title="Uncut Gems",
               description="With his debts mounting and angry collectors closing in, a fast-talking New York City jeweler risks everything in hope of staying afloat and alive.",
               trailer="https://www.youtube.com/watch?v=vTfJp2Ts9X8", year=2019, rating=7.4, genre_id=5, director_id=5)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3, m4, m5])
    movie_dao.get_by_year = MagicMock(return_value=m1)
    movie_dao.get_by_genre_id = MagicMock(return_value=m1)
    movie_dao.get_by_director_id = MagicMock(return_value=m1)
    movie_dao.create = MagicMock(return_value=Movie(id=5))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all({"director_id": 1})
        assert movies is not None

    def test_create(self):
        movie_d = {"title": "Joker",
               "description": "A mentally troubled stand-up comedian embarks on a downward spiral that leads to the creation of an iconic villain.",
               "trailer": "https://www.youtube.com/watch?v=zAGVQLHvwOY", "year": 2019, "rating": 8.4, "genre_id": 1, "director_id": 1}
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        self.movie_service.delete(5)

    def test_delete(self):
        movie_d = {"id": 1, "title": "Joker",
               "description": "A mentally troubled stand-up comedian embarks on a downward spiral that leads to the creation of an iconic villain.",
               "trailer": "https://www.youtube.com/watch?v=zAGVQLHvwOY", "year": 2019, "rating": 8.4, "genre_id": 1, "director_id": 1}
        self.movie_service.update(movie_d)


if __name__ == '__main__':
    os.system("pytest")


