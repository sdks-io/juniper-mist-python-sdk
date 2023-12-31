# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class TuntermPortConfig(object):

    """Implementation of the 'TuntermPortConfig' model.

    ethernet port configurations

    Attributes:
        downstream_ports (list of string): list of ports to be used for
            downstream (to AP) purpose
        separate_upstream_downstream (bool): weather to separate upstream /
            downstream ports. default is false where all ports will be used.
        upstream_port_vlan_id (int): native VLAN id for upstream ports
        upstream_ports (list of string): list of ports to be used for upstrea
            purpose (to LAN)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "downstream_ports": 'downstream_ports',
        "separate_upstream_downstream": 'separate_upstream_downstream',
        "upstream_port_vlan_id": 'upstream_port_vlan_id',
        "upstream_ports": 'upstream_ports'
    }

    _optionals = [
        'downstream_ports',
        'separate_upstream_downstream',
        'upstream_port_vlan_id',
        'upstream_ports',
    ]

    def __init__(self,
                 downstream_ports=APIHelper.SKIP,
                 separate_upstream_downstream=False,
                 upstream_port_vlan_id=1,
                 upstream_ports=APIHelper.SKIP):
        """Constructor for the TuntermPortConfig class"""

        # Initialize members of the class
        if downstream_ports is not APIHelper.SKIP:
            self.downstream_ports = downstream_ports 
        self.separate_upstream_downstream = separate_upstream_downstream 
        self.upstream_port_vlan_id = upstream_port_vlan_id 
        if upstream_ports is not APIHelper.SKIP:
            self.upstream_ports = upstream_ports 

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

        downstream_ports = dictionary.get("downstream_ports") if dictionary.get("downstream_ports") else APIHelper.SKIP
        separate_upstream_downstream = dictionary.get("separate_upstream_downstream") if dictionary.get("separate_upstream_downstream") else False
        upstream_port_vlan_id = dictionary.get("upstream_port_vlan_id") if dictionary.get("upstream_port_vlan_id") else 1
        upstream_ports = dictionary.get("upstream_ports") if dictionary.get("upstream_ports") else APIHelper.SKIP
        # Return an object of this model
        return cls(downstream_ports,
                   separate_upstream_downstream,
                   upstream_port_vlan_id,
                   upstream_ports)
