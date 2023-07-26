# Sites Devices-WAN

```python
sites_devices_wan_controller = client.sites_devices_wan
```

## Class Name

`SitesDevicesWANController`

## Methods

* [Clear Site Ssr Arp Cache](../../doc/controllers/sites-devices-wan.md#clear-site-ssr-arp-cache)
* [Clear Site Ssr Bgp Routes](../../doc/controllers/sites-devices-wan.md#clear-site-ssr-bgp-routes)
* [Release Site Ssr Dhcp Lease](../../doc/controllers/sites-devices-wan.md#release-site-ssr-dhcp-lease)
* [Test Site Ssr Dns Resolution](../../doc/controllers/sites-devices-wan.md#test-site-ssr-dns-resolution)
* [Service Ping From Ssr](../../doc/controllers/sites-devices-wan.md#service-ping-from-ssr)
* [Get Site Ssr and Srx Routes](../../doc/controllers/sites-devices-wan.md#get-site-ssr-and-srx-routes)
* [Get Site Ssr Service Path](../../doc/controllers/sites-devices-wan.md#get-site-ssr-service-path)
* [Get Site Ssr and Srx Sessions](../../doc/controllers/sites-devices-wan.md#get-site-ssr-and-srx-sessions)


# Clear Site Ssr Arp Cache

Clear the entire ARP cache or a subset if arguments are provided.

*Note*: port_id is optional if neither vlan nor ip is specified

```python
def clear_site_ssr_arp_cache(self,
                            site_id,
                            device_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesClearArpRequest`](../../doc/models/api-v1-sites-devices-clear-arp-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesClearArpRequest(
    ip='10.1.1.1',
    node=NodeEnum.NODE0,
    port_id='wan',
    vlan=1000
)

result = sites_devices_wan_controller.clear_site_ssr_arp_cache(
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
| 400 | port_id must be specified with vlan or ip<br>Both vlan and ip cannot be specified | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesClearArp401ErrorException`](../../doc/models/api-v1-sites-devices-clear-arp-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesClearArp403ErrorException`](../../doc/models/api-v1-sites-devices-clear-arp-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesClearArp404ErrorException`](../../doc/models/api-v1-sites-devices-clear-arp-404-error-exception.md) |


# Clear Site Ssr Bgp Routes

Clear routes associated with one or all BGP neighbors

```python
def clear_site_ssr_bgp_routes(self,
                             site_id,
                             device_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesClearBgpRequest`](../../doc/models/api-v1-sites-devices-clear-bgp-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesClearBgpRequest(
    neighbor='all',
    mtype=Type53Enum.ENUM_IN,
    vrf='TestVrf'
)

result = sites_devices_wan_controller.clear_site_ssr_bgp_routes(
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
| 400 | parameter neighbor absent | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesClearBgp401ErrorException`](../../doc/models/api-v1-sites-devices-clear-bgp-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesClearBgp403ErrorException`](../../doc/models/api-v1-sites-devices-clear-bgp-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesClearBgp404ErrorException`](../../doc/models/api-v1-sites-devices-clear-bgp-404-error-exception.md) |


# Release Site Ssr Dhcp Lease

Releases an active DHCP lease.

```python
def release_site_ssr_dhcp_lease(self,
                               site_id,
                               device_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesReleaseDhcpRequest`](../../doc/models/api-v1-sites-devices-release-dhcp-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesReleaseDhcpRequest(
    port='string',
    node=NodeEnum.NODE0
)

result = sites_devices_wan_controller.release_site_ssr_dhcp_lease(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Parameter `port` absent | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesReleaseDhcp401ErrorException`](../../doc/models/api-v1-sites-devices-release-dhcp-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesReleaseDhcp403ErrorException`](../../doc/models/api-v1-sites-devices-release-dhcp-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesReleaseDhcp404ErrorException`](../../doc/models/api-v1-sites-devices-release-dhcp-404-error-exception.md) |


# Test Site Ssr Dns Resolution

DNS resolutions are performed on the Device. The output will be available through websocket. As there can be multiple command issued against the same SSR at the same time and the output all goes through the same websocket stream, `session` is used for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```
 Router      | Hostname               | Resolved | Last Resolved        | Expiration
-------------|------------------------|----------|----------------------|---------------------
 test-device | xxx.yyy.net            | Y        | 2022-03-28T03:56:49Z | 2022-03-28T03:57:49Z
```

```python
def test_site_ssr_dns_resolution(self,
                                site_id,
                                device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wan_controller.test_site_ssr_dns_resolution(
    site_id,
    device_id
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
| 401 | Unauthorized | [`ApiV1SitesDevicesResolveDns401ErrorException`](../../doc/models/api-v1-sites-devices-resolve-dns-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesResolveDns403ErrorException`](../../doc/models/api-v1-sites-devices-resolve-dns-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesResolveDns404ErrorException`](../../doc/models/api-v1-sites-devices-resolve-dns-404-error-exception.md) |


# Service Ping From Ssr

Ping from SSR

Service Ping can be performed from the Device. The output will be available through websocket. As there can be multiple command issued against the same device at the same time and the output all goes through the same websocket stream, session is introduced for demux.

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
def service_ping_from_ssr(self,
                         site_id,
                         device_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesServicePingRequest`](../../doc/models/api-v1-sites-devices-service-ping-request.md) | Body, Optional | Request Body |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesServicePingRequest(
    host='1.1.1.1',
    service='web-session',
    count=10
)

result = sites_devices_wan_controller.service_ping_from_ssr(
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
| 401 | Unauthorized | [`ApiV1SitesDevicesServicePing401ErrorException`](../../doc/models/api-v1-sites-devices-service-ping-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesServicePing403ErrorException`](../../doc/models/api-v1-sites-devices-service-ping-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesServicePing404ErrorException`](../../doc/models/api-v1-sites-devices-service-ping-404-error-exception.md) |


# Get Site Ssr and Srx Routes

Get routes from the Device. The output will be available through websocket. As there can be multiple command issued against the same device at the same time and the output all goes through the same websocket stream, `session` is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```
admin@labsystem1.fiedler# show bgp neighbors
BGP neighbor is 192.168.4.1, remote AS 4200000001, local AS 4200000128, external
link
  BGP version 4, remote router ID 1.1.1.1
  BGP state = Established, up for 00:27:25
  Last read 00:00:25, hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 90, keepalive interval is 30 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    Route refresh: advertised and received(old &amp; new)
    Address family IPv4 Unicast: advertised and received
    Graceful Restart Capabilty: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
        ...
```

```python
def get_site_ssr_and_srx_routes(self,
                               site_id,
                               device_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesShowRouteRequest`](../../doc/models/api-v1-sites-devices-show-route-request.md) | Body, Optional | all attributes are optional |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesShowRouteRequest(
    neighbor='192.168.4.1',
    prefix='192.168.0.5/30',
    protocol='bgp',
    route=RouteEnum.ADVERTISED,
    vrf_name='default'
)

result = sites_devices_wan_controller.get_site_ssr_and_srx_routes(
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
| 401 | Unauthorized | [`ApiV1SitesDevicesShowRoute401ErrorException`](../../doc/models/api-v1-sites-devices-show-route-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesShowRoute403ErrorException`](../../doc/models/api-v1-sites-devices-show-route-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesShowRoute404ErrorException`](../../doc/models/api-v1-sites-devices-show-route-404-error-exception.md) |


# Get Site Ssr Service Path

Get service path information of the Device. The output will be available through websocket. As there can be multiple command issued against the same device at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```
show service-path

Service    Service-route     Type              Destination  Next-Hop  Interface  Vector  Cost  Rate  Capacity        State

Web        web-route1        service-agent     4.4.4.4      1.1.1.2     lan        red     10    1    200/3000       Up*
Web        web-route1        service-agent     4.4.4.4      1.1.1.3     lan        red     10    1    200/3000       Up
Web        web-route2        service-agent     5.5.5.5      2.2.2.2     lan       blue     20    2    50/unlimited   Down
Login      <None>            BgpOverSVR        10.1.1.1     1.2.3.4     wan        red     10    3        -          Up
Login      <None>            BgpOverSVR        11.1.1.1     1.2.3.4     wan        red     10    1        -          Up
App1       <None>            Routed                -           -         -          -      -     -        -          -
App1       learned-routed    Routed                -           -         -          -      -     -        -          -
```

```python
def get_site_ssr_service_path(self,
                             site_id,
                             device_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesShowServicePathRequest`](../../doc/models/api-v1-sites-devices-show-service-path-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesShowServicePathRequest(
    node=NodeEnum.NODE0,
    service_name='any'
)

result = sites_devices_wan_controller.get_site_ssr_service_path(
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
| 401 | Unauthorized | [`ApiV1SitesDevicesShowServicePath401ErrorException`](../../doc/models/api-v1-sites-devices-show-service-path-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesShowServicePath403ErrorException`](../../doc/models/api-v1-sites-devices-show-service-path-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesShowServicePath404ErrorException`](../../doc/models/api-v1-sites-devices-show-service-path-404-error-exception.md) |


# Get Site Ssr and Srx Sessions

Get active sessions passing through the Device. The output will be available through websocket. As there can be multiple command issued against the same device at the same time and the output all goes through the same websocket stream, session is introduced for demux.

#### Subscribe to Device Command outputs

`WS /api-ws/v1/stream`

```json
{
    "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
}
```

##### Example output from ws stream

```
admin@ssr.node# show sessions
Fri 2020-04-17 16:55:34 UTC

Node: node1

====================================== ===== ============= =========== ========== ====== ======= ================= ========== ================= =========== ================= ========== =================== ========= =================
 Session Id                             Dir   Service       Tenant      Dev Name   VLAN   Proto   Src IP            Src Port   Dest IP           Dest Port   NAT IP            NAT Port   Payload Encrypted   Timeout   Uptime
====================================== ===== ============= =========== ========== ====== ======= ================= ========== ================= =========== ================= ========== =================== ========= =================
 01187fb8-765a-45e5-ae90-37d77f15e292   fwd   Internet      lanSubnet   lan           0   udp     192.168.0.28         44674   35.166.173.18          9930   96.230.191.130       19569   false                   154   0 days  0:00:28
 01187fb8-765a-45e5-ae90-37d77f15e292   rev   Internet      lanSubnet   wan           0   udp     35.166.173.18         9930   96.230.191.130        19569   0.0.0.0                  0   false                   154   0 days  0:00:28
 0859a4ae-bcff-4aa6-b812-79a5236a6c13   fwd   Internet      lanSubnet   lan           0   tcp     192.168.0.41         60843   17.249.171.246          443   96.230.191.130       51941   false                     2   0 days  0:00:10

```

```python
def get_site_ssr_and_srx_sessions(self,
                                 site_id,
                                 device_id,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesShowSessionRequest`](../../doc/models/api-v1-sites-devices-show-session-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = 'device_id6'

body = ApiV1SitesDevicesShowSessionRequest(
    node=Node8Enum.NODE0,
    service_name='any'
)

result = sites_devices_wan_controller.get_site_ssr_and_srx_sessions(
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
| 401 | Unauthorized | [`ApiV1SitesDevicesShowSession401ErrorException`](../../doc/models/api-v1-sites-devices-show-session-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesShowSession403ErrorException`](../../doc/models/api-v1-sites-devices-show-session-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesShowSession404ErrorException`](../../doc/models/api-v1-sites-devices-show-session-404-error-exception.md) |

