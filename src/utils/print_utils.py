"""
This module contains utility functions for printing search results.
"""

from typing import List
from src.models.movie import Movie
from src.utils.utils import sort_by_rating

def print_no_results(movies, num_results):
    """
    Print suggestion of top rated movies when no matching results are found.
    """
    # Sort the list of Movies based on ratings
    top_movies = sort_by_rating(movies, num_results)

    print("\n--- No Results Found ---")
    print("Here are some of the top rated movies of all time:")
    for i, movie in enumerate(top_movies, start=1):
        print(f"{i}. {movie.name} ({movie.year})")

def print_exact_match_results(movies: List[Movie]):
    """
    Print movies from exact match search.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    """
    print("\n--- Exact Match found ---")
    print("\nMovies found:")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie.name} ({movie.year})")

def print_probable_match_results(movies: List[Movie]):
    """
    Print movies from probable/fuzzy match search.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    """
    if movies:
        print("\n\n--- Probable Matches found ---")
        print("\nMovies found:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print("\nNo Probable Matches Found.")

def print_search_results_for_actor(movies: List[Movie], actor: str):
    """
    Print movies for a specific actor.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    actor: str
        The actor's name.
    """
    if movies:
        print(f"\n\nMovies with actor, {actor}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found with actor, {actor}.")

def print_search_results_for_year(movies: List[Movie], year: int):
    """
    Print movies for a specific year.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    year: int
        The year of movies.
    """
    if movies:
        print(f"\n\nMovies from the year, {year}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found from the year, {year}.")

def print_search_results_for_directors(movies: List[Movie], director: str):
    """
    Print movies from a specific director.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    director: str
        The director's name.
    """
    if movies:
        print(f"\n\nMovies by director, {director}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found by director, {director}.")

def print_search_results_for_creator(movies: List[Movie], creator: str):
    """
    Print movies from a specific creator.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    creator: str
        The creator's name.
    """
    if movies:
        print(f"\n\nMovies by creator, {creator}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found by creator, {creator}.")

def print_search_results_for_genre(movies: List[Movie], genre: str):
    """
    Print movies for a specific genre.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    genre: str
        The genre name.
    """
    if movies:
        print(f"\n\nMovies in genre, {genre}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found in genre, {genre}.")

def print_search_results_for_movie_name(movies: List[Movie], movie_name: str):
    """
    Print movies for a specific movie name.

    Parameters
    ----------
    movies: List[Movie]
        The list of movies found from the search.
    movie_name: str
        The movie name.
    """
    if movies:
        print(f"\n\nMovies with name, {movie_name}:")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie.name} ({movie.year})")
    else:
        print(f"\nNo Movies Found with name, {movie_name}.")