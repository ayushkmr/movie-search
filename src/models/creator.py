"""
This module defines the Creator class which could be a Person or Organization.
"""
from src.models.person import Person
from src.models.organization import Organization


class Creator:
    """
    A class to represent a Creator which could be either a Person or an Organization.

    Attributes
    ----------
    _creator : Person or Organization
        the actual creator which is either a Person or an Organization

    Methods
    -------
    creator : property
        Allows us to get the _creator
    name: property
        Allows us to get the name/url of the _creator
    """

    def __init__(self, data: dict):
        """
        Initialize Creator which could be either a Person or an Organization.

        Parameters
        ----------
        data : dict
            a dictionary containing the creator's data
        """
        if data.get('@type') == 'Person':
            self._creator = Person(data)
        elif data.get('@type') == 'Organization':
            self._creator = Organization(data)

    @property
    def creator(self):
        """ Returns the creator """
        return self._creator

    @property
    def name(self):
        """ Returns the name of the creator if it is a Person or url if it is an Organization """
        return self._creator.name

    def to_dict(self):
        """ Returns the dictionary representation of the creator """
        return self._creator.to_dict()