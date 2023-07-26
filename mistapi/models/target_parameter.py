# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class TargetParameter(object):

    """Implementation of the 'TargetParameter' model.

    TODO: type model description here.

    Attributes:
        message_processing_model (MessageProcessingModelEnum): TODO: type
            description here.
        name (string): TODO: type description here.
        notify_filter (string): refer to profile-name in notify-filter
        security_level (SecurityLevelEnum): TODO: type description here.
        security_model (SecurityModelEnum): TODO: type description here.
        security_name (string): refer to security_name in usm

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_processing_model": 'message_processing_model',
        "name": 'name',
        "notify_filter": 'notify_filter',
        "security_level": 'security_level',
        "security_model": 'security_model',
        "security_name": 'security_name'
    }

    _optionals = [
        'message_processing_model',
        'name',
        'notify_filter',
        'security_level',
        'security_model',
        'security_name',
    ]

    def __init__(self,
                 message_processing_model=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 notify_filter=APIHelper.SKIP,
                 security_level=APIHelper.SKIP,
                 security_model=APIHelper.SKIP,
                 security_name=APIHelper.SKIP):
        """Constructor for the TargetParameter class"""

        # Initialize members of the class
        if message_processing_model is not APIHelper.SKIP:
            self.message_processing_model = message_processing_model 
        if name is not APIHelper.SKIP:
            self.name = name 
        if notify_filter is not APIHelper.SKIP:
            self.notify_filter = notify_filter 
        if security_level is not APIHelper.SKIP:
            self.security_level = security_level 
        if security_model is not APIHelper.SKIP:
            self.security_model = security_model 
        if security_name is not APIHelper.SKIP:
            self.security_name = security_name 

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

        message_processing_model = dictionary.get("message_processing_model") if dictionary.get("message_processing_model") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        notify_filter = dictionary.get("notify_filter") if dictionary.get("notify_filter") else APIHelper.SKIP
        security_level = dictionary.get("security_level") if dictionary.get("security_level") else APIHelper.SKIP
        security_model = dictionary.get("security_model") if dictionary.get("security_model") else APIHelper.SKIP
        security_name = dictionary.get("security_name") if dictionary.get("security_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(message_processing_model,
                   name,
                   notify_filter,
                   security_level,
                   security_model,
                   security_name)
