# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.aps import Aps
from mistapi.models.gateways import Gateways
from mistapi.models.switches import Switches


class Capture(object):

    """Implementation of the 'capture' model.

    TODO: type model description here.

    Attributes:
        ap_mac (string): filter by ap_mac
        client_mac (string): client mac, required if `type`==`client`;
            optional otherwise
        duration (int): duration of the capture, in seconds
        includes_mcast (bool): TODO: type description here.
        max_pkt_len (int): max_len of each packet to capture
        num_packets (int): number of packets to capture, 0 for unlimited,
            default is 1024 for client-capture
        ssid (string): optional filter by ssid
        mtype (Type7Enum): client
        format (FormatEnum): pcap format
        tcpdump_expression (string): tcpdump expression
        band (Band1Enum): only used for radiotap
        wlan_id (uuid|string): WLAN ID
        radiotap_tcpdump_expression (string): tcpdump expression for radiotap
            interface (802.11 + radio headers)
        wired_tcpdump_expression (string): tcpdump expression for wired
        wireless_tcpdump_expression (string): tcpdump expression for radiotap
            interface (802.11)
        gateways (dict): List of SSRs. Property key is the SSR MAC
        aps (dict): TODO: type description here.
        channel (string): specify the channel value where scan PCAP has to be
            started
        width (string): specify the bandwidth value with respect to the
            channel.
        switches (dict): Property key is the switch mac

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap_mac": 'ap_mac',
        "client_mac": 'client_mac',
        "duration": 'duration',
        "includes_mcast": 'includes_mcast',
        "max_pkt_len": 'max_pkt_len',
        "num_packets": 'num_packets',
        "ssid": 'ssid',
        "mtype": 'type',
        "format": 'format',
        "tcpdump_expression": 'tcpdump_expression',
        "band": 'band',
        "wlan_id": 'wlan_id',
        "radiotap_tcpdump_expression": 'radiotap_tcpdump_expression',
        "wired_tcpdump_expression": 'wired_tcpdump_expression',
        "wireless_tcpdump_expression": 'wireless_tcpdump_expression',
        "gateways": 'gateways',
        "aps": 'aps',
        "channel": 'channel',
        "width": 'width',
        "switches": 'switches'
    }

    _optionals = [
        'ap_mac',
        'client_mac',
        'duration',
        'includes_mcast',
        'max_pkt_len',
        'num_packets',
        'ssid',
        'mtype',
        'format',
        'tcpdump_expression',
        'band',
        'wlan_id',
        'radiotap_tcpdump_expression',
        'wired_tcpdump_expression',
        'wireless_tcpdump_expression',
        'gateways',
        'aps',
        'channel',
        'width',
        'switches',
    ]

    _nullables = [
        'ap_mac',
        'client_mac',
        'ssid',
    ]

    def __init__(self,
                 ap_mac=APIHelper.SKIP,
                 client_mac=APIHelper.SKIP,
                 duration=600,
                 includes_mcast=APIHelper.SKIP,
                 max_pkt_len=128,
                 num_packets=1024,
                 ssid=APIHelper.SKIP,
                 mtype='client',
                 format='pcap',
                 tcpdump_expression=APIHelper.SKIP,
                 band='24',
                 wlan_id=APIHelper.SKIP,
                 radiotap_tcpdump_expression=APIHelper.SKIP,
                 wired_tcpdump_expression=APIHelper.SKIP,
                 wireless_tcpdump_expression=APIHelper.SKIP,
                 gateways=APIHelper.SKIP,
                 aps=APIHelper.SKIP,
                 channel=APIHelper.SKIP,
                 width=APIHelper.SKIP,
                 switches=APIHelper.SKIP):
        """Constructor for the Capture class"""

        # Initialize members of the class
        if ap_mac is not APIHelper.SKIP:
            self.ap_mac = ap_mac 
        if client_mac is not APIHelper.SKIP:
            self.client_mac = client_mac 
        self.duration = duration 
        if includes_mcast is not APIHelper.SKIP:
            self.includes_mcast = includes_mcast 
        self.max_pkt_len = max_pkt_len 
        self.num_packets = num_packets 
        if ssid is not APIHelper.SKIP:
            self.ssid = ssid 
        self.mtype = mtype 
        self.format = format 
        if tcpdump_expression is not APIHelper.SKIP:
            self.tcpdump_expression = tcpdump_expression 
        self.band = band 
        if wlan_id is not APIHelper.SKIP:
            self.wlan_id = wlan_id 
        if radiotap_tcpdump_expression is not APIHelper.SKIP:
            self.radiotap_tcpdump_expression = radiotap_tcpdump_expression 
        if wired_tcpdump_expression is not APIHelper.SKIP:
            self.wired_tcpdump_expression = wired_tcpdump_expression 
        if wireless_tcpdump_expression is not APIHelper.SKIP:
            self.wireless_tcpdump_expression = wireless_tcpdump_expression 
        if gateways is not APIHelper.SKIP:
            self.gateways = gateways 
        if aps is not APIHelper.SKIP:
            self.aps = aps 
        if channel is not APIHelper.SKIP:
            self.channel = channel 
        if width is not APIHelper.SKIP:
            self.width = width 
        if switches is not APIHelper.SKIP:
            self.switches = switches 

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

        ap_mac = dictionary.get("ap_mac") if "ap_mac" in dictionary.keys() else APIHelper.SKIP
        client_mac = dictionary.get("client_mac") if "client_mac" in dictionary.keys() else APIHelper.SKIP
        duration = dictionary.get("duration") if dictionary.get("duration") else 600
        includes_mcast = dictionary.get("includes_mcast") if "includes_mcast" in dictionary.keys() else APIHelper.SKIP
        max_pkt_len = dictionary.get("max_pkt_len") if dictionary.get("max_pkt_len") else 128
        num_packets = dictionary.get("num_packets") if dictionary.get("num_packets") else 1024
        ssid = dictionary.get("ssid") if "ssid" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'client'
        format = dictionary.get("format") if dictionary.get("format") else 'pcap'
        tcpdump_expression = dictionary.get("tcpdump_expression") if dictionary.get("tcpdump_expression") else APIHelper.SKIP
        band = dictionary.get("band") if dictionary.get("band") else '24'
        wlan_id = dictionary.get("wlan_id") if dictionary.get("wlan_id") else APIHelper.SKIP
        radiotap_tcpdump_expression = dictionary.get("radiotap_tcpdump_expression") if dictionary.get("radiotap_tcpdump_expression") else APIHelper.SKIP
        wired_tcpdump_expression = dictionary.get("wired_tcpdump_expression") if dictionary.get("wired_tcpdump_expression") else APIHelper.SKIP
        wireless_tcpdump_expression = dictionary.get("wireless_tcpdump_expression") if dictionary.get("wireless_tcpdump_expression") else APIHelper.SKIP
        gateways = Gateways.from_dictionary(dictionary.get('gateways')) if 'gateways' in dictionary.keys() else APIHelper.SKIP
        aps = Aps.from_dictionary(dictionary.get('aps')) if 'aps' in dictionary.keys() else APIHelper.SKIP
        channel = dictionary.get("channel") if dictionary.get("channel") else APIHelper.SKIP
        width = dictionary.get("width") if dictionary.get("width") else APIHelper.SKIP
        switches = Switches.from_dictionary(dictionary.get('switches')) if 'switches' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(ap_mac,
                   client_mac,
                   duration,
                   includes_mcast,
                   max_pkt_len,
                   num_packets,
                   ssid,
                   mtype,
                   format,
                   tcpdump_expression,
                   band,
                   wlan_id,
                   radiotap_tcpdump_expression,
                   wired_tcpdump_expression,
                   wireless_tcpdump_expression,
                   gateways,
                   aps,
                   channel,
                   width,
                   switches)
