"""
This module contains utility functions that are used by the Search object 
to sort movies by rating value, print out the search results, print no result message,
get movies by a particular year. It also includes a function used to parse a string
into a date in strict 'YYYY-MM-DD' format.
"""

from typing import Dict, List, Union
from datetime import datetime
from operator import attrgetter
from src.models.movie import Movie

def print_results(movies: List[Movie], num_results: int, prefix: str = "\nTop"):
    """
    Print out the search results.
    
    Parameters
    ----------
    movies : list[Movie]
        List of movies to print.
    num_results : int
        Number of results to display.
    prefix : str, optional
        Prefix string for results output, default is '\nTop'
    """
    # Enforce uniqueness
    unique_movies = {movie.name: movie for movie in movies}

    # Select top N unique movies
    top_movies = sorted(unique_movies.values(), key=attrgetter('rating_value'), reverse=True)[:num_results]

    # Determine the number of printed results
    actual_num_results = len(top_movies)

    print(f"{prefix} {actual_num_results} result(s):")
    for movie in top_movies:
        print(f'\t{movie.name}')


def print_no_result_message(no_result_message: str, top_rated_movies: List[Movie]):
    """
    Prints no results message and displays top-rated movies.

    Parameters
    ----------
    no_result_message : str
        Message to display when no result is found.
    top_rated_movies : list[Movie]
        List of top-rated movies.
    """
    print(no_result_message)
    print('Showing top-rated movies instead:')
    for movie in top_rated_movies:
        print(f'\t{movie.name}')


def get_movies_by_year(year_index: Dict[int, List[Movie]], year: int, num_results: int):
    """
    Fetches and prints the names of top-rated movies released in a particular year,
    removing duplicates based on movie names.
    
    Parameters
    ----------
    year_index : dict
        Dictionary of movies indexed by their year.
    year : int
        The year to find movies from.
    num_results : int
        Number of results to display.
    """
    # Fetch movies by year from the year_index
    movies_by_year = year_index.get(year, [])
    
    # Enforce uniqueness with a dict
    unique_movies = {movie.name: movie for movie in movies_by_year}

    # Select top N unique movies
    top_movies = sorted(unique_movies.values(), key=attrgetter('rating_value'), reverse=True)[:num_results]

    # Get the actual number of results, to be used in the print statement
    results_count = len(top_movies)

    if top_movies:
        print(f"\nTop {results_count} result(s):")
        for movie in top_movies:
            print(f'\t{movie.name}')
    else:
        print(f"No movies found from the year {year}.")


def sort_by_rating(movies: List[Movie], num_results: int):
    """
    Sorts a list of Movies by rating value and returns the top results.

    Parameters
    ----------
    movies : list[Movie]
        List of movies to sort.
    num_results : int
        Number of results to return.

    Returns
    -------
    list[Movie]
        Sorted list of movies.
    """
    return sorted(movies, key=attrgetter('rating_value'), reverse=True)[:num_results]


def try_parse_date(text: str) -> Union[datetime, None]:
    """
    Tries to parse a string into a date in 'YYYY-MM-DD' format.
    If the string is not a valid date in 'YYYY-MM-DD' format, it returns None.
    Arguments:
        text : a string to parse into a date
    Returns:
        a datetime object if the string is a valid date; otherwise, None
    """
    try:
        return datetime.strptime(text, '%Y-%m-%d')
    except ValueError:
        return None