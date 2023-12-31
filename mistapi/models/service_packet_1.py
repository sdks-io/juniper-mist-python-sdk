# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ServicePacket1(object):

    """Implementation of the 'ServicePacket1' model.

    TODO: type model description here.

    Attributes:
        service_data (string): TODO: type description here.
        service_uuid (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_data": 'service_data',
        "service_uuid": 'service_uuid'
    }

    _optionals = [
        'service_data',
        'service_uuid',
    ]

    def __init__(self,
                 service_data=APIHelper.SKIP,
                 service_uuid=APIHelper.SKIP):
        """Constructor for the ServicePacket1 class"""

        # Initialize members of the class
        if service_data is not APIHelper.SKIP:
            self.service_data = service_data 
        if service_uuid is not APIHelper.SKIP:
            self.service_uuid = service_uuid 

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

        service_data = dictionary.get("service_data") if dictionary.get("service_data") else APIHelper.SKIP
        service_uuid = dictionary.get("service_uuid") if dictionary.get("service_uuid") else APIHelper.SKIP
        # Return an object of this model
        return cls(service_data,
                   service_uuid)
