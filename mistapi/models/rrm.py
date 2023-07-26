# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.rftemplate import Rftemplate
from mistapi.models.rrm_band import RrmBand
from mistapi.models.rrm_band_metric import RrmBandMetric


class Rrm(object):

    """Implementation of the 'rrm' model.

    RRM

    Attributes:
        band_24 (dict): proposal on band 2.4G, key is ap_id, value is the
            proposal
        band_24_metric (RrmBandMetric): TODO: type description here.
        band_5 (dict): proposal on band 5G, key is ap_id, value is the
            proposal
        band_5_metric (RrmBandMetric): TODO: type description here.
        band_6 (dict): proposal on band 6G, key is ap_id, value is the
            proposal
        band_6_metric (RrmBandMetric): TODO: type description here.
        rftemplate (Rftemplate): RF Template
        rftemplate_id (uuid|string): TODO: type description here.
        rftemplate_name (string): TODO: type description here.
        status (Status3Enum): TODO: type description here.
        timestamp (float): time where the status was updated

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band_24": 'band_24',
        "band_24_metric": 'band_24_metric',
        "band_5": 'band_5',
        "band_5_metric": 'band_5_metric',
        "rftemplate": 'rftemplate',
        "rftemplate_id": 'rftemplate_id',
        "rftemplate_name": 'rftemplate_name',
        "status": 'status',
        "timestamp": 'timestamp',
        "band_6": 'band_6',
        "band_6_metric": 'band_6_metric'
    }

    _optionals = [
        'band_6',
        'band_6_metric',
    ]

    def __init__(self,
                 band_24=None,
                 band_24_metric=None,
                 band_5=None,
                 band_5_metric=None,
                 rftemplate=None,
                 rftemplate_id=None,
                 rftemplate_name=None,
                 status=None,
                 timestamp=None,
                 band_6=APIHelper.SKIP,
                 band_6_metric=APIHelper.SKIP):
        """Constructor for the Rrm class"""

        # Initialize members of the class
        self.band_24 = band_24 
        self.band_24_metric = band_24_metric 
        self.band_5 = band_5 
        self.band_5_metric = band_5_metric 
        if band_6 is not APIHelper.SKIP:
            self.band_6 = band_6 
        if band_6_metric is not APIHelper.SKIP:
            self.band_6_metric = band_6_metric 
        self.rftemplate = rftemplate 
        self.rftemplate_id = rftemplate_id 
        self.rftemplate_name = rftemplate_name 
        self.status = status 
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

        band_24 = RrmBand.from_dictionary(dictionary.get('band_24')) if dictionary.get('band_24') else None
        band_24_metric = RrmBandMetric.from_dictionary(dictionary.get('band_24_metric')) if dictionary.get('band_24_metric') else None
        band_5 = RrmBand.from_dictionary(dictionary.get('band_5')) if dictionary.get('band_5') else None
        band_5_metric = RrmBandMetric.from_dictionary(dictionary.get('band_5_metric')) if dictionary.get('band_5_metric') else None
        rftemplate = Rftemplate.from_dictionary(dictionary.get('rftemplate')) if dictionary.get('rftemplate') else None
        rftemplate_id = dictionary.get("rftemplate_id") if dictionary.get("rftemplate_id") else None
        rftemplate_name = dictionary.get("rftemplate_name") if dictionary.get("rftemplate_name") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        band_6 = RrmBand.from_dictionary(dictionary.get('band_6')) if 'band_6' in dictionary.keys() else APIHelper.SKIP
        band_6_metric = RrmBandMetric.from_dictionary(dictionary.get('band_6_metric')) if 'band_6_metric' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(band_24,
                   band_24_metric,
                   band_5,
                   band_5_metric,
                   rftemplate,
                   rftemplate_id,
                   rftemplate_name,
                   status,
                   timestamp,
                   band_6,
                   band_6_metric)