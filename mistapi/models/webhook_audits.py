# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.event_2 import Event2


class WebhookAudits(object):

    """Implementation of the 'webhook_audits' model.

    audit webhook

    Attributes:
        events (list of Event2): TODO: type description here.
        topic (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "events": 'events',
        "topic": 'topic'
    }

    def __init__(self,
                 events=None,
                 topic='audits'):
        """Constructor for the WebhookAudits class"""

        # Initialize members of the class
        self.events = events 
        self.topic = topic 

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

        events = None
        if dictionary.get('events') is not None:
            events = [Event2.from_dictionary(x) for x in dictionary.get('events')]
        topic = dictionary.get("topic") if dictionary.get("topic") else 'audits'
        # Return an object of this model
        return cls(events,
                   topic)
