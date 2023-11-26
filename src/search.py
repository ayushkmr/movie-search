"""
This module is responsible for searching through indexed movie data.

The Search class encapsulates the logic for performing searches
by using the pre-built index. It also makes use of the helper functions
in the search_utils.py module.
"""

from src.utils.search_utils import (
    print_results,
    print_no_result_message,
    get_movies_by_year,
    sort_by_rating,
    try_parse_date
)
from src.models.movie import Movie
from src.index import Index
from typing import Dict, List

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
    """

    def __init__(self, index: Index, num_results: int = 3, no_result_message: str = 'No results found'):
        """
        Constructs all the necessary attributes for the Search object.

        Parameters
        ----------
        index : Index
            An index object that the Search object will use to perform searches.
        num_results : int
            The number of search results to display (by default is 3).
        no_result_message : str
            A message to display when no results are found (by default is 'No results found').
        """
        self.index = index.index
        self.year_index = index.year_index
        self.num_results = num_results
        self.no_result_message = no_result_message
        rated_movies = [movie for movie in index.movies if movie.rating_value is not None]
        self.top_rated_movies = sort_by_rating(rated_movies, num_results)

    def perform_search(self, query: str):
        """
        Performs a search using the query, and prints out the top matching movies
        or movies published on a specific date or year if the query is a date.

        Parameters
        ----------
        query: str
            The search query or date.
        """
        # First, check if the query matches the name of a movie exactly
        movies = [movie for movie_list in self.index.values() for movie in movie_list
                  if movie.name.lower() == query.lower()]

        if movies:  # If there are matches, print them
            print_results(sort_by_rating(movies, self.num_results), self.num_results)
            return

        # If no exact name match found, then try to parse the query as a date
        date = try_parse_date(query)
        if date:  # If query is a date
            # No need to check for movies matching this date
            # Just get movies by the year of the query date
            self.get_movies_by_year(date.year)

        else:  # If the query is not a valid date, treat it as a string
            result_set = {movie for word in query.lower().split() if word in self.index for movie in self.index[word]}
            if result_set:
                print_results(sort_by_rating(list(result_set), self.num_results), self.num_results)
            else:
                print_no_result_message(self.no_result_message, self.top_rated_movies)

    def get_movies_by_year(self, year: int):
        """
        Wrapper function for the get_movies_by_year in search_utils.

        Parameters
        ----------
        year : int
            The year to find movies from.
        """
        get_movies_by_year(self.year_index, year, self.num_results)