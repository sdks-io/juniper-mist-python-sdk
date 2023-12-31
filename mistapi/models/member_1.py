# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Member1(object):

    """Implementation of the 'Member1' model.

    TODO: type model description here.

    Attributes:
        mac (string): same as the mac of device_id. Required if `op`==`add`
        member (int): Required if `op`==`remove`. Optional if `op`==`add`
        vc_ports (list of string): Optional. Only if `op`==`add`
        vc_role (VcRole1Enum): Optional. Only if `op`==`add`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac',
        "member": 'member',
        "vc_ports": 'vc_ports',
        "vc_role": 'vc_role'
    }

    _optionals = [
        'mac',
        'member',
        'vc_ports',
        'vc_role',
    ]

    def __init__(self,
                 mac=APIHelper.SKIP,
                 member=APIHelper.SKIP,
                 vc_ports=APIHelper.SKIP,
                 vc_role=APIHelper.SKIP):
        """Constructor for the Member1 class"""

        # Initialize members of the class
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if member is not APIHelper.SKIP:
            self.member = member 
        if vc_ports is not APIHelper.SKIP:
            self.vc_ports = vc_ports 
        if vc_role is not APIHelper.SKIP:
            self.vc_role = vc_role 

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

        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        member = dictionary.get("member") if dictionary.get("member") else APIHelper.SKIP
        vc_ports = dictionary.get("vc_ports") if dictionary.get("vc_ports") else APIHelper.SKIP
        vc_role = dictionary.get("vc_role") if dictionary.get("vc_role") else APIHelper.SKIP
        # Return an object of this model
        return cls(mac,
                   member,
                   vc_ports,
                   vc_role)
