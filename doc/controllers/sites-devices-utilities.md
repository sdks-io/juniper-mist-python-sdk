# Sites Devices Utilities

```python
sites_devices_utilities_controller = client.sites_devices_utilities
```

## Class Name

`SitesDevicesUtilitiesController`

## Methods

* [Arp From Device](../../doc/controllers/sites-devices-utilities.md#arp-from-device)
* [Ping From Device](../../doc/controllers/sites-devices-utilities.md#ping-from-device)
* [Create Site Device Snapshot](../../doc/controllers/sites-devices-utilities.md#create-site-device-snapshot)
* [Traceroute From Device](../../doc/controllers/sites-devices-utilities.md#traceroute-from-device)


# Arp From Device

ARP can be performed on the Device. The output will be available through websocket. As there can be multiple command issued against the same AP at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```json
{ 
 "event": "data", 
 "channel": "/sites/4ac1dcf4-9d8b-7211-65c4-057819f0862b/devices/00000000-0000-0000-1000-5c5b350e0060/cmd", 
 "data": { 
   "session": "session_id", 
   "raw": 
   "Output": "\tMAC\t\tDEV\tVLAN\tRx Packets\t\t Rx Bytes\t\tTx Packets\t\t Tx Bytes\tFlows\tIdle sec\n-----------------------------------------------------------------------------------------------------------------------"
  } 
}
```

```python
def arp_from_device(self,
                   site_id,
                   device_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesArpRequest`](../../doc/models/api-v1-sites-devices-arp-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesArpRequest(
    node=NodeEnum.NODE0
)

result = sites_devices_utilities_controller.arp_from_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "session": "session_id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesArp401ErrorException`](../../doc/models/api-v1-sites-devices-arp-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesArp403ErrorException`](../../doc/models/api-v1-sites-devices-arp-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesArp404ErrorException`](../../doc/models/api-v1-sites-devices-arp-404-error-exception.md) |


# Ping From Device

Ping from AP, Switch and SSR

Ping can be performed from the Device. The output will be available through websocket. As there can be multiple command issued against the same AP at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```json
{
    "event": "data",
    "channel": "/sites/4ac1dcf4-9d8b-7211-65c4-057819f0862b/devices/00000000-0000-0000-1000-5c5b350e0060/cmd",
    "data": {
        "session": "session_id",
        "raw": "64 bytes from 23.211.0.110: seq=8 ttl=58 time=12.323 ms\n"
    }
}
```

```python
def ping_from_device(self,
                    site_id,
                    device_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesPingRequest`](../../doc/models/api-v1-sites-devices-ping-request.md) | Body, Optional | Request Body |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesPingRequest(
    host='1.1.1.1',
    count=10
)

result = sites_devices_utilities_controller.ping_from_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "session": "session_id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesPing401ErrorException`](../../doc/models/api-v1-sites-devices-ping-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesPing403ErrorException`](../../doc/models/api-v1-sites-devices-ping-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesPing404ErrorException`](../../doc/models/api-v1-sites-devices-ping-404-error-exception.md) |


# Create Site Device Snapshot

Create recovery device snapshot (Available on Junos OS EX2300-, EX3400-, EX4400- devices)

```python
def create_site_device_snapshot(self,
                               site_id,
                               device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesDevicesSnapshotResponse`](../../doc/models/api-v1-sites-devices-snapshot-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_utilities_controller.create_site_device_snapshot(
    site_id,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status_id": "string",
  "staus": "starting",
  "timestamp": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesSnapshot401ErrorException`](../../doc/models/api-v1-sites-devices-snapshot-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesSnapshot403ErrorException`](../../doc/models/api-v1-sites-devices-snapshot-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesSnapshot404ErrorException`](../../doc/models/api-v1-sites-devices-snapshot-404-error-exception.md) |


# Traceroute From Device

Traceroute can be performed from the Device. The output will be available through websocket. As there can be multiple command issued against the same AP at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

```python
def traceroute_from_device(self,
                          site_id,
                          device_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesTracerouteRequest`](../../doc/models/api-v1-sites-devices-traceroute-request.md) | Body, Optional | Request Body |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesTracerouteRequest(
    host='string',
    port=33434,
    protocol=Protocol9Enum.UDP
)

result = sites_devices_utilities_controller.traceroute_from_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "session": "session_id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesTraceroute401ErrorException`](../../doc/models/api-v1-sites-devices-traceroute-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesTraceroute403ErrorException`](../../doc/models/api-v1-sites-devices-traceroute-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesTraceroute404ErrorException`](../../doc/models/api-v1-sites-devices-traceroute-404-error-exception.md) |

