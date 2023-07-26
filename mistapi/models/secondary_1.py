# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Secondary1(object):

    """Implementation of the 'Secondary1' model.

    TODO: type model description here.

    Attributes:
        hosts (list of string): TODO: type description here.
        internal_ips (list of string): Only if: * `provider`== `custom-ipsec`
        probe_ips (list of string): TODO: type description here.
        remote_ids (list of string): Only if:  * `provider`== `custom-ipsec`
        wan_names (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hosts": 'hosts',
        "internal_ips": 'internal_ips',
        "probe_ips": 'probe_ips',
        "remote_ids": 'remote_ids',
        "wan_names": 'wan_names'
    }

    _optionals = [
        'hosts',
        'internal_ips',
        'probe_ips',
        'remote_ids',
        'wan_names',
    ]

    def __init__(self,
                 hosts=APIHelper.SKIP,
                 internal_ips=APIHelper.SKIP,
                 probe_ips=APIHelper.SKIP,
                 remote_ids=APIHelper.SKIP,
                 wan_names=APIHelper.SKIP):
        """Constructor for the Secondary1 class"""

        # Initialize members of the class
        if hosts is not APIHelper.SKIP:
            self.hosts = hosts 
        if internal_ips is not APIHelper.SKIP:
            self.internal_ips = internal_ips 
        if probe_ips is not APIHelper.SKIP:
            self.probe_ips = probe_ips 
        if remote_ids is not APIHelper.SKIP:
            self.remote_ids = remote_ids 
        if wan_names is not APIHelper.SKIP:
            self.wan_names = wan_names 

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

        hosts = dictionary.get("hosts") if dictionary.get("hosts") else APIHelper.SKIP
        internal_ips = dictionary.get("internal_ips") if dictionary.get("internal_ips") else APIHelper.SKIP
        probe_ips = dictionary.get("probe_ips") if dictionary.get("probe_ips") else APIHelper.SKIP
        remote_ids = dictionary.get("remote_ids") if dictionary.get("remote_ids") else APIHelper.SKIP
        wan_names = dictionary.get("wan_names") if dictionary.get("wan_names") else APIHelper.SKIP
        # Return an object of this model
        return cls(hosts,
                   internal_ips,
                   probe_ips,
                   remote_ids,
                   wan_names)