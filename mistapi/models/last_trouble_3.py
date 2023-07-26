# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LastTrouble3(object):

    """Implementation of the 'LastTrouble3' model.

    last trouble code of switch

    Attributes:
        code (string): Codes: - 102   No DHCP lease received on any interface
            - 103   No default gateway - 104   Gateway unreachable - 105   No
            DNS server - 106   DNS lookup failed - 108   Agent cannot connect
            to controller - 109   Authentication failed - 110   Underlying
            service (i.e. Netconf/SSH/HTTPS) is down - 113   DNS failure with
            Mist cloud - 114   Empty DNS response with Mist cloud
        timestamp (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "timestamp": 'timestamp'
    }

    def __init__(self,
                 code=None,
                 timestamp=None):
        """Constructor for the LastTrouble3 class"""

        # Initialize members of the class
        self.code = code 
        self.timestamp = timestamp 

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

        code = dictionary.get("code") if dictionary.get("code") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        # Return an object of this model
        return cls(code,
                   timestamp)
