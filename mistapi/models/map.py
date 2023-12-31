# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.latlng_br import LatlngBr
from mistapi.models.latlng_tl import LatlngTl
from mistapi.models.sitesurvey_path import SitesurveyPath
from mistapi.models.wall_path import WallPath
from mistapi.models.wayfinding import Wayfinding
from mistapi.models.wayfinding_path import WayfindingPath


class Map(object):

    """Implementation of the 'map' model.

    Map

    Attributes:
        created_time (float): TODO: type description here.
        flags (object): name/val pair objects for location engine to use
        for_site (bool): TODO: type description here.
        height (float): when type=image, height of the image map
        height_m (float): TODO: type description here.
        id (uuid|string): TODO: type description here.
        latlng_br (LatlngBr): when type=google, latitude / longitude of the
            bottom-right corner
        latlng_tl (LatlngTl): when type=google, latitude / longitude of the
            top-left corner
        locked (bool): whether this map is considered locked down
        modified_time (float): TODO: type description here.
        name (string): The name of the map
        occupancy_limit (int): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        orientation (float): orientation of the map, 0 means up is north, 90
            means up is west
        origin_x (float): the user-annotated x origin, pixels
        origin_y (float): the user-annotated y origin, pixels
        ppm (float): when type=image, pixels per meter
        site_id (uuid|string): TODO: type description here.
        sitesurvey_path (list of SitesurveyPath): sitesurvey_path
        thumbnail_url (string): when type=image, the url for the thumbnail
            image / preview
        mtype (Type30Enum): TODO: type description here.
        url (string): when type=image, the url
        use_auto_orientation (bool): whether this map uses autooreintation
            values or ignores them
        use_auto_placement (bool): whether this map uses autoplacement values
            or ignores them
        view (ViewEnum): when type=google
        wall_path (WallPath): a JSON blob for wall definition (same format as
            wayfinding_path)
        wayfinding (Wayfinding): properties related to wayfinding
        wayfinding_path (WayfindingPath): a JSON blob for wayfinding (using
            Dijkstra’s algorithm)
        width (float): when type=image, width of the image map
        width_m (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time": 'created_time',
        "flags": 'flags',
        "for_site": 'for_site',
        "height": 'height',
        "height_m": 'height_m',
        "id": 'id',
        "latlng_br": 'latlng_br',
        "latlng_tl": 'latlng_tl',
        "locked": 'locked',
        "modified_time": 'modified_time',
        "name": 'name',
        "occupancy_limit": 'occupancy_limit',
        "org_id": 'org_id',
        "orientation": 'orientation',
        "origin_x": 'origin_x',
        "origin_y": 'origin_y',
        "ppm": 'ppm',
        "site_id": 'site_id',
        "sitesurvey_path": 'sitesurvey_path',
        "thumbnail_url": 'thumbnail_url',
        "mtype": 'type',
        "url": 'url',
        "use_auto_orientation": 'use_auto_orientation',
        "use_auto_placement": 'use_auto_placement',
        "view": 'view',
        "wall_path": 'wall_path',
        "wayfinding": 'wayfinding',
        "wayfinding_path": 'wayfinding_path',
        "width": 'width',
        "width_m": 'width_m'
    }

    _optionals = [
        'created_time',
        'flags',
        'for_site',
        'height',
        'height_m',
        'id',
        'latlng_br',
        'latlng_tl',
        'locked',
        'modified_time',
        'name',
        'occupancy_limit',
        'org_id',
        'orientation',
        'origin_x',
        'origin_y',
        'ppm',
        'site_id',
        'sitesurvey_path',
        'thumbnail_url',
        'mtype',
        'url',
        'use_auto_orientation',
        'use_auto_placement',
        'view',
        'wall_path',
        'wayfinding',
        'wayfinding_path',
        'width',
        'width_m',
    ]

    _nullables = [
        'view',
    ]

    def __init__(self,
                 created_time=APIHelper.SKIP,
                 flags=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 height=APIHelper.SKIP,
                 height_m=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 latlng_br=APIHelper.SKIP,
                 latlng_tl=APIHelper.SKIP,
                 locked=False,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 occupancy_limit=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 orientation=0,
                 origin_x=APIHelper.SKIP,
                 origin_y=APIHelper.SKIP,
                 ppm=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 sitesurvey_path=APIHelper.SKIP,
                 thumbnail_url=APIHelper.SKIP,
                 mtype='image',
                 url=APIHelper.SKIP,
                 use_auto_orientation=False,
                 use_auto_placement=False,
                 view=APIHelper.SKIP,
                 wall_path=APIHelper.SKIP,
                 wayfinding=APIHelper.SKIP,
                 wayfinding_path=APIHelper.SKIP,
                 width=APIHelper.SKIP,
                 width_m=APIHelper.SKIP):
        """Constructor for the Map class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if flags is not APIHelper.SKIP:
            self.flags = flags 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if height is not APIHelper.SKIP:
            self.height = height 
        if height_m is not APIHelper.SKIP:
            self.height_m = height_m 
        if id is not APIHelper.SKIP:
            self.id = id 
        if latlng_br is not APIHelper.SKIP:
            self.latlng_br = latlng_br 
        if latlng_tl is not APIHelper.SKIP:
            self.latlng_tl = latlng_tl 
        self.locked = locked 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if occupancy_limit is not APIHelper.SKIP:
            self.occupancy_limit = occupancy_limit 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        self.orientation = orientation 
        if origin_x is not APIHelper.SKIP:
            self.origin_x = origin_x 
        if origin_y is not APIHelper.SKIP:
            self.origin_y = origin_y 
        if ppm is not APIHelper.SKIP:
            self.ppm = ppm 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if sitesurvey_path is not APIHelper.SKIP:
            self.sitesurvey_path = sitesurvey_path 
        if thumbnail_url is not APIHelper.SKIP:
            self.thumbnail_url = thumbnail_url 
        self.mtype = mtype 
        if url is not APIHelper.SKIP:
            self.url = url 
        self.use_auto_orientation = use_auto_orientation 
        self.use_auto_placement = use_auto_placement 
        if view is not APIHelper.SKIP:
            self.view = view 
        if wall_path is not APIHelper.SKIP:
            self.wall_path = wall_path 
        if wayfinding is not APIHelper.SKIP:
            self.wayfinding = wayfinding 
        if wayfinding_path is not APIHelper.SKIP:
            self.wayfinding_path = wayfinding_path 
        if width is not APIHelper.SKIP:
            self.width = width 
        if width_m is not APIHelper.SKIP:
            self.width_m = width_m 

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

        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        flags = dictionary.get("flags") if dictionary.get("flags") else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        height = dictionary.get("height") if dictionary.get("height") else APIHelper.SKIP
        height_m = dictionary.get("height_m") if dictionary.get("height_m") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        latlng_br = LatlngBr.from_dictionary(dictionary.get('latlng_br')) if 'latlng_br' in dictionary.keys() else APIHelper.SKIP
        latlng_tl = LatlngTl.from_dictionary(dictionary.get('latlng_tl')) if 'latlng_tl' in dictionary.keys() else APIHelper.SKIP
        locked = dictionary.get("locked") if dictionary.get("locked") else False
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        occupancy_limit = dictionary.get("occupancy_limit") if dictionary.get("occupancy_limit") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        orientation = dictionary.get("orientation") if dictionary.get("orientation") else 0
        origin_x = dictionary.get("origin_x") if dictionary.get("origin_x") else APIHelper.SKIP
        origin_y = dictionary.get("origin_y") if dictionary.get("origin_y") else APIHelper.SKIP
        ppm = dictionary.get("ppm") if dictionary.get("ppm") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        sitesurvey_path = None
        if dictionary.get('sitesurvey_path') is not None:
            sitesurvey_path = [SitesurveyPath.from_dictionary(x) for x in dictionary.get('sitesurvey_path')]
        else:
            sitesurvey_path = APIHelper.SKIP
        thumbnail_url = dictionary.get("thumbnail_url") if dictionary.get("thumbnail_url") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'image'
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        use_auto_orientation = dictionary.get("use_auto_orientation") if dictionary.get("use_auto_orientation") else False
        use_auto_placement = dictionary.get("use_auto_placement") if dictionary.get("use_auto_placement") else False
        view = dictionary.get("view") if "view" in dictionary.keys() else APIHelper.SKIP
        wall_path = WallPath.from_dictionary(dictionary.get('wall_path')) if 'wall_path' in dictionary.keys() else APIHelper.SKIP
        wayfinding = Wayfinding.from_dictionary(dictionary.get('wayfinding')) if 'wayfinding' in dictionary.keys() else APIHelper.SKIP
        wayfinding_path = WayfindingPath.from_dictionary(dictionary.get('wayfinding_path')) if 'wayfinding_path' in dictionary.keys() else APIHelper.SKIP
        width = dictionary.get("width") if dictionary.get("width") else APIHelper.SKIP
        width_m = dictionary.get("width_m") if dictionary.get("width_m") else APIHelper.SKIP
        # Return an object of this model
        return cls(created_time,
                   flags,
                   for_site,
                   height,
                   height_m,
                   id,
                   latlng_br,
                   latlng_tl,
                   locked,
                   modified_time,
                   name,
                   occupancy_limit,
                   org_id,
                   orientation,
                   origin_x,
                   origin_y,
                   ppm,
                   site_id,
                   sitesurvey_path,
                   thumbnail_url,
                   mtype,
                   url,
                   use_auto_orientation,
                   use_auto_placement,
                   view,
                   wall_path,
                   wayfinding,
                   wayfinding_path,
                   width,
                   width_m)
