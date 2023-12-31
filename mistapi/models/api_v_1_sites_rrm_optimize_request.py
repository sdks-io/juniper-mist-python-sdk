# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesRrmOptimizeRequest(object):

    """Implementation of the 'Api V1 Sites Rrm Optimize Request' model.

    TODO: type model description here.

    Attributes:
        bands (list of string): list of bands
        macs (list of string): targeting AP (neighbor APs may get changed,
            too), default is empty for ALL APs
        txpower_only (bool): only changng TX Power (will not disconnect
            clients)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bands": 'bands',
        "macs": 'macs',
        "txpower_only": 'txpower_only'
    }

    _optionals = [
        'macs',
        'txpower_only',
    ]

    def __init__(self,
                 bands=None,
                 macs=APIHelper.SKIP,
                 txpower_only=False):
        """Constructor for the ApiV1SitesRrmOptimizeRequest class"""

        # Initialize members of the class
        self.bands = bands 
        if macs is not APIHelper.SKIP:
            self.macs = macs 
        self.txpower_only = txpower_only 

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

        bands = dictionary.get("bands") if dictionary.get("bands") else None
        macs = dictionary.get("macs") if dictionary.get("macs") else APIHelper.SKIP
        txpower_only = dictionary.get("txpower_only") if dictionary.get("txpower_only") else False
        # Return an object of this model
        return cls(bands,
                   macs,
                   txpower_only)
