# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.intervals import Intervals
from mistapi.models.params import Params
from mistapi.models.report_duration import ReportDuration


class ApiV1ConstInsightMetricsResponse(object):

    """Implementation of the 'Api V1 Const Insight Metrics Response' model.

    TODO: type model description here.

    Attributes:
        ctype (list of string): TODO: type description here.
        description (string): TODO: type description here.
        exampe (list of object): TODO: type description here.
        intervals (dict): Property key is the interval (e.g. 10m, 1h, ...)
        keys (object): TODO: type description here.
        params (dict): Property key is the parameter name
        report_duration (dict): Property key is the duration (e.g. 1d, 1w,
            ...)
        report_scopes (list of string): TODO: type description here.
        scopes (list of Scope1Enum): TODO: type description here.
        sle_baselined (bool): TODO: type description here.
        sle_classifiers (list of string): TODO: type description here.
        mtype (string): TODO: type description here.
        unit (string): TODO: type description here.
        values (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ctype": 'ctype',
        "description": 'description',
        "exampe": 'exampe',
        "intervals": 'intervals',
        "keys": 'keys',
        "params": 'params',
        "report_duration": 'report_duration',
        "report_scopes": 'report_scopes',
        "scopes": 'scopes',
        "sle_baselined": 'sle_baselined',
        "sle_classifiers": 'sle_classifiers',
        "mtype": 'type',
        "unit": 'unit',
        "values": 'values'
    }

    _optionals = [
        'ctype',
        'description',
        'exampe',
        'intervals',
        'keys',
        'params',
        'report_duration',
        'report_scopes',
        'scopes',
        'sle_baselined',
        'sle_classifiers',
        'mtype',
        'unit',
        'values',
    ]

    def __init__(self,
                 ctype=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 exampe=APIHelper.SKIP,
                 intervals=APIHelper.SKIP,
                 keys=APIHelper.SKIP,
                 params=APIHelper.SKIP,
                 report_duration=APIHelper.SKIP,
                 report_scopes=APIHelper.SKIP,
                 scopes=APIHelper.SKIP,
                 sle_baselined=APIHelper.SKIP,
                 sle_classifiers=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 unit=APIHelper.SKIP,
                 values=APIHelper.SKIP):
        """Constructor for the ApiV1ConstInsightMetricsResponse class"""

        # Initialize members of the class
        if ctype is not APIHelper.SKIP:
            self.ctype = ctype 
        if description is not APIHelper.SKIP:
            self.description = description 
        if exampe is not APIHelper.SKIP:
            self.exampe = exampe 
        if intervals is not APIHelper.SKIP:
            self.intervals = intervals 
        if keys is not APIHelper.SKIP:
            self.keys = keys 
        if params is not APIHelper.SKIP:
            self.params = params 
        if report_duration is not APIHelper.SKIP:
            self.report_duration = report_duration 
        if report_scopes is not APIHelper.SKIP:
            self.report_scopes = report_scopes 
        if scopes is not APIHelper.SKIP:
            self.scopes = scopes 
        if sle_baselined is not APIHelper.SKIP:
            self.sle_baselined = sle_baselined 
        if sle_classifiers is not APIHelper.SKIP:
            self.sle_classifiers = sle_classifiers 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if unit is not APIHelper.SKIP:
            self.unit = unit 
        if values is not APIHelper.SKIP:
            self.values = values 

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

        ctype = dictionary.get("ctype") if dictionary.get("ctype") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        exampe = dictionary.get("exampe") if dictionary.get("exampe") else APIHelper.SKIP
        intervals = Intervals.from_dictionary(dictionary.get('intervals')) if 'intervals' in dictionary.keys() else APIHelper.SKIP
        keys = dictionary.get("keys") if dictionary.get("keys") else APIHelper.SKIP
        params = Params.from_dictionary(dictionary.get('params')) if 'params' in dictionary.keys() else APIHelper.SKIP
        report_duration = ReportDuration.from_dictionary(dictionary.get('report_duration')) if 'report_duration' in dictionary.keys() else APIHelper.SKIP
        report_scopes = dictionary.get("report_scopes") if dictionary.get("report_scopes") else APIHelper.SKIP
        scopes = dictionary.get("scopes") if dictionary.get("scopes") else APIHelper.SKIP
        sle_baselined = dictionary.get("sle_baselined") if "sle_baselined" in dictionary.keys() else APIHelper.SKIP
        sle_classifiers = dictionary.get("sle_classifiers") if dictionary.get("sle_classifiers") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        unit = dictionary.get("unit") if dictionary.get("unit") else APIHelper.SKIP
        values = dictionary.get("values") if dictionary.get("values") else APIHelper.SKIP
        # Return an object of this model
        return cls(ctype,
                   description,
                   exampe,
                   intervals,
                   keys,
                   params,
                   report_duration,
                   report_scopes,
                   scopes,
                   sle_baselined,
                   sle_classifiers,
                   mtype,
                   unit,
                   values)