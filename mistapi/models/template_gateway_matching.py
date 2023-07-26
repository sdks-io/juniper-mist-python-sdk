# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.rules_3 import Rules3


class TemplateGatewayMatching(object):

    """Implementation of the 'template_gateway.matching' model.

    Gateway matching

    Attributes:
        enable (bool): TODO: type description here.
        rules (list of Rules3): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable": 'enable',
        "rules": 'rules'
    }

    _optionals = [
        'enable',
        'rules',
    ]

    def __init__(self,
                 enable=APIHelper.SKIP,
                 rules=APIHelper.SKIP):
        """Constructor for the TemplateGatewayMatching class"""

        # Initialize members of the class
        if enable is not APIHelper.SKIP:
            self.enable = enable 
        if rules is not APIHelper.SKIP:
            self.rules = rules 

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

        enable = dictionary.get("enable") if "enable" in dictionary.keys() else APIHelper.SKIP
        rules = None
        if dictionary.get('rules') is not None:
            rules = [Rules3.from_dictionary(x) for x in dictionary.get('rules')]
        else:
            rules = APIHelper.SKIP
        # Return an object of this model
        return cls(enable,
                   rules)
