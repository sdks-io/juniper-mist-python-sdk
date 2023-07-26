# Sites Devices-WANHA

```python
sites_devices_wanha_controller = client.sites_devices_wanha
```

## Class Name

`SitesDevicesWANHAController`

## Methods

* [Delete Site Device Ha Cluster](../../doc/controllers/sites-devices-wanha.md#delete-site-device-ha-cluster)
* [Create Site Device Ha Cluster](../../doc/controllers/sites-devices-wanha.md#create-site-device-ha-cluster)
* [Swap Site Device Ha Cluster Node](../../doc/controllers/sites-devices-wanha.md#swap-site-device-ha-cluster-node)


# Delete Site Device Ha Cluster

Delete HA Cluster

```python
def delete_site_device_ha_cluster(self,
                                 site_id,
                                 device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wan_ha_controller.delete_site_device_ha_cluster(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesHa401ErrorException`](../../doc/models/api-v1-sites-devices-ha-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesHa403ErrorException`](../../doc/models/api-v1-sites-devices-ha-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesHa404ErrorException`](../../doc/models/api-v1-sites-devices-ha-404-error-exception.md) |


# Create Site Device Ha Cluster

Create HA Cluster
Both nodes has to be in the same site. We expect the user to configure ha_sync / ha_data port in port_configs already

### SRX cabling

see [Chassis Cluster User Guide for SRX Series Devices](https://www.juniper.net/documentation/us/en/software/junos/chassis-cluster-security-devices/topics/concept/chassis-cluster-srx-series-node-interface-understanding.html) Here’s the recommended cabling.

#### SRX300

From ZTP / default state, ge-0/0/0 and ge-0/0/7 (SFP) are default WAN ports and will get DHCP IP. However, ge-0/0/0 becomes OOB/fxp0 after cluster is enabled (i.e. using it for reach Mist is not recommended)

1. form cluster in UI
2. configure ge-0/0/7,ge-1/0/7 for WAN (reth0)
3. configure ge-0/0/2,ge-1/0/2 for ha_data
4. configure ge-0/0/3- for LAN or additional WAN e.g.

```json
{
    "port_config": {
        "ge-0/0/2,ge-1/0/2": {
            "usage": "ha_data"
        },
        "ge-0/0/7,ge-1/0/7": {
            "usage": "wan",
            "redundant": true,
            "reth_idx": 0,
            "ip_config": {"type": "dhcp"}
        },
    }
}

```

1. connect ge-0/0/1 back to back for ha_control
2. connect ge-0/0/2 back to back for ha_data
3. connect both ge-0/0/7 to uplink switch to WAN and to reach Mist
4. power up both devices
5. it takes about 30 minutes for the cluster to form

#### SRX320

From ZTP / default state, ge-0/0/0, ge-0/0/7 (SFP) and cl-1/0/0 (LTE) are default WAN ports and will get DHCP IP. However, ge-0/0/0 becomes OOB/fxp0 after cluster is enabled (i.e. using it for reach Mist is not recommended)

##### ZTP via ge-0/0/7

Similar to SRX300

##### ZTP via cl-1/0/0 (LTE)

1. form cluster in UI
2. configure cl-1/0/0, cl-3/0/0 as WAN (reth0)
3. configure ge-0/0/2,ge-3/0/2 for ha_data
4. same as above

#### SRX340 / SRX345 / SRX380

SRX340/SRX345 has dedicated OOB/fxp0 ports

1. form cluster in UI
2. configure ge-0/0/0,ge-5/0/0 for WAN (reth0)
3. configure ge-0/0/2,ge-5/0/2 for ha_data
4. configure ge-0/0/3- for LAN or additional WAN
5. connect ge-0/0/0 to uplink switch to WAN and to reach Mist
6. connect ge-0/0/1 back-to-back for ha_control
7. connect ge-0/0/2 back-to-back for ha_data (fabric); or for SRX380, xe-0/0/16 if 10G SFP+ is used
8. connect ge-0/0/3- to LAN or additional WANs

#### SRX550

ge-0/0/0 becomes OOB/fxp0 after cluster is enabled, make suenable oob_ip_config as dhcp to maintain cloud connectivity

1. connect ge-0/0/0 to reach Mist (after cluster is fully up, this port becomes OOB/fxp0)
2. connect ge-0/0/1 back-to-back for ha_control
3. connect ge-0/0/2 back-to-back for ha_data (fabric)
4. connect ge-0/0/3 to WAN (after cluster is up, intended to be used for reth0)
5. connect ge-0/0/4- to LAN or additional WANs

#### SRX1500

SRX1500 has, additionally, dedicated HA Control port

1. form cluster in UI
2. configure ge-0/0/0,ge-5/0/0 for WAN (reth0)
3. configure ge-0/0/1,ge-5/0/1 for ha_data
4. configure ge-0/0/2- for LAN or additional WAN
5. connect dedicated ha_control back-to-back
6. connect ge-0/0/0 to uplink switch to WAN and to reach Mist
7. connect ge-0/0/1 back-to-back for ha_data
8. connect ge-0/0/2- to LAN or additional WANs

#### SRX4100

SRX4100 has dedicated ha_control and ha_data (fabric) ports

1. connect dedicated ha_control back-to-back
2. connect dedicated ha_data back-to-back
3. connect xe-0/0/0 to WAN to reach Mist
4. connect xe-0/0/1- to LAN or additional WANs

#### VSRX

When standalone, VSRX has fxp0 as first Network Adapter, then ge-0/0/0-N When clustered, VSRX has fxp0, em0, then ge-0/0/0-N

1. connect net0 (fxp0) to WAN to reach Mist
2. connect net1 back-to-back for ha_control
3. connect net2 (ge-0/0/0) back-to-back for ha_data (fab0/fab1)
4. connect net3 (ge-0/0/1) to WAN, intended to be used for reth0
5. connect net4 (ge-0/0/2) to LAN

SRX340/SRX345 has dedicated OOB/fxp0 ports VSRX has fxp0 as first Network Adapter, then ge-0/0/0-N

1. connect ge-0/0/0 to WAN to reach Mist
2. connect ge-0/0/1 back-to-back for ha_control
3. connect ge-0/0/2 back-to-back for ha_data (fabric); or for SRX380, xe-0/0/16 if 10G SFP+ is used
4. connect ge-0/0/3- to LAN or additional WANs

#### SRX550

ge-0/0/0 becomes OOB/fxp0 after cluster is enabled, make suenable oob_ip_config as dhcp to maintain cloud connectivity

1. connect ge-0/0/0 to reach Mist (after cluster is fully up, this port becomes OOB/fxp0)
2. connect ge-0/0/1 back-to-back for ha_control
3. connect ge-0/0/2 back-to-back for ha_data (fabric)
4. connect ge-0/0/3 to WAN (after cluster is up, intended to be used for reth0)
5. connect ge-0/0/4- to LAN or additional WANs

#### SRX1500

SRX1500 has, additionally, dedicated HA Control port

1. connect dedicated ha_control back-to-back
2. connect ge-0/0/0 to WAN to reach mist
3. connect ge-0/0/1 back-to-back for ha_data
4. connect ge-0/0/2- to LAN or additional WANs

#### SRX4100

SRX4100 has dedicated ha_control and ha_data (fabric) ports

1. connect dedicated ha_control back-to-back
2. connect dedicated ha_data back-to-back
3. connect xe-0/0/0 to WAN to reach Mist
4. connect xe-0/0/1- to LAN or additional WANs

```python
def create_site_device_ha_cluster(self,
                                 site_id,
                                 device_id,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesHaRequest`](../../doc/models/api-v1-sites-devices-ha-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesHaRequest(
    nodes=[
        Node3(
            mac='aff827549235'
        ),
        Node3(
            mac='8396cd006c8c'
        )
    ]
)

result = sites_devices_wan_ha_controller.create_site_device_ha_cluster(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesHa401ErrorException`](../../doc/models/api-v1-sites-devices-ha-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesHa403ErrorException`](../../doc/models/api-v1-sites-devices-ha-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesHa404ErrorException`](../../doc/models/api-v1-sites-devices-ha-404-error-exception.md) |


# Swap Site Device Ha Cluster Node

**This endpoint is deprecated.**

Swap nodes on the HA Cluster

```python
def swap_site_device_ha_cluster_node(self,
                                    site_id,
                                    device_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesHaRequest1`](../../doc/models/api-v1-sites-devices-ha-request-1.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesHaRequest1(
    op=Op4Enum.SWAP
)

result = sites_devices_wan_ha_controller.swap_site_device_ha_cluster_node(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesHa401ErrorException`](../../doc/models/api-v1-sites-devices-ha-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesHa403ErrorException`](../../doc/models/api-v1-sites-devices-ha-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesHa404ErrorException`](../../doc/models/api-v1-sites-devices-ha-404-error-exception.md) |

