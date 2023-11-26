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
    index : Dict[str, List[Movie]]
        An index containing words mapped to movies where it appears.
    year_index : Dict[int, List[Movie]]
        An index containing years mapped to movies released in those years.
    num_results : int
        The number of search results to display.
    no_result_message : str
        The message to display when no results are found.
    top_rated_movies : List[Movie]
        A list of top-rated movies.

    Methods
    -------
    perform_search(query: str)
        Performs a search using the query, and prints out the top matching movies.
    get_movies_by_year(year: int):
        Prints the names of top rated movies released in a particular year.
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

        # Only consider movies that have a rating_value
        rated_movies = [movie for movie in index.movies if movie.rating_value is not None]

        # Sort movies by ratingValue
        rated_movies.sort(key=attrgetter('rating_value'), reverse=True)

        # Keep top num_results movies
        self.top_rated_movies = rated_movies[:num_results]

    def get_movies_by_year(self, year: int): 
        """ Prints the names of top-rated movies released in a particular year. """
        movies = self.year_index[year]
        num_results_to_show = min(len(movies), self.num_results)
        if movies:
            print(f"\nTop {num_results_to_show} movies from {year}:")
            for movie in sorted(movies, key=attrgetter('rating_value'), reverse=True)[:num_results_to_show]:
                print(f'\t{movie.name}')
        else:
            print(f"No movies found from {year}.")

    def perform_search(self, query: str):
        """
        Perform search for the query
        """
        query_words = query.lower().split()
        result_set = []

        for word in query_words:
            if word in self.index:
                result_set.extend(self.index[word])

        # If we found some results, sort them by rating_value and display top results
        if result_set:
            result_set.sort(key=attrgetter('rating_value'), reverse=True)
            num_results_to_show = min(len(result_set), self.num_results)
            print(f"\nTop {num_results_to_show} results:")
            for movie in result_set[:num_results_to_show]:
                print(f'\t{movie.name}')

        # If no result was found, print top-rated movies.
        else:
            print(self.no_result_message)
            print('Showing top-rated movies instead:')
            for movie in self.top_rated_movies:
                print(f'\t{movie.name}')
