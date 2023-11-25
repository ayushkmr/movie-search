"""
This module defines the Organization class.
"""

class Organization:
    """
    A class to represent an Organization with `url`.

    Attributes
    ----------
    _url : str
        a private attribute to store the url of the organization
    _name : str
        a duplicate of _url attribute, for compatibility with classes expecting a 'name'

    Methods
    -------
    url : property
        allows us to get and set the value of _url
    name : property
        allows us to get and set the value of _name
    """

    def __init__(self, data):
        """
        Initialize Organization with url.

        Parameters
        ----------
            data : dict
                a dictionary containing the organization's data
        """
        self._url = data.get('url')
        self._name = self._url

    @property
    def url(self):
        """ Returns the url of the organization """
        return self._url

    @url.setter
    def url(self, value):
        """ Updates the url of the organization """
        self._name = self._url = value

    @property
    def name(self):
        """ Returns the name of the organization """
        return self._name

    @name.setter
    def name(self, value):
        """ Updates the name of the organization """
        self._name = self._url = value

    def to_dict(self):
        """ Returns the dictionary representation of the organization """
        return {
            'url': self._url
        }
