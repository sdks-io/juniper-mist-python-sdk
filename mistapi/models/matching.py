# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Matching(object):

    """Implementation of the 'Matching' model.

    TODO: type model description here.

    Attributes:
        attack_name (list of string): TODO: type description here.
        dst_subnet (list of string): TODO: type description here.
        severity (list of SeverityEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attack_name": 'attack_name',
        "dst_subnet": 'dst_subnet',
        "severity": 'severity'
    }

    _optionals = [
        'attack_name',
        'dst_subnet',
        'severity',
    ]

    def __init__(self,
                 attack_name=APIHelper.SKIP,
                 dst_subnet=APIHelper.SKIP,
                 severity=APIHelper.SKIP):
        """Constructor for the Matching class"""

        # Initialize members of the class
        if attack_name is not APIHelper.SKIP:
            self.attack_name = attack_name 
        if dst_subnet is not APIHelper.SKIP:
            self.dst_subnet = dst_subnet 
        if severity is not APIHelper.SKIP:
            self.severity = severity 

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

        attack_name = dictionary.get("attack_name") if dictionary.get("attack_name") else APIHelper.SKIP
        dst_subnet = dictionary.get("dst_subnet") if dictionary.get("dst_subnet") else APIHelper.SKIP
        severity = dictionary.get("severity") if dictionary.get("severity") else APIHelper.SKIP
        # Return an object of this model
        return cls(attack_name,
                   dst_subnet,
                   severity)