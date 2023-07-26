# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Counts1(object):

    """Implementation of the 'Counts1' model.

    TODO: type model description here.

    Attributes:
        failed (int): TODO: type description here.
        queued (int): TODO: type description here.
        success (int): TODO: type description here.
        upgrading (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failed": 'failed',
        "queued": 'queued',
        "success": 'success',
        "upgrading": 'upgrading'
    }

    def __init__(self,
                 failed=None,
                 queued=None,
                 success=None,
                 upgrading=None):
        """Constructor for the Counts1 class"""

        # Initialize members of the class
        self.failed = failed 
        self.queued = queued 
        self.success = success 
        self.upgrading = upgrading 

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

        failed = dictionary.get("failed") if dictionary.get("failed") else None
        queued = dictionary.get("queued") if dictionary.get("queued") else None
        success = dictionary.get("success") if dictionary.get("success") else None
        upgrading = dictionary.get("upgrading") if dictionary.get("upgrading") else None
        # Return an object of this model
        return cls(failed,
                   queued,
                   success,
                   upgrading)
