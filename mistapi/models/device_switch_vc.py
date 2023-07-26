# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.member_1 import Member1


class DeviceSwitchVc(object):

    """Implementation of the 'device_switch_vc' model.

    Virtual Chassis

    Attributes:
        member (int): Only if `op`==`renumber`
        members (list of Member1): TODO: type description here.
        new_member (int): Only if `op`==`renumber`
        op (OpEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "member": 'member',
        "members": 'members',
        "new_member": 'new-member',
        "op": 'op'
    }

    _optionals = [
        'member',
        'members',
        'new_member',
        'op',
    ]

    def __init__(self,
                 member=APIHelper.SKIP,
                 members=APIHelper.SKIP,
                 new_member=APIHelper.SKIP,
                 op=APIHelper.SKIP):
        """Constructor for the DeviceSwitchVc class"""

        # Initialize members of the class
        if member is not APIHelper.SKIP:
            self.member = member 
        if members is not APIHelper.SKIP:
            self.members = members 
        if new_member is not APIHelper.SKIP:
            self.new_member = new_member 
        if op is not APIHelper.SKIP:
            self.op = op 

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

        member = dictionary.get("member") if dictionary.get("member") else APIHelper.SKIP
        members = None
        if dictionary.get('members') is not None:
            members = [Member1.from_dictionary(x) for x in dictionary.get('members')]
        else:
            members = APIHelper.SKIP
        new_member = dictionary.get("new-member") if dictionary.get("new-member") else APIHelper.SKIP
        op = dictionary.get("op") if dictionary.get("op") else APIHelper.SKIP
        # Return an object of this model
        return cls(member,
                   members,
                   new_member,
                   op)
