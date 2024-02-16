"""
This module contains utility functions for converting Movie objects to JSON strings
and creating Movie objects from JSON strings.
"""

import json
from src.models.movie import Movie
from operator import attrgetter
from typing import List, Union, Optional


def movie_to_json(movie):
    """
    Convert a Movie object to a JSON string

    Parameters
    ----------
    movie : Movie
        The Movie object to convert to a JSON string

    Returns
    ----------
    str
        A JSON string representation of the Movie object
    """
    return json.dumps(movie.to_dict(), default=str, indent=4)


def json_to_movie(json_str):
    """
    Convert a JSON string to a Movie object

    Parameters
    ----------
    json_str : str
        The JSON string to convert to a Movie object

    Returns
    ----------
    Movie
        A Movie object representation of the JSON string
    """
    try:
        movie = Movie(json.loads(json_str))
        print(f"Movie successfully loaded: {movie.name}")
        return movie
    except Exception as e:
        print(f"Failed to load movie from json: {json_str}")
        print(f"Error: {e}")


def load_movies_from_json_file(filepath):
    """
    Load JSON data from a file and create a list of Movie objects.

    Parameters
    ----------
    filepath : str
        Path of the JSON file to read.

    Returns
    ----------
    list
        A list of Movie object representations of the JSON data.
    """

    movie_objects = []

    with open(filepath, "r", encoding="utf-8") as json_file:
        movies_json_array = json.load(json_file)

    for movie_json in movies_json_array:
        try:
            movie = json_to_movie(json.dumps(movie_json))
            movie_objects.append(movie)
            print(f"Successfully loaded movie: {movie.name}")
        except Exception as e:
            print(f"Unable to load movie. Error: {e}")

    return movie_objects


def sort_by_rating(
    movies: List[Movie], num_results: Optional[int] = None
) -> List[Movie]:
    """
    Sorts a list of Movies by rating_value and returns the top results.

    Parameters
    ---------
    movies: List[Movie]
        List of movies to sort.
    num_results: Optional[int]
        Number of results to return, will return all movies if num_results is None or not provided.

    Returns
    -------
    List[Movie]
        Sorted list of movies.
    """
    sorted_movies = sorted(movies, key=attrgetter("rating_value"), reverse=True)
    return sorted_movies if num_results is None else sorted_movies[:num_results]
