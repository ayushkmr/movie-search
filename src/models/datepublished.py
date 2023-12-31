"""
This module defines the DatePublished class.
"""

from datetime import datetime


class DatePublished:
    """ 
    A class to represent a DatePublished

    Attributes
    ----------
    _date : datetime.date
        a private attribute to hold the date published
    _year : int
        a private attribute to hold the year of date published

    Methods
    -------
    date : property
        allows us to get and set the value of _date
    year : property
        allows us to get and set the value of _year
    parse_date(date_str: str): datetime.date
        parses the date string into a datetime.date object
    to_dict() : str
        serializes the date object to an ISO 8601 string representation
    """

    def __init__(self, date_string: str):
        """
        Initialize DatePublished with date

        Parameters
        ----------
            date_string : str
                the date published in 'YYYY-MM-DD' or 'YYYY' format
        """
        if date_string:
            self._date = self.parse_date(date_string).date()  # convert datetime to date
            self._year = self._date.year
        else:
            self._date = None
            self._year = None

    @property
    def date(self):
        """ Returns the date published as a date object """
        return self._date

    @property
    def year(self):
        """ Returns the year of date published """
        return self._year

    def parse_date(self, date_str: str):
        """Parse a date string in YYYY-MM-DD or YYYY format."""
        # Define the possible date formats
        formats = ['%Y-%m-%d', '%Y']
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                pass
        raise ValueError(f"No known format found for date: {date_str}")

    def to_dict(self):
        return self._date.isoformat() if self._date else None  # convert datetime.date object to ISO 8601 string representation