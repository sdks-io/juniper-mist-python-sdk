# Sites EVPN Topologies

```python
sites_evpn_topologies_controller = client.sites_evpn_topologies
```

## Class Name

`SitesEVPNTopologiesController`

## Methods

* [Get Site Evpn Topology](../../doc/controllers/sites-evpn-topologies.md#get-site-evpn-topology)
* [Create Site Evpn Topology](../../doc/controllers/sites-evpn-topologies.md#create-site-evpn-topology)
* [Delete Site Evpn Topology](../../doc/controllers/sites-evpn-topologies.md#delete-site-evpn-topology)
* [Get Site Evpn Tolopogy](../../doc/controllers/sites-evpn-topologies.md#get-site-evpn-tolopogy)
* [Update Site Evpn Topology](../../doc/controllers/sites-evpn-topologies.md#update-site-evpn-topology)


# Get Site Evpn Topology

Get the existing EVPN topology

```python
def get_site_evpn_topology(self,
                          site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`JunosEvpnTopology`](../../doc/models/junos-evpn-topology.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_evpn_topologies_controller.get_site_evpn_topology(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "9197ec96-4c8d-529f-c595-035895e688b2",
  "name": "CC",
  "pod_names": {
    "1": "default",
    "2": "default"
  },
  "switches": [
    {
      "downlink_ips": [
        "10.255.240.6",
        "10.255.240.8"
      ],
      "downlinks": [
        "5c5b35000007",
        "5c5b35000008"
      ],
      "evpn_id": 1,
      "mac": "5c5b35000003",
      "model": "QFX10002-36Q",
      "role": "collapsed-core",
      "uplinks": [
        "5c5b35000005",
        "5c5b35000006"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEvpnTopologies401ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEvpnTopologies403ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEvpnTopologies404ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-404-error-exception.md) |


# Create Site Evpn Topology

While all the `evpn_id` / `downlink_ips` can be specifidd by hand, the easiest way is to call the `build_vpn_topology` API, allowing you to examine the diff, and update it yourself. You can also simply call it with `overwrite=true` which will apply the updates for you.

**Notes:**

1. You can use `core` / `distribution` / `access` to create a CLOS topology
2. You can also use `core` / `distribution` to form a 2-tier EVPN topology where ESI-Lag is configured distribution to connect to access switches
3. In a small/medium campus, `collapsed-core` can be used where core switches are the inter-connected to do EVPN
4. The API uses a few pre-defined parameters and best-practices to generate the configs. It can be customized by using `evpn_options` in Site Setting / Network Template. (e.g. a different subnet for the underlay)

#### Collapsed Core

In a small-medium campus, EVPN can also be enabled only at the core switches (up to 4) by assigning all participating switches with `collapsed-core role`. When there are more than 2 switches, a ring-like topology will be formed.

#### ESI-Lag

If the access switchess does not have EVPN support, you can take advantage of EVPN by setting up ESI-Lag on distribution switches

#### Leaf / Access / Collapsed-Core

For leaf nodes in a EVPN topology, you’d have to configure the IPs for networks that would participate in EVPN. Optionally, VRFs to isolate traffic from one tenant verus another

```python
def create_site_evpn_topology(self,
                             site_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`JunosEvpnTopology`](../../doc/models/junos-evpn-topology.md) | Body, Optional | - |

## Response Type

[`JunosEvpnTopology`](../../doc/models/junos-evpn-topology.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = JunosEvpnTopology(
    switches=[
        Switches1(
            mac='5c5b35000003',
            role=Role5Enum.COLLAPSEDCORE
        ),
        Switches1(
            mac='5c5b35000004',
            role=Role5Enum.COLLAPSEDCORE
        )
    ],
    name='CC',
    pod_names={
        "1": 'default',
        "2": 'default'
    }
)

result = sites_evpn_topologies_controller.create_site_evpn_topology(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "9197ec96-4c8d-529f-c595-035895e688b2",
  "name": "CC",
  "pod_names": {
    "1": "default",
    "2": "default"
  },
  "switches": [
    {
      "downlink_ips": [
        "10.255.240.6",
        "10.255.240.8"
      ],
      "downlinks": [
        "5c5b35000007",
        "5c5b35000008"
      ],
      "evpn_id": 1,
      "mac": "5c5b35000003",
      "model": "QFX10002-36Q",
      "role": "collapsed-core",
      "uplinks": [
        "5c5b35000005",
        "5c5b35000006"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEvpnTopologies401ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEvpnTopologies403ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEvpnTopologies404ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-404-error-exception.md) |


# Delete Site Evpn Topology

Delete the site EVPN Topology

```python
def delete_site_evpn_topology(self,
                             site_id,
                             evpn_topology_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `evpn_topology_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

evpn_topology_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_evpn_topologies_controller.delete_site_evpn_topology(
    site_id,
    evpn_topology_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEvpnTopologies401ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEvpnTopologies403ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEvpnTopologies404ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-404-error-exception.md) |


# Get Site Evpn Tolopogy

Get One EVPN Topology Detail

```python
def get_site_evpn_tolopogy(self,
                          site_id,
                          evpn_topology_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `evpn_topology_id` | `uuid\|string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

evpn_topology_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_evpn_topologies_controller.get_site_evpn_tolopogy(
    site_id,
    evpn_topology_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEvpnTopologies401ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEvpnTopologies403ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEvpnTopologies404ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-404-error-exception.md) |


# Update Site Evpn Topology

Update the EVPN Topolgy

```python
def update_site_evpn_topology(self,
                             site_id,
                             evpn_topology_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `evpn_topology_id` | `uuid\|string` | Template, Required | - |
| `body` | [`JunosEvpnTopology`](../../doc/models/junos-evpn-topology.md) | Body, Optional | - |

## Response Type

[`JunosEvpnTopology`](../../doc/models/junos-evpn-topology.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

evpn_topology_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = JunosEvpnTopology(
    switches=[
        Switches1(
            mac='5c5b35000003',
            role=Role5Enum.COLLAPSEDCORE
        ),
        Switches1(
            mac='5c5b35000004',
            role=Role5Enum.NONE
        )
    ]
)

result = sites_evpn_topologies_controller.update_site_evpn_topology(
    site_id,
    evpn_topology_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "9197ec96-4c8d-529f-c595-035895e688b2",
  "name": "CC",
  "pod_names": {
    "1": "default",
    "2": "default"
  },
  "switches": [
    {
      "downlink_ips": [
        "10.255.240.6",
        "10.255.240.8"
      ],
      "downlinks": [
        "5c5b35000007",
        "5c5b35000008"
      ],
      "evpn_id": 1,
      "mac": "5c5b35000003",
      "model": "QFX10002-36Q",
      "role": "collapsed-core",
      "uplinks": [
        "5c5b35000005",
        "5c5b35000006"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEvpnTopologies401ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEvpnTopologies403ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEvpnTopologies404ErrorException`](../../doc/models/api-v1-sites-evpn-topologies-404-error-exception.md) |

