"""
This module is responsible for building an index from movie data.
"""

from collections import defaultdict
from operator import attrgetter
from src.models.movie import Movie
from typing import List, Dict
from nltk.corpus import stopwords

class Index:
    """
    A class used to represent an index of movie data for a search engine. 

    Attributes
    ----------
    movies : List[Movie]
        a list of Movie objects to be indexed
    index : Dict[str, List[str]]
        a dictionary containing words mapped to movie names where they appear
    year_index : Dict[int, List[Movie]]
        a dictionary containing years mapped to movie names from that year
    stop_words : set
        a set of commonly used words in English to be filtered out

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
        self.index = defaultdict(list)
        self.year_index = defaultdict(list)
        self.stop_words = set(stopwords.words('english')) # set of nltk stop words
        self.build_index()

    def index_field(self, field, movie_name):
        """
        Index a field for a specific movie.

        Parameters
        ----------
        field : str
            space-separated words representation of a field
        movie_name : str
            name of the movie associated with the field
        """
        for word in field.lower().split():
            if word not in self.stop_words and movie_name not in self.index[word]:
                self.index[word].append(movie_name)


    # Indexing logic for the movie name
    def index_movie_name(self, movie):
        self.index_field(movie.name, movie.name)

    # Indexing logic for the movie description
    def index_movie_description(self, movie):
        self.index_field(movie.description, movie.name)

    # Indexing logic for the movie actors
    def index_movie_actors(self, movie):
        self.index_field(' '.join([actor.name for actor in movie.actors]), movie.name)

    # Indexing logic for movie directors
    def index_movie_directors(self, movie):
        self.index_field(' '.join([director.name for director in movie.directors]), movie.name)
    
    # Indexing logic for movie creators
    def index_movie_creators(self, movie):
        self.index_field(' '.join([creator.name for creator in movie.creators]), movie.name)

    # Indexing logic for movie genres
    def index_movie_genres(self, movie):
        self.index_field(' '.join([genre.name for genre in movie.genres]), movie.name)

    # Indexing logic for movie rating
    # def index_movie_rating(self, movie):
    #     self.index_field(movie.rating, movie.name)

    # Indexing logic for movie content_rating
    # def index_movie_content_rating(self, movie):
    #     self.index_field(movie.content_rating, movie.name)

    # Indexing logic for movie duration
    def index_movie_duration(self, movie):
        self.index_field(movie.duration, movie.name)

    # Indexing logic for movie image
    def index_movie_image(self, movie):
        self.index_field(movie.image, movie.name)

    # Indexing logic for movie url
    def index_movie_url(self, movie):
        self.index_field(movie.url, movie.name)

    # Indexing logic for movie date_published
    def index_movie_date_published(self, movie):
        self.index_field(str(movie.date_published), movie.name)

    # Indexing logic for movie trailer
    # def index_movie_trailer(self, movie):
    #     self.index_field(movie.trailer, movie.name)

    def index_movie_by_year(self, movie: Movie, top_n=3):
        """
        Adds a movie to the year index based on its published year.
        Keeps only top N movies per year based on rating.
        """
        if movie.year:
            self.year_index[movie.year].append(movie)
            # Sort movies by rating and keep only the top N
            self.year_index[movie.year] = sorted(
                self.year_index[movie.year], key=attrgetter('rating_value'), reverse=True
            )[:top_n]

    # Indexing logic for movie type
    def index_movie_type(self, movie):
        self.index_field(movie.type, movie.name)

    def build_index(self):
        """
        Builds the inverted index from the movie data.
        """
        for movie in self.movies:
            self.index_movie_name(movie)
            self.index_movie_description(movie)
            self.index_movie_actors(movie)
            self.index_movie_directors(movie)
            self.index_movie_creators(movie)
            self.index_movie_genres(movie)
            # self.index_movie_rating(movie)
            # self.index_movie_content_rating(movie)
            self.index_movie_duration(movie)
            self.index_movie_image(movie)
            self.index_movie_url(movie)
            self.index_movie_date_published(movie)
            # self.index_movie_trailer(movie)
            self.index_movie_by_year(movie)
            self.index_movie_type(movie)
