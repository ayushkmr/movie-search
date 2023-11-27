"""
This module contains utility functions that are used by the Search object to sort movies by rating value, 
print out the search results, print no result message, and get movies by a particular year. 
It includes functions used to parse a string into a date in strict 'YYYY-MM-DD' format as 
well as search functions to find movies by year, actor's name, creator name, and genre.
"""

from typing import Dict, List
from fuzzywuzzy import fuzz
from operator import attrgetter
from src.models.movie import Movie
from src.index import Index

import logging

logger = logging.getLogger('movie_search')

def perform_exact_search(movies: List[Movie], query: str) -> List[Movie]:
    """
    Performs an exact match search by looking for the query as a substring in the movie's name.

    Parameters
    ----------
    movies : List[Movie]
        The list of movies where we should search.
    query : str
        The search query.

    Returns
    -------
    List[Movie]
        List of movies that contain the exact search query in their names.
    """
    logger.debug("Performing exact search with query: %s", query)
    movies_match = [movie for movie in movies if query.lower() in movie.name.lower()]
    logger.debug("Exact search movies: %s", [movie.name for movie in movies_match])
    return movies_match

def perform_combined_search(index: Index, query: str) -> List[Movie]:
    """
    Attempts to iteratively find matches for chunks of the query within movie names.

    Parameters
    ----------
    index : Index
        An index object containing words mapped to movies where it appears.
    query : str
        The search query (which will be split into chunks).

    Returns
    -------
    list[Movie]
        List of unique movies that match all chunks of the query.
    """
    logger.debug("Performing combined index and chunked query search with query: %s", query)
    chunks = query.lower().split()

    intersect_movies = set(index.index[chunks[0]]) if chunks else set()

    for chunk in chunks[1:]:
        intersect_movies &= set(index.index[chunk])

    logger.debug("Combined index and chunk search movies: %s", [movie.name for movie in intersect_movies])
    return list(intersect_movies)

def perform_fuzzy_search(movies: List[Movie], query: str, fuzz_ratio: int) -> List[Movie]:
    """
    Attempts to find fuzzy matches of the chunks of the query in movie names.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    query: str
        The search query.
    fuzz_ratio: int
        The minimum similarity ratio to be considered a match in a fuzzy search.

    Returns
    -------
    list[Movie]
        List of unique movies that match all chunks of the query based on fuzziness.
    """
    logger.debug("Performing fuzzy search with query: %s", query)
    chunks = query.lower().split()
    intersect_movies = set(movie for movie in movies if fuzz.ratio(chunks[0], movie.name.lower()) >= fuzz_ratio) if chunks else set()

    for chunk in chunks[1:]:
        intersect_movies &= set(movie for movie in movies if fuzz.ratio(chunk, movie.name.lower()) >= fuzz_ratio)

    logger.debug("Fuzzy search movies: %s", [movie.name for movie in intersect_movies])
    return list(intersect_movies)

def perform_json_search(movies: List[Movie], query: str) -> List[Movie]:
    """
    Performs a JSON substring search by looking for the query as a substring in the movie's raw_json.
    It only performs the search when the query contains non-alphanumeric characters.

    Parameters
    ----------
    movies : List[Movie]
        The list of movies where we should search.
    query : str
        The search query.
        
    Returns
    -------
    List[Movie]
        List of movies where the raw_json contains the search query.
    """
    if query.isalnum():  # If the query contains only alphanumeric characters, return an empty list
        return []

    logger.debug("Performing JSON substring search with query: %s", query)
    query = query.lower()
    movies_match = [movie for movie in movies if query in movie.raw_json.lower()]
    logger.debug("JSON substring search movies: %s", [movie.name for movie in movies_match])
    return movies_match

def search_by_year(movies: List[Movie], year: int) -> List[Movie]:
    """
    Search for movies released in the specified year.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    year: int
        The year to search for.

    Returns
    -------
    list[Movie]
        List of movies released in the specified year.
    """
    return [movie for movie in movies if movie.year == year]

def search_by_actor(movies: List[Movie], actor: str) -> List[Movie]:
    """
    Search for movies featuring a specified actor.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    actor: str
        The name of the actor to search for.

    Returns
    -------
    list[Movie]
        List of movies that feature the specified actor.
    """
    return [movie for movie in movies if any(actor.lower() in a.name.lower() for a in movie.actors)]

def search_by_genre(movies: List[Movie], genre: str) -> List[Movie]:
    """
    Search for movies from a specified genre.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    genre: str
        The genre to search for.

    Returns
    -------
    list[Movie]
        List of movies from the specified genre.
    """
    return [movie for movie in movies if any(genre.lower() in g.name.lower() for g in movie.genres)]

def search_by_creator(movies: List[Movie], creator: str) -> List[Movie]:
    """
    Search for movies created by a specific person or entity.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    creator: str
        The creator to search for.

    Returns
    -------
    list[Movie]
        List of movies created by the specified person or entity.
    """
    return [movie for movie in movies if any(creator.lower() in c.name.lower() for c in movie.creators)]


def search_by_director(movies: List[Movie], director: str) -> List[Movie]:
    """
    Search for movies directed by a specific director.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies where we should search.
    director: str
        The director to search for.

    Returns
    -------
    list[Movie]
        List of movies directed by the specified director.
    """
    return [movie for movie in movies if any(director.lower() in d.name.lower() for d in movie.directors)]
