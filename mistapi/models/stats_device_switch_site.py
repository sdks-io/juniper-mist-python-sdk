# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.client_1 import Client1
from mistapi.models.cpu_stat_1 import CpuStat1
from mistapi.models.if_stat import IfStat
from mistapi.models.ip_stat_2 import IpStat2
from mistapi.models.last_trouble_1 import LastTrouble1
from mistapi.models.memory_stat_1 import MemoryStat1
from mistapi.models.module_stat_1 import ModuleStat1
from mistapi.models.num_clients import NumClients


class StatsDeviceSwitchSite(object):

    """Implementation of the 'stats_device_switch_site' model.

    Switch statistics

    Attributes:
        clients (list of Client1): TODO: type description here.
        cpu_stat (CpuStat1): TODO: type description here.
        hostname (string): hostname reported by the device
        if_stat (dict): Property key is the interface name
        ip (string): TODO: type description here.
        ip_stat (IpStat2): TODO: type description here.
        last_seen (float): TODO: type description here.
        last_trouble (LastTrouble1): last trouble code of switch
        mac (string): TODO: type description here.
        memory_stat (MemoryStat1): memory usage stat (for virtual chassis,
            memory usage of master RE)
        model (string): TODO: type description here.
        module_stat (list of ModuleStat1): TODO: type description here.
        name (string): device name if configured
        num_clients (NumClients): TODO: type description here.
        serial (string): TODO: type description here.
        status (string): TODO: type description here.
        mtype (string): TODO: type description here.
        uptime (float): TODO: type description here.
        version (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "clients": 'clients',
        "cpu_stat": 'cpu_stat',
        "hostname": 'hostname',
        "if_stat": 'if_stat',
        "ip": 'ip',
        "ip_stat": 'ip_stat',
        "last_seen": 'last_seen',
        "last_trouble": 'last_trouble',
        "mac": 'mac',
        "memory_stat": 'memory_stat',
        "model": 'model',
        "module_stat": 'module_stat',
        "name": 'name',
        "num_clients": 'num_clients',
        "serial": 'serial',
        "status": 'status',
        "mtype": 'type',
        "uptime": 'uptime',
        "version": 'version'
    }

    _optionals = [
        'clients',
        'cpu_stat',
        'hostname',
        'if_stat',
        'ip',
        'ip_stat',
        'last_seen',
        'last_trouble',
        'mac',
        'memory_stat',
        'model',
        'module_stat',
        'name',
        'num_clients',
        'serial',
        'status',
        'mtype',
        'uptime',
        'version',
    ]

    def __init__(self,
                 clients=APIHelper.SKIP,
                 cpu_stat=APIHelper.SKIP,
                 hostname=APIHelper.SKIP,
                 if_stat=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 ip_stat=APIHelper.SKIP,
                 last_seen=APIHelper.SKIP,
                 last_trouble=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 memory_stat=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 module_stat=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 num_clients=APIHelper.SKIP,
                 serial=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 uptime=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the StatsDeviceSwitchSite class"""

        # Initialize members of the class
        if clients is not APIHelper.SKIP:
            self.clients = clients 
        if cpu_stat is not APIHelper.SKIP:
            self.cpu_stat = cpu_stat 
        if hostname is not APIHelper.SKIP:
            self.hostname = hostname 
        if if_stat is not APIHelper.SKIP:
            self.if_stat = if_stat 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if ip_stat is not APIHelper.SKIP:
            self.ip_stat = ip_stat 
        if last_seen is not APIHelper.SKIP:
            self.last_seen = last_seen 
        if last_trouble is not APIHelper.SKIP:
            self.last_trouble = last_trouble 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if memory_stat is not APIHelper.SKIP:
            self.memory_stat = memory_stat 
        if model is not APIHelper.SKIP:
            self.model = model 
        if module_stat is not APIHelper.SKIP:
            self.module_stat = module_stat 
        if name is not APIHelper.SKIP:
            self.name = name 
        if num_clients is not APIHelper.SKIP:
            self.num_clients = num_clients 
        if serial is not APIHelper.SKIP:
            self.serial = serial 
        if status is not APIHelper.SKIP:
            self.status = status 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if uptime is not APIHelper.SKIP:
            self.uptime = uptime 
        if version is not APIHelper.SKIP:
            self.version = version 

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

        clients = None
        if dictionary.get('clients') is not None:
            clients = [Client1.from_dictionary(x) for x in dictionary.get('clients')]
        else:
            clients = APIHelper.SKIP
        cpu_stat = CpuStat1.from_dictionary(dictionary.get('cpu_stat')) if 'cpu_stat' in dictionary.keys() else APIHelper.SKIP
        hostname = dictionary.get("hostname") if dictionary.get("hostname") else APIHelper.SKIP
        if_stat = IfStat.from_dictionary(dictionary.get('if_stat')) if 'if_stat' in dictionary.keys() else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        ip_stat = IpStat2.from_dictionary(dictionary.get('ip_stat')) if 'ip_stat' in dictionary.keys() else APIHelper.SKIP
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else APIHelper.SKIP
        last_trouble = LastTrouble1.from_dictionary(dictionary.get('last_trouble')) if 'last_trouble' in dictionary.keys() else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        memory_stat = MemoryStat1.from_dictionary(dictionary.get('memory_stat')) if 'memory_stat' in dictionary.keys() else APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        module_stat = None
        if dictionary.get('module_stat') is not None:
            module_stat = [ModuleStat1.from_dictionary(x) for x in dictionary.get('module_stat')]
        else:
            module_stat = APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        num_clients = NumClients.from_dictionary(dictionary.get('num_clients')) if 'num_clients' in dictionary.keys() else APIHelper.SKIP
        serial = dictionary.get("serial") if dictionary.get("serial") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        uptime = dictionary.get("uptime") if dictionary.get("uptime") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(clients,
                   cpu_stat,
                   hostname,
                   if_stat,
                   ip,
                   ip_stat,
                   last_seen,
                   last_trouble,
                   mac,
                   memory_stat,
                   model,
                   module_stat,
                   name,
                   num_clients,
                   serial,
                   status,
                   mtype,
                   uptime,
                   version)
