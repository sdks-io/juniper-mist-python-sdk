# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
import mistapi.exceptions.api_exception


class ApiV1MspsLicenses403ErrorException(mistapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ApiV1MspsLicenses403ErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ApiV1MspsLicenses403ErrorException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.detail = dictionary.get("detail") if dictionary.get("detail") else None
