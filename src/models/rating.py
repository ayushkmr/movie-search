"""
This module defines the Rating class.
"""
class Rating:
    """ 
    A class to represent a Rating

    Attributes
    ----------
    _best_rating : int
        a private attribute to hold the best rating of a movie
    _rating_count : int
        a private attribute to hold the rating count of a movie
    _rating_value : float
        a private attribute to hold the rating value of a movie
    _worst_rating : int
        a private attribute to hold the worst rating value of a movie

    Methods
    -------
    best_rating, rating_count, rating_value, worst_rating : properties
        allow us to get and set the values of corresponding private attributes
    """
    def __init__(self, data):
        """
        Initialize Rating with best rating, rating count, rating value, worst rating

        Parameters
        ----------
            data : dict
                a dictionary containing the rating data
        """
        self._best_rating = data.get('bestRating')
        self._rating_count = data.get('ratingCount')
        self._rating_value = data.get('ratingValue', 0)
        self._worst_rating = data.get('worstRating')

    @property
    def best_rating(self):
        """ Returns the best rating of the movie """
        return self._best_rating

    @best_rating.setter
    def best_rating(self, value):
        """ Updates the best rating of the movie """
        self._best_rating = value

    # Similar getter and setter methods for `rating_count`, `rating_value`, and `worst_rating`...

    def to_dict(self):
        return {
            "bestRating": self._best_rating,
            "ratingCount": self._rating_count,
            "ratingValue": self._rating_value,
            "worstRating": self._worst_rating
        }