# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.alert_event import AlertEvent


class Event9(object):

    """Implementation of the 'Event9' model.

    TODO: type model description here.

    Attributes:
        alert_events (list of AlertEvent): list of occupancy alerts for
            non-compliance zones within the site detected around the same
            time
        for_site (bool): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        site_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site_id": 'site_id',
        "site_name": 'site_name',
        "alert_events": 'alert_events',
        "for_site": 'for_site'
    }

    _optionals = [
        'alert_events',
        'for_site',
    ]

    def __init__(self,
                 site_id=None,
                 site_name=None,
                 alert_events=APIHelper.SKIP,
                 for_site=APIHelper.SKIP):
        """Constructor for the Event9 class"""

        # Initialize members of the class
        if alert_events is not APIHelper.SKIP:
            self.alert_events = alert_events 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        self.site_id = site_id 
        self.site_name = site_name 

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

        site_id = dictionary.get("site_id") if dictionary.get("site_id") else None
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else None
        alert_events = None
        if dictionary.get('alert_events') is not None:
            alert_events = [AlertEvent.from_dictionary(x) for x in dictionary.get('alert_events')]
        else:
            alert_events = APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(site_id,
                   site_name,
                   alert_events,
                   for_site)
