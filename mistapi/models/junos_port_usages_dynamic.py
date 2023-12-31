# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.rules_2 import Rules2


class JunosPortUsagesDynamic(object):

    """Implementation of the 'junos_port_usages_dynamic' model.

    This is a special mode where the actually usage is determined by a set of
    rules the port will start with `access` mode and isolated depending on the
    rules, if resolved, the port will have the resolved usage applied.

    Attributes:
        mode (string): TODO: type description here.
        reset_default_when (ResetDefaultWhenEnum): Control when the DPC port
            should be changed to the default port usage Configuring to none
            will let the DPC port keep at the current port usage.
        rules (list of Rules2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode": 'mode',
        "reset_default_when": 'reset_default_when',
        "rules": 'rules'
    }

    _optionals = [
        'reset_default_when',
        'rules',
    ]

    def __init__(self,
                 reset_default_when='link_down',
                 rules=APIHelper.SKIP):
        """Constructor for the JunosPortUsagesDynamic class"""

        # Initialize members of the class
        self.mode = 'dynamic' 
        self.reset_default_when = reset_default_when 
        if rules is not APIHelper.SKIP:
            self.rules = rules 

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

        reset_default_when = dictionary.get("reset_default_when") if dictionary.get("reset_default_when") else 'link_down'
        rules = None
        if dictionary.get('rules') is not None:
            rules = [Rules2.from_dictionary(x) for x in dictionary.get('rules')]
        else:
            rules = APIHelper.SKIP
        # Return an object of this model
        return cls(reset_default_when,
                   rules)
