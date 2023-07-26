# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DwellTagNames(object):

    """Implementation of the 'DwellTagNames' model.

    TODO: type model description here.

    Attributes:
        bounce (string): TODO: type description here.
        engaged (string): TODO: type description here.
        passerby (string): TODO: type description here.
        stationed (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bounce": 'bounce',
        "engaged": 'engaged',
        "passerby": 'passerby',
        "stationed": 'stationed'
    }

    def __init__(self,
                 bounce=None,
                 engaged=None,
                 passerby=None,
                 stationed=None):
        """Constructor for the DwellTagNames class"""

        # Initialize members of the class
        self.bounce = bounce 
        self.engaged = engaged 
        self.passerby = passerby 
        self.stationed = stationed 

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

        bounce = dictionary.get("bounce") if dictionary.get("bounce") else None
        engaged = dictionary.get("engaged") if dictionary.get("engaged") else None
        passerby = dictionary.get("passerby") if dictionary.get("passerby") else None
        stationed = dictionary.get("stationed") if dictionary.get("stationed") else None
        # Return an object of this model
        return cls(bounce,
                   engaged,
                   passerby,
                   stationed)