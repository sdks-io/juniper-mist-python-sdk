# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Attachment(object):

    """Implementation of the 'Attachment' model.

    TODO: type model description here.

    Attributes:
        content_type (string): TODO: type description here.
        content_url (string): TODO: type description here.
        size (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content_type": 'content_type',
        "content_url": 'content_url',
        "size": 'size'
    }

    _optionals = [
        'content_type',
        'content_url',
        'size',
    ]

    def __init__(self,
                 content_type=APIHelper.SKIP,
                 content_url=APIHelper.SKIP,
                 size=APIHelper.SKIP):
        """Constructor for the Attachment class"""

        # Initialize members of the class
        if content_type is not APIHelper.SKIP:
            self.content_type = content_type 
        if content_url is not APIHelper.SKIP:
            self.content_url = content_url 
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

        content_type = dictionary.get("content_type") if dictionary.get("content_type") else APIHelper.SKIP
        content_url = dictionary.get("content_url") if dictionary.get("content_url") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        # Return an object of this model
        return cls(content_type,
                   content_url,
                   size)