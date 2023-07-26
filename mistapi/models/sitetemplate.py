# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.auto_upgrade import AutoUpgrade
from mistapi.models.vars import Vars


class Sitetemplate(object):

    """Implementation of the 'sitetemplate' model.

    TODO: type model description here.

    Attributes:
        auto_upgrade (AutoUpgrade): TODO: type description here.
        name (string): TODO: type description here.
        vars (Vars): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_upgrade": 'auto_upgrade',
        "name": 'name',
        "vars": 'vars'
    }

    _optionals = [
        'auto_upgrade',
        'name',
        'vars',
    ]

    def __init__(self,
                 auto_upgrade=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 vars=APIHelper.SKIP):
        """Constructor for the Sitetemplate class"""

        # Initialize members of the class
        if auto_upgrade is not APIHelper.SKIP:
            self.auto_upgrade = auto_upgrade 
        if name is not APIHelper.SKIP:
            self.name = name 
        if vars is not APIHelper.SKIP:
            self.vars = vars 

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

        auto_upgrade = AutoUpgrade.from_dictionary(dictionary.get('auto_upgrade')) if 'auto_upgrade' in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        vars = Vars.from_dictionary(dictionary.get('vars')) if 'vars' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(auto_upgrade,
                   name,
                   vars)
