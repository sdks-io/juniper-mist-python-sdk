# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.user import User


class Usm(object):

    """Implementation of the 'Usm' model.

    TODO: type model description here.

    Attributes:
        engine_id (string): required only if `engine_type`==`remote_engine`
        engine_type (EngineTypeEnum): TODO: type description here.
        users (list of User): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "engine_id": 'engine-id',
        "engine_type": 'engine_type',
        "users": 'users'
    }

    _optionals = [
        'engine_id',
        'engine_type',
        'users',
    ]

    def __init__(self,
                 engine_id=APIHelper.SKIP,
                 engine_type=APIHelper.SKIP,
                 users=APIHelper.SKIP):
        """Constructor for the Usm class"""

        # Initialize members of the class
        if engine_id is not APIHelper.SKIP:
            self.engine_id = engine_id 
        if engine_type is not APIHelper.SKIP:
            self.engine_type = engine_type 
        if users is not APIHelper.SKIP:
            self.users = users 

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

        engine_id = dictionary.get("engine-id") if dictionary.get("engine-id") else APIHelper.SKIP
        engine_type = dictionary.get("engine_type") if dictionary.get("engine_type") else APIHelper.SKIP
        users = None
        if dictionary.get('users') is not None:
            users = [User.from_dictionary(x) for x in dictionary.get('users')]
        else:
            users = APIHelper.SKIP
        # Return an object of this model
        return cls(engine_id,
                   engine_type,
                   users)
