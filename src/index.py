"""
This module is responsible for building an index from movie data.
"""

from collections import defaultdict
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
    index : Dict[str, List[Movie]]
        a dictionary containing words mapped to movies where they appear
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

    def index_field(self, field, movie: Movie):
        """
        Index a field for a specific movie.

        Parameters
        ----------
        field : str
            space-separated words representation of a field
        movie : Movie
            movie associated with the field
        """
        for word in field.lower().split():
            if word not in self.stop_words and movie not in self.index[word]:
                self.index[word].append(movie)

    # Indexing logic for the movie name
    def index_movie_name(self, movie):
        self.index_field(movie.name, movie)

    # Indexing logic for the movie description
    def index_movie_description(self, movie):
        self.index_field(movie.description, movie)

    # Indexing logic for the movie actors
    def index_movie_actors(self, movie):
        self.index_field(' '.join([actor.name for actor in movie.actors]), movie)

    # Indexing logic for movie directors
    def index_movie_directors(self, movie):
        self.index_field(' '.join([director.name for director in movie.directors]), movie)
    
    # Indexing logic for movie creators
    def index_movie_creators(self, movie):
        self.index_field(' '.join([creator.name for creator in movie.creators]), movie)

    # Indexing logic for movie genres
    def index_movie_genres(self, movie):
        self.index_field(' '.join([genre.name for genre in movie.genres]), movie)

    # Indexing logic for movie rating
    # def index_movie_rating(self, movie):
    #     self.index_field(movie.rating, movie.name)

    # Indexing logic for movie content_rating
    # def index_movie_content_rating(self, movie):
    #     self.index_field(movie.content_rating, movie.name)

    # Indexing logic for movie duration
    def index_movie_duration(self, movie):
        self.index_field(movie.duration, movie)

    # Indexing logic for movie image
    def index_movie_image(self, movie):
        self.index_field(movie.image, movie)

    # Indexing logic for movie url
    def index_movie_url(self, movie):
        self.index_field(movie.url, movie)

    # Indexing logic for movie date_published
    def index_movie_date_published(self, movie):
        self.index_field(str(movie.date_published), movie)


    # Indexing logic for movie trailer
    # def index_movie_trailer(self, movie):
    #     self.index_field(movie.trailer, movie.name)

    def index_movie_by_year(self, movie: Movie):
        """
        Adds a movie to the year index based on its published year.
        """
        if movie.year:
            self.year_index[movie.year].append(movie)

    # Indexing logic for movie type
    def index_movie_type(self, movie):
        self.index_field(movie.type, movie)

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
