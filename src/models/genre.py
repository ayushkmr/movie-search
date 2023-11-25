"""
This module defines the Genre class.
"""
class Genre:
    """ 
    A class to represent a Genre with `name` property

    Attributes
    ----------
    _name : str
        a private attribute to hold the name of the Genre

    Methods
    -------
    name : property
        allows us to get and set the value of _name
    """
    def __init__(self, data):
        """
        Initialize Genre with name

        Parameters
        ----------
            data : str
                the name of the genre
        """
        self._name = data

    @property
    def name(self):
        """ Returns the name of the genre """
        return self._name

    @name.setter
    def name(self, value):
        """ Updates the name of the genre """
        self._name = value

    def to_dict(self):
        return self._name  # directly return string as it doesn't have nested objects