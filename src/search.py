"""
This module is responsible for searching through indexed movie data.
"""

from collections import defaultdict
from operator import attrgetter
from typing import Dict, List
from src.index import Index
from src.models.movie import Movie

class Search:
    """
    A class used to represent a search engine that uses the index to perform searches.

    Attributes
    ----------
    index : Dict[str, List[str]]
        An index containing words mapped to movie names where it appears.
    num_results : int
        The number of search results to display.
    no_result_message : str
        The message to display when no results are found.
    top_rated_movies : List[str]
        A list of movie names of top-rated movies.

    Methods
    -------
    perform_search(query: str)
        Performs a search using the query, and prints out the top matching movies.
    """

    def __init__(self, index: Index, num_results: int = 3, no_result_message: str = 'No results found'):
        """
        Constructs all the necessary attributes for the Search object.
        
        Parameters
        ----------
        index : Index
            An index object that the Search object will use to perform searches.
        num_results : int
            The number of search results to display (default is 3).
        no_result_message : str
            The message to display when no results are found (default is 'No results found').
        """
        self.index = index.index
        self.year_index = index.year_index
        self.num_results = num_results
        self.no_result_message = no_result_message

        # Only consider movies that have a ratingValue
        rated_movies = [movie for movie in index.movies if movie.rating_value is not None]

        # Sort movies by ratingValue
        rated_movies.sort(key=attrgetter('rating_value'), reverse=True)

        # Keep top num_results movies
        self.top_rated_movies = rated_movies[:num_results]
        
    def get_movies_by_year(self, year: int): 
        """ Prints the names of top rated movies released in a particular year. """
        movies = self.year_index[year]
        if movies:
            print(f"Top rated movies from {year}:")
            for movie in movies:
                print(f'\t{movie.name}')
        else:
            print(f"No movies found from {year}.")

    def perform_search(self, query: str):
        """
        Performs a search using the query, and prints out the top matching movies.

        Parameters
        ----------
        query : str
            The search query.
        """
        results = defaultdict(int)
        for word in query.lower().split():
            for movie_name in self.index[word]:
                results[movie_name] += 1
        results = sorted(results.items(), key=lambda x: x[1], reverse=True)[:self.num_results]

        if not results:
            print(self.no_result_message)
            print('Showing top-rated movies instead:')
            for movie in self.top_rated_movies:
                print(movie.name)
        else:
            print(f'Top {min(self.num_results,len(results))} movies for your query:')
            for movie_name, _ in results:
                print(movie_name)