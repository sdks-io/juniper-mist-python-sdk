# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesSsrUpgradeRequest(object):

    """Implementation of the 'Api V1 Sites Ssr Upgrade Request' model.

    TODO: type model description here.

    Attributes:
        channel (ChannelEnum): upgrade channel to follow
        reboot_at (int): eboot start time in epoch seconds, default is
            start_time, -1 disables reboot
        start_time (int): 128T firmware download start time in epoch seconds,
            default is now, -1 disables download
        version (string): 128T firmware version to upgrade (e.g. 5.3.0-93)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": 'version',
        "channel": 'channel',
        "reboot_at": 'reboot_at',
        "start_time": 'start_time'
    }

    _optionals = [
        'channel',
        'reboot_at',
        'start_time',
    ]

    def __init__(self,
                 version='stable',
                 channel='stable',
                 reboot_at=APIHelper.SKIP,
                 start_time=APIHelper.SKIP):
        """Constructor for the ApiV1SitesSsrUpgradeRequest class"""

        # Initialize members of the class
        self.channel = channel 
        if reboot_at is not APIHelper.SKIP:
            self.reboot_at = reboot_at 
        if start_time is not APIHelper.SKIP:
            self.start_time = start_time 
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

        version = dictionary.get("version") if dictionary.get("version") else 'stable'
        channel = dictionary.get("channel") if dictionary.get("channel") else 'stable'
        reboot_at = dictionary.get("reboot_at") if dictionary.get("reboot_at") else APIHelper.SKIP
        start_time = dictionary.get("start_time") if dictionary.get("start_time") else APIHelper.SKIP
        # Return an object of this model
        return cls(version,
                   channel,
                   reboot_at,
                   start_time)