# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class JunosIpConfigGateway(object):

    """Implementation of the 'junos_ip_config_gateway' model.

    Junos IP Config

    Attributes:
        dns (list of string): except for out-of-band interface (vme/em0/fxp0)
        dns_suffix (list of string): except for out-of-band interface
            (vme/em0/fxp0)
        gateway (string): except for out-of-band interface (vme/em0/fxp0)
        ip (string): TODO: type description here.
        netmask (string): used only if `subnet` is not specified in
            `networks`
        network (string): optional, the network to be used for mgmt
        poser_password (string): if `type`==`pppoe`
        ppoe_username (string): if `type`==`pppoe`
        pppoe_auth (PppoeAuthEnum): if `type`==`pppoe`
        mtype (Type14Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns": 'dns',
        "dns_suffix": 'dns_suffix',
        "gateway": 'gateway',
        "ip": 'ip',
        "netmask": 'netmask',
        "network": 'network',
        "poser_password": 'poser_password',
        "ppoe_username": 'ppoe_username',
        "pppoe_auth": 'pppoe_auth',
        "mtype": 'type'
    }

    _optionals = [
        'dns',
        'dns_suffix',
        'gateway',
        'ip',
        'netmask',
        'network',
        'poser_password',
        'ppoe_username',
        'pppoe_auth',
        'mtype',
    ]

    def __init__(self,
                 dns=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 gateway=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 netmask=APIHelper.SKIP,
                 network=APIHelper.SKIP,
                 poser_password=APIHelper.SKIP,
                 ppoe_username=APIHelper.SKIP,
                 pppoe_auth='none',
                 mtype='dhcp'):
        """Constructor for the JunosIpConfigGateway class"""

        # Initialize members of the class
        if dns is not APIHelper.SKIP:
            self.dns = dns 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if netmask is not APIHelper.SKIP:
            self.netmask = netmask 
        if network is not APIHelper.SKIP:
            self.network = network 
        if poser_password is not APIHelper.SKIP:
            self.poser_password = poser_password 
        if ppoe_username is not APIHelper.SKIP:
            self.ppoe_username = ppoe_username 
        self.pppoe_auth = pppoe_auth 
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

        dns = dictionary.get("dns") if dictionary.get("dns") else APIHelper.SKIP
        dns_suffix = dictionary.get("dns_suffix") if dictionary.get("dns_suffix") else APIHelper.SKIP
        gateway = dictionary.get("gateway") if dictionary.get("gateway") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        netmask = dictionary.get("netmask") if dictionary.get("netmask") else APIHelper.SKIP
        network = dictionary.get("network") if dictionary.get("network") else APIHelper.SKIP
        poser_password = dictionary.get("poser_password") if dictionary.get("poser_password") else APIHelper.SKIP
        ppoe_username = dictionary.get("ppoe_username") if dictionary.get("ppoe_username") else APIHelper.SKIP
        pppoe_auth = dictionary.get("pppoe_auth") if dictionary.get("pppoe_auth") else 'none'
        mtype = dictionary.get("type") if dictionary.get("type") else 'dhcp'
        # Return an object of this model
        return cls(dns,
                   dns_suffix,
                   gateway,
                   ip,
                   netmask,
                   network,
                   poser_password,
                   ppoe_username,
                   pppoe_auth,
                   mtype)
