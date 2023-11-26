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
        self._name = self.clean_url(self._url)

    @staticmethod
    def clean_url(url: str) -> str:
        """
        Cleans up a URL by removing leading '/company/' and trailing '/'.

        Args:
            url (str): A URL string to be cleaned.

        Returns:
            str: A cleaned URL string.
        """
        if not url: 
            return url
        url = url.replace('/company/', '')
        return url.rstrip('/')

    @property
    def url(self):
        """ Returns the url of the organization """
        return self._url

    @url.setter
    def url(self, value):
        """ Updates the url of the organization and also updates the name accordingly """
        self._url = value
        self._name = self.clean_url(value)

    @property
    def name(self):
        """ Returns the name (cleaned url) of the organization """
        return self._name

    @name.setter
    def name(self, value):
        """ Raises an exception as name is the cleaned version of URL and shouldn't be manually set """
        raise Exception("Can't set name directly. It's derived from URL.")

    def to_dict(self):
        """ Returns the dictionary representation of the organization """
        return {
            'url': self._url
        }
