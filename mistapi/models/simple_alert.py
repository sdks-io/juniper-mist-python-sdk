# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.arp_failure import ArpFailure
from mistapi.models.dhcp_failure import DhcpFailure
from mistapi.models.dns_failure import DnsFailure


class SimpleAlert(object):

    """Implementation of the 'simple_alert' model.

    Set of heuristic rules will be enabled when marvis subscription is not
    available.
    It triggers when, in a Z minute window, there are more than Y distinct
    client encountring over X failures

    Attributes:
        arp_failure (ArpFailure): TODO: type description here.
        dhcp_failure (DhcpFailure): TODO: type description here.
        dns_failure (DnsFailure): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "arp_failure": 'arp_failure',
        "dhcp_failure": 'dhcp_failure',
        "dns_failure": 'dns_failure'
    }

    _optionals = [
        'arp_failure',
        'dhcp_failure',
        'dns_failure',
    ]

    def __init__(self,
                 arp_failure=APIHelper.SKIP,
                 dhcp_failure=APIHelper.SKIP,
                 dns_failure=APIHelper.SKIP):
        """Constructor for the SimpleAlert class"""

        # Initialize members of the class
        if arp_failure is not APIHelper.SKIP:
            self.arp_failure = arp_failure 
        if dhcp_failure is not APIHelper.SKIP:
            self.dhcp_failure = dhcp_failure 
        if dns_failure is not APIHelper.SKIP:
            self.dns_failure = dns_failure 

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

        arp_failure = ArpFailure.from_dictionary(dictionary.get('arp_failure')) if 'arp_failure' in dictionary.keys() else APIHelper.SKIP
        dhcp_failure = DhcpFailure.from_dictionary(dictionary.get('dhcp_failure')) if 'dhcp_failure' in dictionary.keys() else APIHelper.SKIP
        dns_failure = DnsFailure.from_dictionary(dictionary.get('dns_failure')) if 'dns_failure' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(arp_failure,
                   dhcp_failure,
                   dns_failure)
