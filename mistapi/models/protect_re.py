# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.custom import Custom


class ProtectRe(object):

    """Implementation of the 'ProtectRe' model.

    restrict inbound-traffic to host
    when enabled, all traffic that is not essential to our operation will be
    dropped 
    e.g. ntp / dns / traffic to mist will be allowed by default, if dhcpd is
    enabled, we'll make sure it works

    Attributes:
        allowed_services (list of string): optionally, services we'll allow
        custom (list of Custom): TODO: type description here.
        enabled (bool): TODO: type description here.
        trusted_hosts (list of string): optionally, host/subnets we'll allow
            traffic to/from

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allowed_services": 'allowed_services',
        "custom": 'custom',
        "enabled": 'enabled',
        "trusted_hosts": 'trusted_hosts'
    }

    _optionals = [
        'allowed_services',
        'custom',
        'enabled',
        'trusted_hosts',
    ]

    def __init__(self,
                 allowed_services=APIHelper.SKIP,
                 custom=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 trusted_hosts=APIHelper.SKIP):
        """Constructor for the ProtectRe class"""

        # Initialize members of the class
        if allowed_services is not APIHelper.SKIP:
            self.allowed_services = allowed_services 
        if custom is not APIHelper.SKIP:
            self.custom = custom 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if trusted_hosts is not APIHelper.SKIP:
            self.trusted_hosts = trusted_hosts 

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

        allowed_services = dictionary.get("allowed_services") if dictionary.get("allowed_services") else APIHelper.SKIP
        custom = None
        if dictionary.get('custom') is not None:
            custom = [Custom.from_dictionary(x) for x in dictionary.get('custom')]
        else:
            custom = APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        trusted_hosts = dictionary.get("trusted_hosts") if dictionary.get("trusted_hosts") else APIHelper.SKIP
        # Return an object of this model
        return cls(allowed_services,
                   custom,
                   enabled,
                   trusted_hosts)
