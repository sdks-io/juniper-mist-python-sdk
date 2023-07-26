# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.action import Action


class JunosAclPolicies(object):

    """Implementation of the 'junos_acl_policies' model.

    - for GBP-based policy, all src_tags and dst_tags have to be gbp-based
    - for ACL-based policy, `network` is required in either the source or
    destination so that we know where to attach the policy to

    Attributes:
        actions (list of Action): - for GBP-based policy, all src_tags and
            dst_tags have to be gbp-based - for ACL-based policy, `network` is
            required in either the source or destination so that we know where
            to attach the policy to
        name (string): TODO: type description here.
        src_tags (list of string): - for GBP-based policy, all src_tags and
            dst_tags have to be gbp-based - for ACL-based policy, `network` is
            required in either the source or destination so that we know where
            to attach the policy to

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "actions": 'actions',
        "name": 'name',
        "src_tags": 'src_tags'
    }

    _optionals = [
        'actions',
        'name',
        'src_tags',
    ]

    def __init__(self,
                 actions=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 src_tags=APIHelper.SKIP):
        """Constructor for the JunosAclPolicies class"""

        # Initialize members of the class
        if actions is not APIHelper.SKIP:
            self.actions = actions 
        if name is not APIHelper.SKIP:
            self.name = name 
        if src_tags is not APIHelper.SKIP:
            self.src_tags = src_tags 

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

        actions = None
        if dictionary.get('actions') is not None:
            actions = [Action.from_dictionary(x) for x in dictionary.get('actions')]
        else:
            actions = APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        src_tags = dictionary.get("src_tags") if dictionary.get("src_tags") else APIHelper.SKIP
        # Return an object of this model
        return cls(actions,
                   name,
                   src_tags)