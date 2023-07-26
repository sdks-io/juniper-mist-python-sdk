# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Archive(object):

    """Implementation of the 'Archive' model.

    TODO: type model description here.

    Attributes:
        files (int): TODO: type description here.
        size (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "files": 'files',
        "size": 'size'
    }

    _optionals = [
        'files',
        'size',
    ]

    def __init__(self,
                 files=APIHelper.SKIP,
                 size=APIHelper.SKIP):
        """Constructor for the Archive class"""

        # Initialize members of the class
        if files is not APIHelper.SKIP:
            self.files = files 
        if size is not APIHelper.SKIP:
            self.size = size 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        files = dictionary.get("files") if dictionary.get("files") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        # Return an object of this model
        return cls(files,
                   size)
