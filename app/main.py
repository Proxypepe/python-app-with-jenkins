"""Some module"""
import json


class MovieJsonLoader:
    """
    Class for get movies from json file.
    """

    def __init__(self, file_path: str):
        self.movies = []
        with open(file_path, encoding='utf-8') as json_file:
            self.movies = json.load(json_file)

    def get_rank(self, index: int) -> str:
        """
        Getting access to movie rank by index
        """
        assert index > -1
        return self.movies[index]['rank']

    def get_title(self, index: int) -> str:
        """
        Getting access to movie title by index
        """
        assert index > -1
        return self.movies[index]['title']

    def get_id(self, index: int) -> str:
        """
        Getting access to movie id by index
        """
        assert index > -1
        return self.movies[index]['id']
