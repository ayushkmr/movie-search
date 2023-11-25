"""
This module defines the Trailer class.
"""
class Trailer:
    """ 
    A class used to represent a Trailer 

    Attributes
    ----------
    _description : str
        a private attribute to hold the description of the trailer
    _embed_url : str
        a private attribute to store the embed URL of the trailer
    _name : str
        a private attribute to hold the name of the trailer
    _thumbnail_url : str
        a private attribute to store the thumbnail URL of the trailer
    _type : str
        a private attribute to hold the type of the trailer
    _upload_date : str
        a private attribute to hold the upload date of the trailer

    Methods
    -------
    description, embed_url, name, thumbnail_url, type, upload_date : properties
        allow us to get and set the values of corresponding private attributes
    """
    def __init__(self, data):
        """
        Initialize Trailer with description, embed url, name, thumbnail url, type, upload date

        Parameters
        ----------
            data : dict
                a dictionary containing the trailer data
        """
        self._description = data.get('description')
        self._embed_url = data.get('embedUrl')
        self._name = data.get('name')
        self._thumbnail_url = data.get('thumbnailUrl')
        self._type = data.get('@type')
        self._upload_date = data.get('uploadDate')

    @property
    def description(self):
        """ Returns the description of the trailer """
        return self._description

    @description.setter
    def description(self, value):
        """ Updates the description of the trailer """
        self._description = value

    # Similar getter and setter methods for `embed_url`, `name`, `thumbnail_url`, `type`, and `upload_date`...

    def to_dict(self):
        return {
            'description': self._description,
            'embedUrl': self._embed_url,
            'name': self._name,
            'thumbnailUrl': self._thumbnail_url,
            '@type': self._type,
            'uploadDate': self._upload_date
        }