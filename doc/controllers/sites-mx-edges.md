# Sites Mx Edges

```python
sites_mx_edges_controller = client.sites_mx_edges
```

## Class Name

`SitesMxEdgesController`

## Methods

* [List Site Mx Edges](../../doc/controllers/sites-mx-edges.md#list-site-mx-edges)
* [Create Site Mx Edge](../../doc/controllers/sites-mx-edges.md#create-site-mx-edge)
* [Delete Site Mx Edge](../../doc/controllers/sites-mx-edges.md#delete-site-mx-edge)
* [Get Site Mx Edge](../../doc/controllers/sites-mx-edges.md#get-site-mx-edge)
* [Update Site Mx Edge](../../doc/controllers/sites-mx-edges.md#update-site-mx-edge)
* [Upload Site Mx Edge Support Files](../../doc/controllers/sites-mx-edges.md#upload-site-mx-edge-support-files)


# List Site Mx Edges

Get List of Site Mist Edges

```python
def list_site_mx_edges(self,
                      site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Mxedge`](../../doc/models/mxedge.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_mx_edges_controller.list_site_mx_edges(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "cpu_stat": {
      "cpus": {
        "cpu0": {
          "idle": 79,
          "interrupt": 0,
          "system": 4,
          "usage": 20,
          "user": 16
        },
        "cpu1": {
          "idle": 93,
          "interrupt": 0,
          "system": 4,
          "usage": 6,
          "user": 1
        }
      },
      "idle": 87,
      "interrupt": 0,
      "system": 5,
      "usage": 12,
      "user": 7
    },
    "ext_ip": "116.187.144.16",
    "id": "387804a7-3474-85ce-15a2-f9a9684c9c90",
    "ip_stat": {
      "ip": "172.16.5.3",
      "ips": {
        "ens192": "172.16.5.3/24,fe81::20c:29ff:fef8:d18e/64"
      }
    },
    "lag_stat": {
      "lag0": {
        "active_ports": [
          "0",
          "1"
        ]
      }
    },
    "last_seen": 1547437078,
    "magic": "ExNpT5gi-ADR8WTFd4EiQPY3cP5WdSoD",
    "memory_stats": {
      "active": 1061085184,
      "available": 4124860416,
      "buffers": 789495808,
      "cached": 718016512,
      "free": 2818838528,
      "inactive": 458158080,
      "swap_cached": 0,
      "swap_free": 8161062912,
      "swap_total": 8161062912,
      "total": 7947616256,
      "usage": 65
    },
    "model": "ME-S2019",
    "mxagent_registered": false,
    "mxcluster_id": "572586b7-f97b-a22b-526c-8b97a3f609c4",
    "name": "Guest",
    "num_tunnels": 31,
    "port_stat": {
      "eth0": {
        "full_duplex": true,
        "lldp_stats": {
          "mgmt_addr": "122.16.3.11",
          "port_desc": "GigabitEthernet4/0/16",
          "port_id": "\u0005Gi4/0/16",
          "system_desc": "Cisco IOS Software",
          "system_name": "ME-DC2-DIS-SW"
        },
        "rx_bytes": 2056,
        "rx_errors": 0,
        "rx_pkts": 670,
        "speed": 1000,
        "tx_bytes": 2056,
        "tx_pkts": 670,
        "up": true
      },
      "eth1": {
        "up": false
      },
      "module": {
        "up": false
      }
    },
    "status": "connected",
    "tunterm_registered": false,
    "tunterm_stat": {
      "monitoring_failed": false
    },
    "uptime": 884221,
    "version": "0.1.2",
    "virtualization_type": "VirtualizationVMware"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedges401ErrorException`](../../doc/models/api-v1-sites-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedges403ErrorException`](../../doc/models/api-v1-sites-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedges404ErrorException`](../../doc/models/api-v1-sites-mxedges-404-error-exception.md) |


# Create Site Mx Edge

Create Site Mist Edge

```python
def create_site_mx_edge(self,
                       site_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Mxedge`](../../doc/models/mxedge.md) | Body, Optional | - |

## Response Type

[`Mxedge`](../../doc/models/mxedge.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Mxedge(
    model='ME-100',
    name='Guest',
    id='95ddd29a-6a3c-929e-a431-51a5b09f36a6',
    magic='L-NpT5gi-ADR8WTFd4EiQPY3cP5WdSoD',
    mxcluster_id='572586b7-f97b-a22b-526c-8b97a3f609c4',
    note='note for mxedge'
)

result = sites_mx_edges_controller.create_site_mx_edge(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "95ddd29a-6a3c-929e-a431-51a5b09f36a6",
  "magic": "L-NpT5gi-ADR8WTFd4EiQPY3cP5WdSoD",
  "model": "ME-100",
  "mxagent_registered": true,
  "mxcluster_id": "572586b7-f97b-a22b-526c-8b97a3f609c4",
  "mxedge_mgmt": {
    "mist_password": "MIST_PASSWORD",
    "root_password": "ROOT_PASSWORD"
  },
  "name": "Guest",
  "ntp_servers": [],
  "oob_ip_config": {
    "dns": [
      "8.8.8.8",
      "4.4.4.4"
    ],
    "gateway": "10.2.1.254",
    "ip": "10.2.1.10",
    "netmask": "255.255.255.0",
    "type": "static"
  },
  "tunterm_dhcpd_config": {
    "2": {
      "enabled": true,
      "servers": [
        "11.2.3.44"
      ]
    },
    "enabled": false,
    "servers": [
      "11.2.3.4"
    ]
  },
  "tunterm_extra_routes": {
    "11.0.0.0/8": {
      "via": "10.3.3.1"
    }
  },
  "tunterm_ip_config": {
    "dns": [
      "8.8.8.8"
    ],
    "dns_suffix": [
      ".mist.local"
    ],
    "gateway": "10.2.1.254",
    "ip": "10.2.1.1",
    "netmask": "255.255.255.0"
  },
  "tunterm_monitoring": [
    {
      "host": "10.2.8.15",
      "port": 80,
      "protocol": "ping",
      "timeout": 300
    }
  ],
  "tunterm_other_ip_configs": {
    "5": {
      "ip": "10.3.3.1",
      "netmask": "255.255.255.0"
    }
  },
  "tunterm_port_config": {
    "downstream_ports": [
      "3"
    ],
    "separate_upstream_downstream": true,
    "upstream_port_vlan_id": 30,
    "upstream_ports": [
      "0",
      "1",
      "2"
    ]
  },
  "tunterm_registered": true,
  "tunterm_switch_config": {
    "0": {
      "port_vlan_id": 1,
      "vlan_ids": [
        1,
        3055
      ]
    },
    "enabled": true
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedges401ErrorException`](../../doc/models/api-v1-sites-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedges403ErrorException`](../../doc/models/api-v1-sites-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedges404ErrorException`](../../doc/models/api-v1-sites-mxedges-404-error-exception.md) |


# Delete Site Mx Edge

Delete Site Mist Edge

```python
def delete_site_mx_edge(self,
                       site_id,
                       mxedge_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mxedge_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_mx_edges_controller.delete_site_mx_edge(
    site_id,
    mxedge_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedges401ErrorException`](../../doc/models/api-v1-sites-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedges403ErrorException`](../../doc/models/api-v1-sites-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedges404ErrorException`](../../doc/models/api-v1-sites-mxedges-404-error-exception.md) |


# Get Site Mx Edge

get Site Mist Edge

```python
def get_site_mx_edge(self,
                    site_id,
                    mxedge_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mxedge_id` | `uuid\|string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_mx_edges_controller.get_site_mx_edge(
    site_id,
    mxedge_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedges401ErrorException`](../../doc/models/api-v1-sites-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedges403ErrorException`](../../doc/models/api-v1-sites-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedges404ErrorException`](../../doc/models/api-v1-sites-mxedges-404-error-exception.md) |


# Update Site Mx Edge

Update Site Mist Edge settings

```python
def update_site_mx_edge(self,
                       site_id,
                       mxedge_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mxedge_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Mxedge`](../../doc/models/mxedge.md) | Body, Optional | - |

## Response Type

[`Mxedge`](../../doc/models/mxedge.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Mxedge(
    model='ME-100',
    name='Guest',
    id='95ddd29a-6a3c-929e-a431-51a5b09f36a6',
    magic='L-NpT5gi-ADR8WTFd4EiQPY3cP5WdSoD',
    mxcluster_id='572586b7-f97b-a22b-526c-8b97a3f609c4',
    note='note for mxedge'
)

result = sites_mx_edges_controller.update_site_mx_edge(
    site_id,
    mxedge_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "95ddd29a-6a3c-929e-a431-51a5b09f36a6",
  "magic": "L-NpT5gi-ADR8WTFd4EiQPY3cP5WdSoD",
  "model": "ME-100",
  "mxagent_registered": true,
  "mxcluster_id": "572586b7-f97b-a22b-526c-8b97a3f609c4",
  "mxedge_mgmt": {
    "mist_password": "MIST_PASSWORD",
    "root_password": "ROOT_PASSWORD"
  },
  "name": "Guest",
  "ntp_servers": [],
  "oob_ip_config": {
    "dns": [
      "8.8.8.8",
      "4.4.4.4"
    ],
    "gateway": "10.2.1.254",
    "ip": "10.2.1.10",
    "netmask": "255.255.255.0",
    "type": "static"
  },
  "tunterm_dhcpd_config": {
    "2": {
      "enabled": true,
      "servers": [
        "11.2.3.44"
      ]
    },
    "enabled": false,
    "servers": [
      "11.2.3.4"
    ]
  },
  "tunterm_extra_routes": {
    "11.0.0.0/8": {
      "via": "10.3.3.1"
    }
  },
  "tunterm_ip_config": {
    "dns": [
      "8.8.8.8"
    ],
    "dns_suffix": [
      ".mist.local"
    ],
    "gateway": "10.2.1.254",
    "ip": "10.2.1.1",
    "netmask": "255.255.255.0"
  },
  "tunterm_monitoring": [
    {
      "host": "10.2.8.15",
      "port": 80,
      "protocol": "ping",
      "timeout": 300
    }
  ],
  "tunterm_other_ip_configs": {
    "5": {
      "ip": "10.3.3.1",
      "netmask": "255.255.255.0"
    }
  },
  "tunterm_port_config": {
    "downstream_ports": [
      "3"
    ],
    "separate_upstream_downstream": true,
    "upstream_port_vlan_id": 30,
    "upstream_ports": [
      "0",
      "1",
      "2"
    ]
  },
  "tunterm_registered": true,
  "tunterm_switch_config": {
    "0": {
      "port_vlan_id": 1,
      "vlan_ids": [
        1,
        3055
      ]
    },
    "enabled": true
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedges401ErrorException`](../../doc/models/api-v1-sites-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedges403ErrorException`](../../doc/models/api-v1-sites-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedges404ErrorException`](../../doc/models/api-v1-sites-mxedges-404-error-exception.md) |


# Upload Site Mx Edge Support Files

Support / Upload Mist Edge support files

```python
def upload_site_mx_edge_support_files(self,
                                     site_id,
                                     mxedge_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `string` | Template, Required | - |
| `mxedge_id` | `string` | Template, Required | - |

## Response Type

[`ApiV1SitesMxedgesSupportResponse`](../../doc/models/api-v1-sites-mxedges-support-response.md)

## Example Usage

```python
site_id = 'site_id6'

mxedge_id = 'mxedge_id6'

result = sites_mx_edges_controller.upload_site_mx_edge_support_files(
    site_id,
    mxedge_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 1574114372,
  "for_site": true,
  "id": "b025de9b-7bb6-43bd-8a71-bf3cu840c9ad",
  "magic": "S2ZD-srTcoOp9GGttZpq1ISQEq4iPY3EhWpAKB9pb9JdWjeP12bjIbFYsDy5jP3a",
  "model": "ME-100",
  "modified_time": 1574117211,
  "mxagent_registered": false,
  "mxcluster_id": "c88aa7a2-ac27-7d87-b633-1ac3a7837929",
  "name": "staging_edge",
  "org_id": "5a5ed2f4-632f-41f3-b8ed-d3afa4b27f96",
  "services": [
    "tunterm"
  ],
  "site_id": "c88aa7a2-ac27-7d87-b633-1ac3a7837928",
  "status": "disconnected",
  "tunterm_ip_config": {
    "gateway": "",
    "ip": "",
    "netmask": ""
  },
  "tunterm_port_config": {
    "downstream_ports": [
      "0"
    ],
    "separate_upstream_downstream": false,
    "upstream_ports": [
      "0"
    ]
  },
  "tunterm_registered": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxedgesSupport401ErrorException`](../../doc/models/api-v1-sites-mxedges-support-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxedgesSupport403ErrorException`](../../doc/models/api-v1-sites-mxedges-support-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxedgesSupport404ErrorException`](../../doc/models/api-v1-sites-mxedges-support-404-error-exception.md) |

