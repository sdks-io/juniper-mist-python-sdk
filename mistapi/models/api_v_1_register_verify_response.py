# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1RegisterVerifyResponse(object):

    """Implementation of the 'Api V1 Register Verify Response' model.

    TODO: type model description here.

    Attributes:
        detail (string): TODO: type description here.
        invite_not_applied (bool): TODO: type description here.
        min_length (int): TODO: type description here.
        return_to (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "detail": 'detail',
        "invite_not_applied": 'invite_not_applied',
        "min_length": 'min_length',
        "return_to": 'return_to'
    }

    _optionals = [
        'detail',
        'invite_not_applied',
        'min_length',
        'return_to',
    ]

    def __init__(self,
                 detail=APIHelper.SKIP,
                 invite_not_applied=APIHelper.SKIP,
                 min_length=APIHelper.SKIP,
                 return_to=APIHelper.SKIP):
        """Constructor for the ApiV1RegisterVerifyResponse class"""

        # Initialize members of the class
        if detail is not APIHelper.SKIP:
            self.detail = detail 
        if invite_not_applied is not APIHelper.SKIP:
            self.invite_not_applied = invite_not_applied 
        if min_length is not APIHelper.SKIP:
            self.min_length = min_length 
        if return_to is not APIHelper.SKIP:
            self.return_to = return_to 

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

        detail = dictionary.get("detail") if dictionary.get("detail") else APIHelper.SKIP
        invite_not_applied = dictionary.get("invite_not_applied") if "invite_not_applied" in dictionary.keys() else APIHelper.SKIP
        min_length = dictionary.get("min_length") if dictionary.get("min_length") else APIHelper.SKIP
        return_to = dictionary.get("return_to") if dictionary.get("return_to") else APIHelper.SKIP
        # Return an object of this model
        return cls(detail,
                   invite_not_applied,
                   min_length,
                   return_to)