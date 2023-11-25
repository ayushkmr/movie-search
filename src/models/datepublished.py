"""
This module defines the DatePublished class.
"""
from datetime import datetime

class DatePublished:
    """ 
    A class to represent a DatePublished with `date` property

    Attributes
    ----------
    _date : datetime
        a private attribute to hold the date published

    Methods
    -------
    date : property
        allows us to get and set the value of _date
    """
    def __init__(self, date_string):
        """
        Initialize DatePublished with date

        Parameters
        ----------
            date_string : str
                the date published in 'YYYY-MM-DD' format
        """
        self._date = datetime.strptime(date_string, '%Y-%m-%d')

    @property
    def date(self):
        """ Returns the date published """
        return self._date

    @date.setter
    def date(self, value):
        """ Updates the date published """
        self._date = value

    def to_dict(self):
        return self._date.isoformat()  # convert datetime object to ISO 8601 string representation