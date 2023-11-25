"""
This module defines the Person class.
"""

class Person:
    """
    A class used to represent a Person.

    Attributes
    ----------
    _name : str
        a private attribute to hold the name of the Person
    _url : str
        a private attribute to hold the URL of the Person

    Methods
    -------
    name : property
        allows us to get and set the value of _name
    url : property
        allows us to get and set the value of _url
    """

    def __init__(self, data: dict):
        """
        Initialize Person with a name and a URL.

        Parameters
        ----------
            data : dict
                a dictionary containing the person data
        """
        self._name = data.get('name', '')
        self._url = data.get('url', '')

    @property
    def name(self):
        """ Returns the name of the Person """
        return self._name

    @name.setter
    def name(self, value: str):
        """ Updates the name of the Person """
        self._name = value

    @property
    def url(self):
        """ Returns the URL of the Person """
        return self._url

    @url.setter
    def url(self, value: str):
        """ Updates the URL of the Person """
        self._url = value

    def to_dict(self):
        """ Convert the Person object to a dict """
        return {
            '@type': 'Person',
            'name' : self._name,
            'url' : self._url
        }
