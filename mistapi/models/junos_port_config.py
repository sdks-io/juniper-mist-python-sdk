# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class JunosPortConfig(object):

    """Implementation of the 'junos_port_config' model.

    Switch port config

    Attributes:
        ae_disable_lacp (bool): To disable LACP support for the AE interface
        ae_idx (int): Users could force to use the designated AE name
        aggregated (bool): TODO: type description here.
        critical (bool): if want to generate port up/down alarm
        description (string): TODO: type description here.
        disable_autoneg (bool): if `speed` and `duplex` are specified, whether
            to disable autonegotiation
        duplex (DuplexEnum): TODO: type description here.
        dynamic_usage (string): Enable dynamic usage for this port. Set to
            `dynamic` to enable.
        esilag (bool): TODO: type description here.
        mtu (int): media maximum transmission unit (MTU) is the largest data
            unit that can be forwarded without fragmentation
        no_local_overwrite (bool): prevent helpdesk to override the port
            config
        poe_disabled (bool): TODO: type description here.
        speed (SpeedEnum): TODO: type description here.
        usage (string): port usage name.   If EVPN is used, use
            `evpn_uplink`or `evpn_downlink`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "usage": 'usage',
        "ae_disable_lacp": 'ae_disable_lacp',
        "ae_idx": 'ae_idx',
        "aggregated": 'aggregated',
        "critical": 'critical',
        "description": 'description',
        "disable_autoneg": 'disable_autoneg',
        "duplex": 'duplex',
        "dynamic_usage": 'dynamic_usage',
        "esilag": 'esilag',
        "mtu": 'mtu',
        "no_local_overwrite": 'no_local_overwrite',
        "poe_disabled": 'poe_disabled',
        "speed": 'speed'
    }

    _optionals = [
        'ae_disable_lacp',
        'ae_idx',
        'aggregated',
        'critical',
        'description',
        'disable_autoneg',
        'duplex',
        'dynamic_usage',
        'esilag',
        'mtu',
        'no_local_overwrite',
        'poe_disabled',
        'speed',
    ]

    _nullables = [
        'dynamic_usage',
    ]

    def __init__(self,
                 usage=None,
                 ae_disable_lacp=APIHelper.SKIP,
                 ae_idx=APIHelper.SKIP,
                 aggregated=False,
                 critical=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 disable_autoneg=False,
                 duplex='auto',
                 dynamic_usage=APIHelper.SKIP,
                 esilag=APIHelper.SKIP,
                 mtu=1514,
                 no_local_overwrite=APIHelper.SKIP,
                 poe_disabled=False,
                 speed='auto'):
        """Constructor for the JunosPortConfig class"""

        # Initialize members of the class
        if ae_disable_lacp is not APIHelper.SKIP:
            self.ae_disable_lacp = ae_disable_lacp 
        if ae_idx is not APIHelper.SKIP:
            self.ae_idx = ae_idx 
        self.aggregated = aggregated 
        if critical is not APIHelper.SKIP:
            self.critical = critical 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.disable_autoneg = disable_autoneg 
        self.duplex = duplex 
        if dynamic_usage is not APIHelper.SKIP:
            self.dynamic_usage = dynamic_usage 
        if esilag is not APIHelper.SKIP:
            self.esilag = esilag 
        self.mtu = mtu 
        if no_local_overwrite is not APIHelper.SKIP:
            self.no_local_overwrite = no_local_overwrite 
        self.poe_disabled = poe_disabled 
        self.speed = speed 
        self.usage = usage 

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

        usage = dictionary.get("usage") if dictionary.get("usage") else None
        ae_disable_lacp = dictionary.get("ae_disable_lacp") if "ae_disable_lacp" in dictionary.keys() else APIHelper.SKIP
        ae_idx = dictionary.get("ae_idx") if dictionary.get("ae_idx") else APIHelper.SKIP
        aggregated = dictionary.get("aggregated") if dictionary.get("aggregated") else False
        critical = dictionary.get("critical") if "critical" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        disable_autoneg = dictionary.get("disable_autoneg") if dictionary.get("disable_autoneg") else False
        duplex = dictionary.get("duplex") if dictionary.get("duplex") else 'auto'
        dynamic_usage = dictionary.get("dynamic_usage") if "dynamic_usage" in dictionary.keys() else APIHelper.SKIP
        esilag = dictionary.get("esilag") if "esilag" in dictionary.keys() else APIHelper.SKIP
        mtu = dictionary.get("mtu") if dictionary.get("mtu") else 1514
        no_local_overwrite = dictionary.get("no_local_overwrite") if "no_local_overwrite" in dictionary.keys() else APIHelper.SKIP
        poe_disabled = dictionary.get("poe_disabled") if dictionary.get("poe_disabled") else False
        speed = dictionary.get("speed") if dictionary.get("speed") else 'auto'
        # Return an object of this model
        return cls(usage,
                   ae_disable_lacp,
                   ae_idx,
                   aggregated,
                   critical,
                   description,
                   disable_autoneg,
                   duplex,
                   dynamic_usage,
                   esilag,
                   mtu,
                   no_local_overwrite,
                   poe_disabled,
                   speed)
