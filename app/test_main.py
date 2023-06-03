"""Testing Some module"""
import pytest

from main import MovieJsonLoader


@pytest.fixture(name="movie_json_loader")
def movie_json_loader_fixture():
    """
    Fixture
    """
    return MovieJsonLoader('movies.json')


def test_rank(movie_json_loader):
    """ 
    Checking work with rank 
    """
    assert movie_json_loader.get_rank(0) == '1'


def test_title(movie_json_loader):
    """
    Checking work with title
    """
    assert movie_json_loader.get_title(0) == 'The Shawshank Redemption'


def test_id(movie_json_loader):
    """
    Checking work with id
    """
    assert movie_json_loader.get_id(0) == 'tt0111161'
