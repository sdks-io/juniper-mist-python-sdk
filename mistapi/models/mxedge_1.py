# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.mxcluster_radsec import MxclusterRadsec
from mistapi.models.mxedge_das import MxedgeDas


class Mxedge1(object):

    """Implementation of the 'Mxedge1' model.

    site mist edges form a cluster of radsecproxy servers

    Attributes:
        mist_das (MxedgeDas): configure cloud-assisted dynamic authorization
            service on this cluster of mist edges
        radsec (MxclusterRadsec): MxEdge Radsec Configuration

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mist_das": 'mist_das',
        "radsec": 'radsec'
    }

    _optionals = [
        'mist_das',
        'radsec',
    ]

    def __init__(self,
                 mist_das=APIHelper.SKIP,
                 radsec=APIHelper.SKIP):
        """Constructor for the Mxedge1 class"""

        # Initialize members of the class
        if mist_das is not APIHelper.SKIP:
            self.mist_das = mist_das 
        if radsec is not APIHelper.SKIP:
            self.radsec = radsec 

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

        mist_das = MxedgeDas.from_dictionary(dictionary.get('mist_das')) if 'mist_das' in dictionary.keys() else APIHelper.SKIP
        radsec = MxclusterRadsec.from_dictionary(dictionary.get('radsec')) if 'radsec' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mist_das,
                   radsec)
