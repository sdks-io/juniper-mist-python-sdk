# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.cluster_stat import ClusterStat
from mistapi.models.cpu_stat import CpuStat
from mistapi.models.ip_stat_1 import IpStat1
from mistapi.models.memory_stat import MemoryStat
from mistapi.models.module_stat import ModuleStat
from mistapi.models.spu_stat import SpuStat


class StatsDeviceGateway(object):

    """Implementation of the 'stats_device_gateway' model.

    Gateway statistics

    Attributes:
        cluster_stat (dict): TODO: type description here.
        cpu_2_stat (string): TODO: type description here.
        cpu_stat (CpuStat): TODO: type description here.
        hostname (string): hostname reported by the device
        ip (string): IP address
        ip_stat (IpStat1): TODO: type description here.
        last_seen (float): last seen timestamp
        mac (string): device mac
        memory_stat (MemoryStat): TODO: type description here.
        model (string): device model
        module_2_stat (string): TODO: type description here.
        module_stat (list of ModuleStat): TODO: type description here.
        name (string): device name if configured
        serial (string): serial
        spu_2_stat (string): TODO: type description here.
        spu_stat (SpuStat): TODO: type description here.
        status (string): TODO: type description here.
        mtype (string): TODO: type description here.
        uptime (float): TODO: type description here.
        version (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac',
        "cluster_stat": 'cluster_stat',
        "cpu_2_stat": 'cpu2_stat',
        "cpu_stat": 'cpu_stat',
        "hostname": 'hostname',
        "ip": 'ip',
        "ip_stat": 'ip_stat',
        "last_seen": 'last_seen',
        "memory_stat": 'memory_stat',
        "model": 'model',
        "module_2_stat": 'module2_stat',
        "module_stat": 'module_stat',
        "name": 'name',
        "serial": 'serial',
        "spu_2_stat": 'spu2_stat',
        "spu_stat": 'spu_stat',
        "status": 'status',
        "mtype": 'type',
        "uptime": 'uptime',
        "version": 'version'
    }

    _optionals = [
        'cluster_stat',
        'cpu_2_stat',
        'cpu_stat',
        'hostname',
        'ip',
        'ip_stat',
        'last_seen',
        'memory_stat',
        'model',
        'module_2_stat',
        'module_stat',
        'name',
        'serial',
        'spu_2_stat',
        'spu_stat',
        'status',
        'mtype',
        'uptime',
        'version',
    ]

    def __init__(self,
                 mac=None,
                 cluster_stat=APIHelper.SKIP,
                 cpu_2_stat=APIHelper.SKIP,
                 cpu_stat=APIHelper.SKIP,
                 hostname=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 ip_stat=APIHelper.SKIP,
                 last_seen=APIHelper.SKIP,
                 memory_stat=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 module_2_stat=APIHelper.SKIP,
                 module_stat=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 serial=APIHelper.SKIP,
                 spu_2_stat=APIHelper.SKIP,
                 spu_stat=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 uptime=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the StatsDeviceGateway class"""

        # Initialize members of the class
        if cluster_stat is not APIHelper.SKIP:
            self.cluster_stat = cluster_stat 
        if cpu_2_stat is not APIHelper.SKIP:
            self.cpu_2_stat = cpu_2_stat 
        if cpu_stat is not APIHelper.SKIP:
            self.cpu_stat = cpu_stat 
        if hostname is not APIHelper.SKIP:
            self.hostname = hostname 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if ip_stat is not APIHelper.SKIP:
            self.ip_stat = ip_stat 
        if last_seen is not APIHelper.SKIP:
            self.last_seen = last_seen 
        self.mac = mac 
        if memory_stat is not APIHelper.SKIP:
            self.memory_stat = memory_stat 
        if model is not APIHelper.SKIP:
            self.model = model 
        if module_2_stat is not APIHelper.SKIP:
            self.module_2_stat = module_2_stat 
        if module_stat is not APIHelper.SKIP:
            self.module_stat = module_stat 
        if name is not APIHelper.SKIP:
            self.name = name 
        if serial is not APIHelper.SKIP:
            self.serial = serial 
        if spu_2_stat is not APIHelper.SKIP:
            self.spu_2_stat = spu_2_stat 
        if spu_stat is not APIHelper.SKIP:
            self.spu_stat = spu_stat 
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

        mac = dictionary.get("mac") if dictionary.get("mac") else None
        cluster_stat = ClusterStat.from_dictionary(dictionary.get('cluster_stat')) if 'cluster_stat' in dictionary.keys() else APIHelper.SKIP
        cpu_2_stat = dictionary.get("cpu2_stat") if dictionary.get("cpu2_stat") else APIHelper.SKIP
        cpu_stat = CpuStat.from_dictionary(dictionary.get('cpu_stat')) if 'cpu_stat' in dictionary.keys() else APIHelper.SKIP
        hostname = dictionary.get("hostname") if dictionary.get("hostname") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        ip_stat = IpStat1.from_dictionary(dictionary.get('ip_stat')) if 'ip_stat' in dictionary.keys() else APIHelper.SKIP
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else APIHelper.SKIP
        memory_stat = MemoryStat.from_dictionary(dictionary.get('memory_stat')) if 'memory_stat' in dictionary.keys() else APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        module_2_stat = dictionary.get("module2_stat") if dictionary.get("module2_stat") else APIHelper.SKIP
        module_stat = None
        if dictionary.get('module_stat') is not None:
            module_stat = [ModuleStat.from_dictionary(x) for x in dictionary.get('module_stat')]
        else:
            module_stat = APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        serial = dictionary.get("serial") if dictionary.get("serial") else APIHelper.SKIP
        spu_2_stat = dictionary.get("spu2_stat") if dictionary.get("spu2_stat") else APIHelper.SKIP
        spu_stat = SpuStat.from_dictionary(dictionary.get('spu_stat')) if 'spu_stat' in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        uptime = dictionary.get("uptime") if dictionary.get("uptime") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(mac,
                   cluster_stat,
                   cpu_2_stat,
                   cpu_stat,
                   hostname,
                   ip,
                   ip_stat,
                   last_seen,
                   memory_stat,
                   model,
                   module_2_stat,
                   module_stat,
                   name,
                   serial,
                   spu_2_stat,
                   spu_stat,
                   status,
                   mtype,
                   uptime,
                   version)
