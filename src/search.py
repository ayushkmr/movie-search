"""
This module is responsible for searching through indexed movie data.

The Search class encapsulates the logic for performing searches
by using the pre-built index. It also makes use of the helper functions
in the search_utils.py module.
"""

import logging
from typing import List, Dict
from src.models.movie import Movie
from src.utils.search_utils import *
from src.utils.print_utils import *

class Search:
    def __init__(self, movies: List[Movie], index: Dict[str, List[Movie]]):
        """
        Initialize the Search object with a list of movies and a word-to-movie index.
        """
        self.logger = logging.getLogger('movie_search')
        self.movies = movies
        self.index = index
        self.logger.info("Search object initialized.")

    def general_search(self, query: str, fuzz_ratio: int, num_results: int):
        """
        General search first performs combined chunked and index-based search,
        then an json search if query contains multiple words,
        and finally a fuzzy search if the total results are less than num_results.
        """
        self.logger.info(f"General search initiated with query: {query}")

        # Perform combined chunked and index search
        index_search_movies = perform_combined_search(self.index, query)

        # Perform json search if query contains multiple words or special chars
        json_search_movies = perform_json_search(self.movies, query)

        # Combine and get unique movies from index search and json search
        combined_movies = list(dict.fromkeys(index_search_movies + json_search_movies))

        movies_found = set(combined_movies)
        
        # Print results of combined search
        if combined_movies:
            print_exact_match_results(combined_movies[:num_results])

        # If the count of combined results is less than num_results, perform fuzzy search
        if len(combined_movies) < num_results:
            fuzzy_search_movies = perform_fuzzy_search(self.movies, query, fuzz_ratio)
            
            # Filter out movies already displayed by the combined search
            fuzzy_search_movies = [movie for movie in fuzzy_search_movies if movie not in combined_movies]
            
            movies_found.update(fuzzy_search_movies)

            # Print fuzzy results
            if fuzzy_search_movies:
                print_probable_match_results(fuzzy_search_movies[:(num_results - len(combined_movies))])
            
            
        if len(movies_found) == 0:
            print_no_results(self.movies, num_results)

        self.logger.info(f"General search completed with total {len(movies_found)} results found.")

    def search_by_year(self, year: int, num_results: int):
        """
        Search for movies released in a specific year.
        """
        self.logger.info(f"Search by year initiated for year: {year}")
        year_movies = search_by_year(self.movies, year)[:num_results]
        if year_movies:
            print_search_results_for_year(year_movies, year)
        self.logger.info(f"Search by year completed with {len(year_movies)} results found.")

    def search_by_genre(self, genre: str, num_results: int):
        """
        Search for movies within a specific genre.
        """
        self.logger.info(f"Search by genre initiated for genre: {genre}")
        genre_movies = search_by_genre(self.movies, genre)[:num_results]
        if genre_movies:
            print_search_results_for_genre(genre_movies, genre)
        self.logger.info(f"Search by genre completed with {len(genre_movies)} results found.")

    def search_by_actor(self, actor: str, num_results: int):
        """
        Search for movies by a specific actor.
        """
        self.logger.info(f"Search by actor initiated for actor: {actor}")
        actor_movies = search_by_actor(self.movies, actor)[:num_results]
        if actor_movies:
            print_search_results_for_actor(actor_movies, actor)
        self.logger.info(f"Search by actor completed with {len(actor_movies)} results found.")

    def search_by_creator(self, creator: str, num_results: int):
        """
        Search for movies by a specific creator.
        """
        self.logger.info(f"Search by creator initiated for creator: {creator}")
        creator_movies = search_by_creator(self.movies, creator)[:num_results]
        if creator_movies:
            print_search_results_for_creator(creator_movies, creator)
        self.logger.info(f"Search by creator completed with {len(creator_movies)} results found.")
    
    def search_by_director(self, director: str, num_results: int):
        """
        Search for movies by a specific director.
        """
        self.logger.info(f"Search by director initiated for director: {director}")
        director_movies = search_by_director(self.movies, director)[:num_results]
        if director_movies:
            print_search_results_for_directors(director_movies, director)
        self.logger.info(f"Search by director completed with {len(director_movies)} results found.")

    def search_by_movie_name(self, movie_name: str, num_results: int):
        """
        Search for movie by a specific movie name.
        """
        self.logger.info(f"Search by movie name initiated for movie name: {movie_name}")
        
        movie_name = movie_name.lower()
        movie_name_movies = [movie for movie in self.movies if movie_name in movie.name.lower()][:num_results]
        if movie_name_movies:
            print_search_results_for_movie_name(movie_name_movies, movie_name)
        self.logger.info(f"Search by movie name completed with {len(movie_name_movies)} results found.")
