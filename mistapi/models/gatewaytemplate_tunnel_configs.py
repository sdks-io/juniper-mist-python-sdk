# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.auto_provision import AutoProvision
from mistapi.models.ike_proposal import IkeProposal
from mistapi.models.ipsec_proposal import IpsecProposal
from mistapi.models.primary_1 import Primary1
from mistapi.models.probe import Probe
from mistapi.models.secondary_1 import Secondary1


class GatewaytemplateTunnelConfigs(object):

    """Implementation of the 'gatewaytemplate_tunnel_configs' model.

    TODO: type model description here.

    Attributes:
        auto_provision (AutoProvision): TODO: type description here.
        ike_lifetime (int): Only if: * `provider`== `custom-ipsec`
        ike_mode (IkeModeEnum): Only if: * `provider`== `custom-ipsec`
        ike_proposals (list of IkeProposal): if `provider`== `custom-ipsec`
        ipsec_lifetime (int): if `provider`== `custom-ipsec`
        ipsec_proposals (list of IpsecProposal): Only if: * `provider`==
            `custom-ipsec`
        local_id (string): Only if: * `provider`== `zscaler-ipsec` *
            `provider`==`jse-ipsec` * `provider`== `custom-ipsec`
        mode (ModeEnum): TODO: type description here.
        primary (Primary1): TODO: type description here.
        probe (Probe): Only if: * `provider`== `custom-ipsec`
        protocol (Protocol1Enum): Only if: * `provider`== `custom-ipsec`
        provider (ProviderEnum): TODO: type description here.
        psk (string): Only if: * `provider`== `zscaler-ipsec` *
            `provider`==`jse-ipsec` * `provider`== `custom-ipsec`
        secondary (Secondary1): TODO: type description here.
        version (VersionEnum): Only if: * `provider`== `custom-gre`  *
            `provider`== `custom-ipsec`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_provision": 'auto_provision',
        "ike_lifetime": 'ike_lifetime',
        "ike_mode": 'ike_mode',
        "ike_proposals": 'ike_proposals',
        "ipsec_lifetime": 'ipsec_lifetime',
        "ipsec_proposals": 'ipsec_proposals',
        "local_id": 'local_id',
        "mode": 'mode',
        "primary": 'primary',
        "probe": 'probe',
        "protocol": 'protocol',
        "provider": 'provider',
        "psk": 'psk',
        "secondary": 'secondary',
        "version": 'version'
    }

    _optionals = [
        'auto_provision',
        'ike_lifetime',
        'ike_mode',
        'ike_proposals',
        'ipsec_lifetime',
        'ipsec_proposals',
        'local_id',
        'mode',
        'primary',
        'probe',
        'protocol',
        'provider',
        'psk',
        'secondary',
        'version',
    ]

    def __init__(self,
                 auto_provision=APIHelper.SKIP,
                 ike_lifetime=APIHelper.SKIP,
                 ike_mode='main',
                 ike_proposals=APIHelper.SKIP,
                 ipsec_lifetime=APIHelper.SKIP,
                 ipsec_proposals=APIHelper.SKIP,
                 local_id=APIHelper.SKIP,
                 mode='active-standby',
                 primary=APIHelper.SKIP,
                 probe=APIHelper.SKIP,
                 protocol=APIHelper.SKIP,
                 provider=APIHelper.SKIP,
                 psk=APIHelper.SKIP,
                 secondary=APIHelper.SKIP,
                 version='2'):
        """Constructor for the GatewaytemplateTunnelConfigs class"""

        # Initialize members of the class
        if auto_provision is not APIHelper.SKIP:
            self.auto_provision = auto_provision 
        if ike_lifetime is not APIHelper.SKIP:
            self.ike_lifetime = ike_lifetime 
        self.ike_mode = ike_mode 
        if ike_proposals is not APIHelper.SKIP:
            self.ike_proposals = ike_proposals 
        if ipsec_lifetime is not APIHelper.SKIP:
            self.ipsec_lifetime = ipsec_lifetime 
        if ipsec_proposals is not APIHelper.SKIP:
            self.ipsec_proposals = ipsec_proposals 
        if local_id is not APIHelper.SKIP:
            self.local_id = local_id 
        self.mode = mode 
        if primary is not APIHelper.SKIP:
            self.primary = primary 
        if probe is not APIHelper.SKIP:
            self.probe = probe 
        if protocol is not APIHelper.SKIP:
            self.protocol = protocol 
        if provider is not APIHelper.SKIP:
            self.provider = provider 
        if psk is not APIHelper.SKIP:
            self.psk = psk 
        if secondary is not APIHelper.SKIP:
            self.secondary = secondary 
        self.version = version 

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

        auto_provision = AutoProvision.from_dictionary(dictionary.get('auto_provision')) if 'auto_provision' in dictionary.keys() else APIHelper.SKIP
        ike_lifetime = dictionary.get("ike_lifetime") if dictionary.get("ike_lifetime") else APIHelper.SKIP
        ike_mode = dictionary.get("ike_mode") if dictionary.get("ike_mode") else 'main'
        ike_proposals = None
        if dictionary.get('ike_proposals') is not None:
            ike_proposals = [IkeProposal.from_dictionary(x) for x in dictionary.get('ike_proposals')]
        else:
            ike_proposals = APIHelper.SKIP
        ipsec_lifetime = dictionary.get("ipsec_lifetime") if dictionary.get("ipsec_lifetime") else APIHelper.SKIP
        ipsec_proposals = None
        if dictionary.get('ipsec_proposals') is not None:
            ipsec_proposals = [IpsecProposal.from_dictionary(x) for x in dictionary.get('ipsec_proposals')]
        else:
            ipsec_proposals = APIHelper.SKIP
        local_id = dictionary.get("local_id") if dictionary.get("local_id") else APIHelper.SKIP
        mode = dictionary.get("mode") if dictionary.get("mode") else 'active-standby'
        primary = Primary1.from_dictionary(dictionary.get('primary')) if 'primary' in dictionary.keys() else APIHelper.SKIP
        probe = Probe.from_dictionary(dictionary.get('probe')) if 'probe' in dictionary.keys() else APIHelper.SKIP
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else APIHelper.SKIP
        provider = dictionary.get("provider") if dictionary.get("provider") else APIHelper.SKIP
        psk = dictionary.get("psk") if dictionary.get("psk") else APIHelper.SKIP
        secondary = Secondary1.from_dictionary(dictionary.get('secondary')) if 'secondary' in dictionary.keys() else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else '2'
        # Return an object of this model
        return cls(auto_provision,
                   ike_lifetime,
                   ike_mode,
                   ike_proposals,
                   ipsec_lifetime,
                   ipsec_proposals,
                   local_id,
                   mode,
                   primary,
                   probe,
                   protocol,
                   provider,
                   psk,
                   secondary,
                   version)