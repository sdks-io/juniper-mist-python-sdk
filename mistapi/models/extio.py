# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Extio(object):

    """Implementation of the 'Extio' model.

    TODO: type model description here.

    Attributes:
        default_dir (DefaultDirEnum): TODO: type description here.
        input (bool): TODO: type description here.
        output (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_dir": 'default_dir',
        "input": 'input',
        "output": 'output'
    }

    _optionals = [
        'default_dir',
        'input',
        'output',
    ]

    def __init__(self,
                 default_dir=APIHelper.SKIP,
                 input=APIHelper.SKIP,
                 output=APIHelper.SKIP):
        """Constructor for the Extio class"""

        # Initialize members of the class
        if default_dir is not APIHelper.SKIP:
            self.default_dir = default_dir 
        if input is not APIHelper.SKIP:
            self.input = input 
        if output is not APIHelper.SKIP:
            self.output = output 

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

        default_dir = dictionary.get("default_dir") if dictionary.get("default_dir") else APIHelper.SKIP
        input = dictionary.get("input") if "input" in dictionary.keys() else APIHelper.SKIP
        output = dictionary.get("output") if "output" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(default_dir,
                   input,
                   output)
