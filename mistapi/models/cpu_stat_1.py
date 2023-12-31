# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class CpuStat1(object):

    """Implementation of the 'CpuStat1' model.

    TODO: type model description here.

    Attributes:
        idle (int): Percentage of CPU time that is idle
        interrupt (int): Percentage of CPU time being used by interrupts
        load_avg (list of object): Load averages for the last 1, 5, and 15
            minutes
        system (int): Percentage of CPU time being used by system processes
        user (int): Percentage of CPU time being used by user processe

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "idle": 'idle',
        "interrupt": 'interrupt',
        "load_avg": 'load_avg',
        "system": 'system',
        "user": 'user'
    }

    _optionals = [
        'idle',
        'interrupt',
        'load_avg',
        'system',
        'user',
    ]

    def __init__(self,
                 idle=APIHelper.SKIP,
                 interrupt=APIHelper.SKIP,
                 load_avg=APIHelper.SKIP,
                 system=APIHelper.SKIP,
                 user=APIHelper.SKIP):
        """Constructor for the CpuStat1 class"""

        # Initialize members of the class
        if idle is not APIHelper.SKIP:
            self.idle = idle 
        if interrupt is not APIHelper.SKIP:
            self.interrupt = interrupt 
        if load_avg is not APIHelper.SKIP:
            self.load_avg = load_avg 
        if system is not APIHelper.SKIP:
            self.system = system 
        if user is not APIHelper.SKIP:
            self.user = user 

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

        idle = dictionary.get("idle") if dictionary.get("idle") else APIHelper.SKIP
        interrupt = dictionary.get("interrupt") if dictionary.get("interrupt") else APIHelper.SKIP
        load_avg = dictionary.get("load_avg") if dictionary.get("load_avg") else APIHelper.SKIP
        system = dictionary.get("system") if dictionary.get("system") else APIHelper.SKIP
        user = dictionary.get("user") if dictionary.get("user") else APIHelper.SKIP
        # Return an object of this model
        return cls(idle,
                   interrupt,
                   load_avg,
                   system,
                   user)
