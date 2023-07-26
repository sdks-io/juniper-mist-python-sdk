# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class SwitchMgmt1(object):

    """Implementation of the 'SwitchMgmt1' model.

    TODO: type model description here.

    Attributes:
        ap_affinity_threshold (string): TODO: type description here.
        config_revert_timer (int): TODO: type description here.
        dhcp_option_fqdn (bool): Enable to provide the FQDN with DHCP option
            81
        mxedge_proxy_host (string): TODO: type description here.
        mxedge_proxy_port (int): TODO: type description here.
        use_mxedge_proxy (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap_affinity_threshold": 'ap_affinity_threshold',
        "config_revert_timer": 'config_revert_timer',
        "dhcp_option_fqdn": 'dhcp_option_fqdn',
        "mxedge_proxy_host": 'mxedge_proxy_host',
        "mxedge_proxy_port": 'mxedge_proxy_port',
        "use_mxedge_proxy": 'use_mxedge_proxy'
    }

    _optionals = [
        'ap_affinity_threshold',
        'config_revert_timer',
        'dhcp_option_fqdn',
        'mxedge_proxy_host',
        'mxedge_proxy_port',
        'use_mxedge_proxy',
    ]

    def __init__(self,
                 ap_affinity_threshold=APIHelper.SKIP,
                 config_revert_timer=10,
                 dhcp_option_fqdn=False,
                 mxedge_proxy_host=APIHelper.SKIP,
                 mxedge_proxy_port=2222,
                 use_mxedge_proxy=False):
        """Constructor for the SwitchMgmt1 class"""

        # Initialize members of the class
        if ap_affinity_threshold is not APIHelper.SKIP:
            self.ap_affinity_threshold = ap_affinity_threshold 
        self.config_revert_timer = config_revert_timer 
        self.dhcp_option_fqdn = dhcp_option_fqdn 
        if mxedge_proxy_host is not APIHelper.SKIP:
            self.mxedge_proxy_host = mxedge_proxy_host 
        self.mxedge_proxy_port = mxedge_proxy_port 
        self.use_mxedge_proxy = use_mxedge_proxy 

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

        ap_affinity_threshold = dictionary.get("ap_affinity_threshold") if dictionary.get("ap_affinity_threshold") else APIHelper.SKIP
        config_revert_timer = dictionary.get("config_revert_timer") if dictionary.get("config_revert_timer") else 10
        dhcp_option_fqdn = dictionary.get("dhcp_option_fqdn") if dictionary.get("dhcp_option_fqdn") else False
        mxedge_proxy_host = dictionary.get("mxedge_proxy_host") if dictionary.get("mxedge_proxy_host") else APIHelper.SKIP
        mxedge_proxy_port = dictionary.get("mxedge_proxy_port") if dictionary.get("mxedge_proxy_port") else 2222
        use_mxedge_proxy = dictionary.get("use_mxedge_proxy") if dictionary.get("use_mxedge_proxy") else False
        # Return an object of this model
        return cls(ap_affinity_threshold,
                   config_revert_timer,
                   dhcp_option_fqdn,
                   mxedge_proxy_host,
                   mxedge_proxy_port,
                   use_mxedge_proxy)
