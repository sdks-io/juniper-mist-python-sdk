# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.dmvpn import Dmvpn
from mistapi.models.ipsec_1 import Ipsec1
from mistapi.models.sessions_2 import Sessions2


class WxlanTunnel(object):

    """Implementation of the 'wxlan_tunnel' model.

    WxLAn Tunnel

    Attributes:
        created_time (float): TODO: type description here.
        dmvpn (Dmvpn): Dynamic Multipoint VPN configurations
        for_mgmt (bool): determined during creation time and cannot be
            toggled. A management tunnel cannot be used by wxlan rule or by
            wlan
        for_site (bool): TODO: type description here.
        hello_interval (int): in seconds, used as heartbeat to detect if a
            tunnel is alive. AP will try another peer after missing N hellos
            specified by hello_retries.
        hello_retries (int): TODO: type description here.
        hostname (string): optional, overwrite the hostname in SCCRQ control
            message, default is “” or null, %H and %M can be used, which will
            be replace with corresponding values: * %H: name of the ap if
            provided (and will be stripped so it can be used for hostname) and
            fallbacks to MAC * %M: MAC (e.g. 5c5b350e0060)
        id (uuid|string): TODO: type description here.
        ipsec (Ipsec1): IPSec-related configurations; requires DMVPN be
            enabled
        is_static (bool): whether it’s static/unmanaged (i.e. no control
            session). As the session configurations are not compatible, cannot
            be toggled.
        modified_time (float): TODO: type description here.
        mtu (int): 0 to enable PMTU, 552-1500 to start PMTU with a lower MTU
        name (string): The name of the tunnel
        org_id (uuid|string): TODO: type description here.
        peers (list of string): list of remote peers’ IP or hostname
        router_id (string): optional, overwrite the router-id in SCCRQ control
            message, default is “0” or null, can also be an IPv4 address
        secret (string): secret, ‘’ if no auth is used
        sessions (list of Sessions2): sessions to be established with the
            tunnel. Has to be >= 1 in order for this tunnel to be useful. For
            management tunnel, it can only have 1
        site_id (uuid|string): TODO: type description here.
        udp_port (int): udp port if `use_udp`==`true`
        use_udp (bool): whether to use UDP instead of IP (proto=115, which is
            default of L2TPv3)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_time": 'created_time',
        "dmvpn": 'dmvpn',
        "for_mgmt": 'for_mgmt',
        "for_site": 'for_site',
        "hello_interval": 'hello_interval',
        "hello_retries": 'hello_retries',
        "hostname": 'hostname',
        "id": 'id',
        "ipsec": 'ipsec',
        "is_static": 'is_static',
        "modified_time": 'modified_time',
        "mtu": 'mtu',
        "org_id": 'org_id',
        "peers": 'peers',
        "router_id": 'router_id',
        "secret": 'secret',
        "sessions": 'sessions',
        "site_id": 'site_id',
        "udp_port": 'udp_port',
        "use_udp": 'use_udp'
    }

    _optionals = [
        'created_time',
        'dmvpn',
        'for_mgmt',
        'for_site',
        'hello_interval',
        'hello_retries',
        'hostname',
        'id',
        'ipsec',
        'is_static',
        'modified_time',
        'mtu',
        'org_id',
        'peers',
        'router_id',
        'secret',
        'sessions',
        'site_id',
        'udp_port',
        'use_udp',
    ]

    def __init__(self,
                 name=None,
                 created_time=APIHelper.SKIP,
                 dmvpn=APIHelper.SKIP,
                 for_mgmt=False,
                 for_site=APIHelper.SKIP,
                 hello_interval=60,
                 hello_retries=7,
                 hostname=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 ipsec=APIHelper.SKIP,
                 is_static=False,
                 modified_time=APIHelper.SKIP,
                 mtu=0,
                 org_id=APIHelper.SKIP,
                 peers=APIHelper.SKIP,
                 router_id=APIHelper.SKIP,
                 secret=APIHelper.SKIP,
                 sessions=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 udp_port=APIHelper.SKIP,
                 use_udp=False):
        """Constructor for the WxlanTunnel class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if dmvpn is not APIHelper.SKIP:
            self.dmvpn = dmvpn 
        self.for_mgmt = for_mgmt 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        self.hello_interval = hello_interval 
        self.hello_retries = hello_retries 
        if hostname is not APIHelper.SKIP:
            self.hostname = hostname 
        if id is not APIHelper.SKIP:
            self.id = id 
        if ipsec is not APIHelper.SKIP:
            self.ipsec = ipsec 
        self.is_static = is_static 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        self.mtu = mtu 
        self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if peers is not APIHelper.SKIP:
            self.peers = peers 
        if router_id is not APIHelper.SKIP:
            self.router_id = router_id 
        if secret is not APIHelper.SKIP:
            self.secret = secret 
        if sessions is not APIHelper.SKIP:
            self.sessions = sessions 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if udp_port is not APIHelper.SKIP:
            self.udp_port = udp_port 
        self.use_udp = use_udp 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        dmvpn = Dmvpn.from_dictionary(dictionary.get('dmvpn')) if 'dmvpn' in dictionary.keys() else APIHelper.SKIP
        for_mgmt = dictionary.get("for_mgmt") if dictionary.get("for_mgmt") else False
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        hello_interval = dictionary.get("hello_interval") if dictionary.get("hello_interval") else 60
        hello_retries = dictionary.get("hello_retries") if dictionary.get("hello_retries") else 7
        hostname = dictionary.get("hostname") if dictionary.get("hostname") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        ipsec = Ipsec1.from_dictionary(dictionary.get('ipsec')) if 'ipsec' in dictionary.keys() else APIHelper.SKIP
        is_static = dictionary.get("is_static") if dictionary.get("is_static") else False
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        mtu = dictionary.get("mtu") if dictionary.get("mtu") else 0
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        peers = dictionary.get("peers") if dictionary.get("peers") else APIHelper.SKIP
        router_id = dictionary.get("router_id") if dictionary.get("router_id") else APIHelper.SKIP
        secret = dictionary.get("secret") if dictionary.get("secret") else APIHelper.SKIP
        sessions = None
        if dictionary.get('sessions') is not None:
            sessions = [Sessions2.from_dictionary(x) for x in dictionary.get('sessions')]
        else:
            sessions = APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        udp_port = dictionary.get("udp_port") if dictionary.get("udp_port") else APIHelper.SKIP
        use_udp = dictionary.get("use_udp") if dictionary.get("use_udp") else False
        # Return an object of this model
        return cls(name,
                   created_time,
                   dmvpn,
                   for_mgmt,
                   for_site,
                   hello_interval,
                   hello_retries,
                   hostname,
                   id,
                   ipsec,
                   is_static,
                   modified_time,
                   mtu,
                   org_id,
                   peers,
                   router_id,
                   secret,
                   sessions,
                   site_id,
                   udp_port,
                   use_udp)
