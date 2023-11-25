"""
This module is responsible for building an index from movie data.
"""

from collections import defaultdict
from src.models.movie import Movie
from typing import List, Dict

class Index:
    """
    A class used to represent an index of movie data for search engine. 

    Attributes
    ----------
    movies : List[Movie]
        a list of Movie objects to be indexed
    index : Dict[str, List[str]]
        a dictionary containing words mapped to movie names where it appears

    Methods
    -------
    build_index()
        Builds the inverted index from the movie data.
    """
    def __init__(self, movies: List[Movie]):
        """
        Constructs all the necessary attributes for the Index object.

        Parameters
        ----------
            movies : List[Movie]
                a list of Movie objects to be indexed
        """
        self.movies = movies
        self.index = self.build_index()

    def build_index(self) -> Dict[str, List[str]]:
        """
        Builds the inverted index from the movie data.

        Returns
        ----------
        Dict[str, List[str]]
            A dictionary with words as keys and a list of movie names as values.
        """
        index = defaultdict(list)
        
        for movie in self.movies:
            index_data = f"{movie.name} {movie.description} \
                          {' '.join([actor.name for actor in movie.actors])} \
                          {' '.join([director.name for director in movie.directors])} \
                          {' '.join([creator.name for creator in movie.creators])} \
                          {' '.join([genre.name for genre in movie.genres])} \
                          {movie.rating} {movie.content_rating} {movie.duration} \
                          {movie.image} {movie.url} {str(movie.date_published)} \
                          {movie.trailer} {movie.type}".lower().split()

            for word in index_data:
                if movie.name not in index[word]:
                    index[word].append(movie.name)
                    
        return index
