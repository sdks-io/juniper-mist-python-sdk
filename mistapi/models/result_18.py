# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result18(object):

    """Implementation of the 'Result18' model.

    TODO: type model description here.

    Attributes:
        ap (string): TODO: type description here.
        auth_method (string): TODO: type description here.
        authorized_expiring_time (float): TODO: type description here.
        authorized_time (float): TODO: type description here.
        company (string): TODO: type description here.
        email (string): TODO: type description here.
        name (string): TODO: type description here.
        ssid (string): TODO: type description here.
        timestamp (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap": 'ap',
        "auth_method": 'auth_method',
        "authorized_expiring_time": 'authorized_expiring_time',
        "authorized_time": 'authorized_time',
        "company": 'company',
        "email": 'email',
        "name": 'name',
        "ssid": 'ssid',
        "timestamp": 'timestamp'
    }

    def __init__(self,
                 ap=None,
                 auth_method=None,
                 authorized_expiring_time=None,
                 authorized_time=None,
                 company=None,
                 email=None,
                 name=None,
                 ssid=None,
                 timestamp=None):
        """Constructor for the Result18 class"""

        # Initialize members of the class
        self.ap = ap 
        self.auth_method = auth_method 
        self.authorized_expiring_time = authorized_expiring_time 
        self.authorized_time = authorized_time 
        self.company = company 
        self.email = email 
        self.name = name 
        self.ssid = ssid 
        self.timestamp = timestamp 

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

        ap = dictionary.get("ap") if dictionary.get("ap") else None
        auth_method = dictionary.get("auth_method") if dictionary.get("auth_method") else None
        authorized_expiring_time = dictionary.get("authorized_expiring_time") if dictionary.get("authorized_expiring_time") else None
        authorized_time = dictionary.get("authorized_time") if dictionary.get("authorized_time") else None
        company = dictionary.get("company") if dictionary.get("company") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        ssid = dictionary.get("ssid") if dictionary.get("ssid") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        # Return an object of this model
        return cls(ap,
                   auth_method,
                   authorized_expiring_time,
                   authorized_time,
                   company,
                   email,
                   name,
                   ssid,
                   timestamp)
