# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.app_probing import AppProbing


class GatewayMgmt(object):

    """Implementation of the 'GatewayMgmt' model.

    TODO: type model description here.

    Attributes:
        app_probing (AppProbing): TODO: type description here.
        app_usage (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_probing": 'app_probing',
        "app_usage": 'app_usage'
    }

    _optionals = [
        'app_probing',
        'app_usage',
    ]

    def __init__(self,
                 app_probing=APIHelper.SKIP,
                 app_usage=APIHelper.SKIP):
        """Constructor for the GatewayMgmt class"""

        # Initialize members of the class
        if app_probing is not APIHelper.SKIP:
            self.app_probing = app_probing 
        if app_usage is not APIHelper.SKIP:
            self.app_usage = app_usage 

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

        app_probing = AppProbing.from_dictionary(dictionary.get('app_probing')) if 'app_probing' in dictionary.keys() else APIHelper.SKIP
        app_usage = dictionary.get("app_usage") if "app_usage" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(app_probing,
                   app_usage)
