# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Json(object):

    """Implementation of the 'json' model.

    TODO: type model description here.

    Attributes:
        import_all_floorplans (bool): TODO: type description here.
        import_height (bool): TODO: type description here.
        import_orientation (bool): TODO: type description here.
        vendor_name (VendorNameEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vendor_name": 'vendor_name',
        "import_all_floorplans": 'import_all_floorplans',
        "import_height": 'import_height',
        "import_orientation": 'import_orientation'
    }

    _optionals = [
        'import_all_floorplans',
        'import_height',
        'import_orientation',
    ]

    def __init__(self,
                 vendor_name=None,
                 import_all_floorplans=False,
                 import_height=False,
                 import_orientation=False):
        """Constructor for the Json class"""

        # Initialize members of the class
        self.import_all_floorplans = import_all_floorplans 
        self.import_height = import_height 
        self.import_orientation = import_orientation 
        self.vendor_name = vendor_name 

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

        vendor_name = dictionary.get("vendor_name") if dictionary.get("vendor_name") else None
        import_all_floorplans = dictionary.get("import_all_floorplans") if dictionary.get("import_all_floorplans") else False
        import_height = dictionary.get("import_height") if dictionary.get("import_height") else False
        import_orientation = dictionary.get("import_orientation") if dictionary.get("import_orientation") else False
        # Return an object of this model
        return cls(vendor_name,
                   import_all_floorplans,
                   import_height,
                   import_orientation)
