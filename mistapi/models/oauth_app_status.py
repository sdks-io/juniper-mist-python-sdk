# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.account import Account


class OauthAppStatus(object):

    """Implementation of the 'oauth_app_status' model.

    TODO: type model description here.

    Attributes:
        accounts (list of Account): List of linked apps(zoom/teams) account
            details
        authorization_url (string): Only if `forward_url` is set in the
            request
        linked (bool): OAuth application linked status, is mist portal
            authorized with the OAuth appliation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accounts": 'accounts',
        "authorization_url": 'authorization_url',
        "linked": 'linked'
    }

    _optionals = [
        'accounts',
        'authorization_url',
        'linked',
    ]

    def __init__(self,
                 accounts=APIHelper.SKIP,
                 authorization_url=APIHelper.SKIP,
                 linked=APIHelper.SKIP):
        """Constructor for the OauthAppStatus class"""

        # Initialize members of the class
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if authorization_url is not APIHelper.SKIP:
            self.authorization_url = authorization_url 
        if linked is not APIHelper.SKIP:
            self.linked = linked 

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

        accounts = None
        if dictionary.get('accounts') is not None:
            accounts = [Account.from_dictionary(x) for x in dictionary.get('accounts')]
        else:
            accounts = APIHelper.SKIP
        authorization_url = dictionary.get("authorization_url") if dictionary.get("authorization_url") else APIHelper.SKIP
        linked = dictionary.get("linked") if "linked" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(accounts,
                   authorization_url,
                   linked)
