# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.fan import Fan
from mistapi.models.pics import Pics
from mistapi.models.poe import Poe
from mistapi.models.psu import Psu
from mistapi.models.temperature import Temperature
from mistapi.models.vc_link import VcLink


class ModuleStat1(object):

    """Implementation of the 'ModuleStat1' model.

    TODO: type model description here.

    Attributes:
        fans (list of Fan): TODO: type description here.
        model (string): TODO: type description here.
        pics (Pics): TODO: type description here.
        poe (Poe): TODO: type description here.
        psus (list of Psu): TODO: type description here.
        serial (string): TODO: type description here.
        temperatures (list of Temperature): TODO: type description here.
        vc_links (list of VcLink): TODO: type description here.
        vc_role (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fans": 'fans',
        "model": 'model',
        "pics": 'pics',
        "poe": 'poe',
        "psus": 'psus',
        "serial": 'serial',
        "temperatures": 'temperatures',
        "vc_links": 'vc_links',
        "vc_role": 'vc_role'
    }

    _optionals = [
        'fans',
        'model',
        'pics',
        'poe',
        'psus',
        'serial',
        'temperatures',
        'vc_links',
        'vc_role',
    ]

    def __init__(self,
                 fans=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 pics=APIHelper.SKIP,
                 poe=APIHelper.SKIP,
                 psus=APIHelper.SKIP,
                 serial=APIHelper.SKIP,
                 temperatures=APIHelper.SKIP,
                 vc_links=APIHelper.SKIP,
                 vc_role=APIHelper.SKIP):
        """Constructor for the ModuleStat1 class"""

        # Initialize members of the class
        if fans is not APIHelper.SKIP:
            self.fans = fans 
        if model is not APIHelper.SKIP:
            self.model = model 
        if pics is not APIHelper.SKIP:
            self.pics = pics 
        if poe is not APIHelper.SKIP:
            self.poe = poe 
        if psus is not APIHelper.SKIP:
            self.psus = psus 
        if serial is not APIHelper.SKIP:
            self.serial = serial 
        if temperatures is not APIHelper.SKIP:
            self.temperatures = temperatures 
        if vc_links is not APIHelper.SKIP:
            self.vc_links = vc_links 
        if vc_role is not APIHelper.SKIP:
            self.vc_role = vc_role 

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

        fans = None
        if dictionary.get('fans') is not None:
            fans = [Fan.from_dictionary(x) for x in dictionary.get('fans')]
        else:
            fans = APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        pics = Pics.from_dictionary(dictionary.get('pics')) if 'pics' in dictionary.keys() else APIHelper.SKIP
        poe = Poe.from_dictionary(dictionary.get('poe')) if 'poe' in dictionary.keys() else APIHelper.SKIP
        psus = None
        if dictionary.get('psus') is not None:
            psus = [Psu.from_dictionary(x) for x in dictionary.get('psus')]
        else:
            psus = APIHelper.SKIP
        serial = dictionary.get("serial") if dictionary.get("serial") else APIHelper.SKIP
        temperatures = None
        if dictionary.get('temperatures') is not None:
            temperatures = [Temperature.from_dictionary(x) for x in dictionary.get('temperatures')]
        else:
            temperatures = APIHelper.SKIP
        vc_links = None
        if dictionary.get('vc_links') is not None:
            vc_links = [VcLink.from_dictionary(x) for x in dictionary.get('vc_links')]
        else:
            vc_links = APIHelper.SKIP
        vc_role = dictionary.get("vc_role") if dictionary.get("vc_role") else APIHelper.SKIP
        # Return an object of this model
        return cls(fans,
                   model,
                   pics,
                   poe,
                   psus,
                   serial,
                   temperatures,
                   vc_links,
                   vc_role)
