# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Cpus(object):

    """Implementation of the 'Cpus' model.

    TODO: type model description here.

    Attributes:
        idle (int): TODO: type description here.
        interrupt (int): TODO: type description here.
        system (int): TODO: type description here.
        usage (int): TODO: type description here.
        user (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "idle": 'idle',
        "interrupt": 'interrupt',
        "system": 'system',
        "usage": 'usage',
        "user": 'user'
    }

    _optionals = [
        'idle',
        'interrupt',
        'system',
        'usage',
        'user',
    ]

    def __init__(self,
                 idle=APIHelper.SKIP,
                 interrupt=APIHelper.SKIP,
                 system=APIHelper.SKIP,
                 usage=APIHelper.SKIP,
                 user=APIHelper.SKIP):
        """Constructor for the Cpus class"""

        # Initialize members of the class
        if idle is not APIHelper.SKIP:
            self.idle = idle 
        if interrupt is not APIHelper.SKIP:
            self.interrupt = interrupt 
        if system is not APIHelper.SKIP:
            self.system = system 
        if usage is not APIHelper.SKIP:
            self.usage = usage 
        if user is not APIHelper.SKIP:
            self.user = user 

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

        idle = dictionary.get("idle") if dictionary.get("idle") else APIHelper.SKIP
        interrupt = dictionary.get("interrupt") if dictionary.get("interrupt") else APIHelper.SKIP
        system = dictionary.get("system") if dictionary.get("system") else APIHelper.SKIP
        usage = dictionary.get("usage") if dictionary.get("usage") else APIHelper.SKIP
        user = dictionary.get("user") if dictionary.get("user") else APIHelper.SKIP
        # Return an object of this model
        return cls(idle,
                   interrupt,
                   system,
                   usage,
                   user)