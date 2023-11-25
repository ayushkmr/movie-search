"""
This module defines the Movie class.
"""
from src.models.actor import Actor
from src.models.director import Director
from src.models.organization import Organization
from src.models.genre import Genre
from src.models.rating import Rating
from src.models.datepublished import DatePublished
from src.models.trailer import Trailer
from src.models.person import Person


class Movie:
    """
    A class used to represent a Movie 

    Attributes
    ----------
    _name : str
        a private attribute to hold the name of the Movie
    _actors : list
        a private attribute to store the list of actors in the movie
    _directors : list
        a private attribute to hold the list of directors of the movie
    _creators : list
        a private attribute to hold the list of creators of the movie
    _genres : list
        a private attribute to store the list of genres of the movie
    _keywords : list
        a private attribute to hold the list of keywords for the movie
    _rating : Rating
        a private attribute to hold the rating of the movie
    _content_rating : str
        a private attribute to store the content rating of the movie
    _description : str
        a private attribute to hold the description of the movie
    _duration : str
        a private attribute to store the duration of the movie
    _image : str
        a private attribute to hold the image link of the movie
    _url : str
        a private attribute to store the url of the movie
    _date_published : datetime
        a private attribute to hold the date published of the movie
    _trailer : Trailer
        a private attribute to hold the trailer details of the movie
    _type : str
        a private attribute to store the type of the movie

    Methods
    -------
    name, actors, directors, creators, genres, keywords, rating, 
    content_rating, description, duration, image, url, date_published, 
    trailer, type : properties
        allow us to get and set the values of corresponding private attributes
    """


    def __init__(self, data):
        """
        Initialize Movie with name, actors, directors, creators, genres, 
        keywords, rating, content rating, description, duration, image, url,
        date published, trailer, type

        Parameters
        ----------
            data : dict
                a dictionary containing the movie data
        """
        try:
            self._name = data.get('name', '')
            self._actors = [Actor(actor) for actor in data.get('actor', []) if actor] or []
            self._directors = [Director(director) for director in data.get('director', []) if director] or []
            self._creators = []
            creators_data = data.get('creator', [])
            for creator in creators_data:
                if creator and creator['@type'] == 'Person':
                    self._creators.append(Person(creator))
                elif creator and creator['@type'] == 'Organization':
                    self._creators.append(Organization(creator))
            self._creators = self._creators or []
            self._genres = [Genre(genre) for genre in data.get('genre', []) if genre] or []
            self._keywords = data.get('keywords', '')
            self._rating = Rating(data.get('aggregateRating', {}))
            self._content_rating = data.get('contentRating', '')
            self._description = data.get('description', '')
            self._duration = data.get('duration', '')
            self._image = data.get('image', '')
            self._url = data.get('url', '')
            self._date_published = DatePublished(data.get('datePublished', {}))
            self._trailer = Trailer(data.get('trailer', {}))
            self._type = data.get('@type', '')
            print(f"Movie object initialized. Name: {self._name}")
        except Exception as e:
            print(f"Failed to initialize Movie object.")
            print(f"Input data: {data}")
            print(f"Error: {e}")

    @property
    def name(self):
        """ Returns the name of the movie """
        return self._name

    @property
    def actors(self):
        """ Returns the list of actors in the movie """
        return self._actors

    @property
    def directors(self):
        """ Returns the list of directors of the movie """
        return self._directors

    @property
    def creators(self):
        """ Returns the list of creators of the movie """
        return self._creators

    @property
    def genres(self):
        """ Returns the list of genres of the movie """
        return self._genres

    @property
    def keywords(self):
        """ Returns the keywords of the movie """
        return self._keywords

    @property
    def rating(self):
        """ Returns the rating of the movie """
        return self._rating

    @property
    def content_rating(self):
        """ Returns the content rating of the movie """
        return self._content_rating

    @property
    def description(self):
        """ Returns the description of the movie """
        return self._description

    @property
    def duration(self):
        """ Returns the duration of the movie """
        return self._duration

    @property
    def image(self):
        """ Returns the image of the movie """
        return self._image

    @property
    def url(self):
        """ Returns the url of the movie """
        return self._url

    @property
    def date_published(self):
        """ Returns the date published of the movie """
        return self._date_published

    @property
    def trailer(self):
        """ Returns the trailer of the movie """
        return self._trailer

    @property
    def type(self):
        """ Returns the type of the movie """
        return self._type 

    @name.setter
    def name(self, value):
        """ Updates the name of the movie """
        self._name = value

    # Same getter and setter methods here for `actors`, `directors`, `creators`,
    # `genres`, `keywords`, `rating`, `content_rating`, `description`,
    # `duration`, `image`, `url`, `date_published`, `trailer`, `type`...

    def to_dict(self):
        """ Convert the Movie object to a dict """
        return {
            '@type': self._type,
            'name': self._name,
            'actor': [actor.to_dict() for actor in self._actors],
            'director': [director.to_dict() for director in self._directors],
            'creator': [creator.to_dict() for creator in self._creators],
            'genre': [genre.to_dict() for genre in self._genres],
            'keywords': self._keywords,
            'aggregateRating': self._rating.to_dict(),
            'contentRating': self._content_rating,
            'description': self._description,
            'duration': self._duration,
            'image': self._image,
            'url': self._url,
            'datePublished': self._date_published.to_dict(),
            'trailer': self._trailer.to_dict(),
        }
