# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Paths(object):

    """Implementation of the 'Paths' model.

    TODO: type model description here.

    Attributes:
        cost (int): TODO: type description here.
        gateway_ip (string): if `type`==`local`, if a different gateway is
            desired
        internet_access (bool): when `type`==`vpn`, if this vpn path can be
            used for internet
        name (string): TODO: type description here.
        networks (list of string): if `type`==`local`
        target_ips (list of string): if `type`==`local`, if destination IP is
            to be replaced
        mtype (Type19Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cost": 'cost',
        "gateway_ip": 'gateway_ip',
        "internet_access": 'internet_access',
        "name": 'name',
        "networks": 'networks',
        "target_ips": 'target_ips',
        "mtype": 'type'
    }

    _optionals = [
        'cost',
        'gateway_ip',
        'internet_access',
        'name',
        'networks',
        'target_ips',
        'mtype',
    ]

    def __init__(self,
                 cost=APIHelper.SKIP,
                 gateway_ip=APIHelper.SKIP,
                 internet_access=False,
                 name=APIHelper.SKIP,
                 networks=APIHelper.SKIP,
                 target_ips=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the Paths class"""

        # Initialize members of the class
        if cost is not APIHelper.SKIP:
            self.cost = cost 
        if gateway_ip is not APIHelper.SKIP:
            self.gateway_ip = gateway_ip 
        self.internet_access = internet_access 
        if name is not APIHelper.SKIP:
            self.name = name 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        if target_ips is not APIHelper.SKIP:
            self.target_ips = target_ips 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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

        cost = dictionary.get("cost") if dictionary.get("cost") else APIHelper.SKIP
        gateway_ip = dictionary.get("gateway_ip") if dictionary.get("gateway_ip") else APIHelper.SKIP
        internet_access = dictionary.get("internet_access") if dictionary.get("internet_access") else False
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        networks = dictionary.get("networks") if dictionary.get("networks") else APIHelper.SKIP
        target_ips = dictionary.get("target_ips") if dictionary.get("target_ips") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(cost,
                   gateway_ip,
                   internet_access,
                   name,
                   networks,
                   target_ips,
                   mtype)