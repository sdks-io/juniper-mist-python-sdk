# Sites Wx Tunnels

```python
sites_wx_tunnels_controller = client.sites_wx_tunnels
```

## Class Name

`SitesWxTunnelsController`

## Methods

* [List Site Wx Tunnels](../../doc/controllers/sites-wx-tunnels.md#list-site-wx-tunnels)
* [Create Site Wx Tunnel](../../doc/controllers/sites-wx-tunnels.md#create-site-wx-tunnel)
* [Delete Site Wx Tunnel](../../doc/controllers/sites-wx-tunnels.md#delete-site-wx-tunnel)
* [Get Site Wx Tunnel](../../doc/controllers/sites-wx-tunnels.md#get-site-wx-tunnel)
* [Update Site Wx Tunnel](../../doc/controllers/sites-wx-tunnels.md#update-site-wx-tunnel)


# List Site Wx Tunnels

Get List of Site WxLan Tunnels

```python
def list_site_wx_tunnels(self,
                        site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of WxlanTunnel`](../../doc/models/wxlan-tunnel.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tunnels_controller.list_site_wx_tunnels(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "dmvpn": {
      "enabled": true,
      "holding_time": 0,
      "host_routes": [
        "string"
      ]
    },
    "for_mgmt": true,
    "hello_interval": 1,
    "hello_retries": 3,
    "hostname": "string",
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "ipsec": {
      "enabled": true,
      "psk": "string123"
    },
    "is_static": true,
    "modified_time": 0,
    "mtu": 1500,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "peers": [
      "string"
    ],
    "router_id": "string",
    "secret": "string",
    "sessions": [
      {
        "ap_as_session_id": "string",
        "comment": "string",
        "enable_cookie": true,
        "ethertype": "ethernet",
        "local_session_id": 1,
        "pseudo_802-1ad_enabled": true,
        "remote_id": "string",
        "remote_session_id": 1,
        "use_ap_as_session_ids": true
      }
    ],
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "udp_port": 0,
    "use_udp": true
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtunnels401ErrorException`](../../doc/models/api-v1-sites-wxtunnels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtunnels403ErrorException`](../../doc/models/api-v1-sites-wxtunnels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtunnels404ErrorException`](../../doc/models/api-v1-sites-wxtunnels-404-error-exception.md) |


# Create Site Wx Tunnel

Create Site WxLan Tunnel

```python
def create_site_wx_tunnel(self,
                         site_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanTunnel`](../../doc/models/wxlan-tunnel.md) | Body, Optional | Request Body |

## Response Type

[`WxlanTunnel`](../../doc/models/wxlan-tunnel.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanTunnel(
    name='string',
    dmvpn=Dmvpn(
        enabled=True,
        holding_time=0,
        host_routes=[
            'string'
        ]
    ),
    for_mgmt=True,
    hello_interval=1,
    hello_retries=3,
    hostname='string',
    ipsec=Ipsec1(
        psk='string123',
        enabled=True
    ),
    is_static=True,
    mtu=0,
    peers=[
        'string'
    ],
    router_id='string',
    secret='string',
    sessions=[
        Sessions2(
            ap_as_session_id='string',
            comment='string',
            enable_cookie=True,
            ethertype=EthertypeEnum.ETHERNET,
            local_session_id=1,
            pseudo_802_1_ad_enabled=True,
            remote_id='string',
            remote_session_id=1,
            use_ap_as_session_ids=True
        )
    ],
    udp_port=0,
    use_udp=True
)

result = sites_wx_tunnels_controller.create_site_wx_tunnel(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "dmvpn": {
    "enabled": true,
    "holding_time": 0,
    "host_routes": [
      "string"
    ]
  },
  "for_mgmt": true,
  "hello_interval": 1,
  "hello_retries": 3,
  "hostname": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "ipsec": {
    "enabled": true,
    "psk": "string123"
  },
  "is_static": true,
  "modified_time": 0,
  "mtu": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "peers": [
    "string"
  ],
  "router_id": "string",
  "secret": "string",
  "sessions": [
    {
      "ap_as_session_id": "string",
      "comment": "string",
      "enable_cookie": true,
      "ethertype": "ethernet",
      "local_session_id": 1,
      "pseudo_802-1ad_enabled": true,
      "remote_id": "string",
      "remote_session_id": 1,
      "use_ap_as_session_ids": true
    }
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "udp_port": 0,
  "use_udp": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtunnels401ErrorException`](../../doc/models/api-v1-sites-wxtunnels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtunnels403ErrorException`](../../doc/models/api-v1-sites-wxtunnels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtunnels404ErrorException`](../../doc/models/api-v1-sites-wxtunnels-404-error-exception.md) |


# Delete Site Wx Tunnel

Delete Site WxLan Tunnel

```python
def delete_site_wx_tunnel(self,
                         site_id,
                         wxtunnel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtunnel_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtunnel_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tunnels_controller.delete_site_wx_tunnel(
    site_id,
    wxtunnel_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtunnels401ErrorException`](../../doc/models/api-v1-sites-wxtunnels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtunnels403ErrorException`](../../doc/models/api-v1-sites-wxtunnels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtunnels404ErrorException`](../../doc/models/api-v1-sites-wxtunnels-404-error-exception.md) |


# Get Site Wx Tunnel

Get Site WxLan tunnel Details

```python
def get_site_wx_tunnel(self,
                      site_id,
                      wxtunnel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtunnel_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`WxlanTunnel`](../../doc/models/wxlan-tunnel.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtunnel_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tunnels_controller.get_site_wx_tunnel(
    site_id,
    wxtunnel_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "dmvpn": {
    "enabled": true,
    "holding_time": 0,
    "host_routes": [
      "string"
    ]
  },
  "for_mgmt": true,
  "hello_interval": 1,
  "hello_retries": 3,
  "hostname": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "ipsec": {
    "enabled": true,
    "psk": "string123"
  },
  "is_static": true,
  "modified_time": 0,
  "mtu": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "peers": [
    "string"
  ],
  "router_id": "string",
  "secret": "string",
  "sessions": [
    {
      "ap_as_session_id": "string",
      "comment": "string",
      "enable_cookie": true,
      "ethertype": "ethernet",
      "local_session_id": 1,
      "pseudo_802-1ad_enabled": true,
      "remote_id": "string",
      "remote_session_id": 1,
      "use_ap_as_session_ids": true
    }
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "udp_port": 0,
  "use_udp": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtunnels401ErrorException`](../../doc/models/api-v1-sites-wxtunnels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtunnels403ErrorException`](../../doc/models/api-v1-sites-wxtunnels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtunnels404ErrorException`](../../doc/models/api-v1-sites-wxtunnels-404-error-exception.md) |


# Update Site Wx Tunnel

Update Site WxLan Tunnel

```python
def update_site_wx_tunnel(self,
                         site_id,
                         wxtunnel_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtunnel_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanTunnel`](../../doc/models/wxlan-tunnel.md) | Body, Optional | Request Body |

## Response Type

[`WxlanTunnel`](../../doc/models/wxlan-tunnel.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtunnel_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanTunnel(
    name='string',
    dmvpn=Dmvpn(
        enabled=True,
        holding_time=0,
        host_routes=[
            'string'
        ]
    ),
    for_mgmt=True,
    hello_interval=1,
    hello_retries=3,
    hostname='string',
    ipsec=Ipsec1(
        psk='string123',
        enabled=True
    ),
    is_static=True,
    mtu=0,
    peers=[
        'string'
    ],
    router_id='string',
    secret='string',
    sessions=[
        Sessions2(
            ap_as_session_id='string',
            comment='string',
            enable_cookie=True,
            ethertype=EthertypeEnum.ETHERNET,
            local_session_id=1,
            pseudo_802_1_ad_enabled=True,
            remote_id='string',
            remote_session_id=1,
            use_ap_as_session_ids=True
        )
    ],
    udp_port=0,
    use_udp=True
)

result = sites_wx_tunnels_controller.update_site_wx_tunnel(
    site_id,
    wxtunnel_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "dmvpn": {
    "enabled": true,
    "holding_time": 0,
    "host_routes": [
      "string"
    ]
  },
  "for_mgmt": true,
  "hello_interval": 1,
  "hello_retries": 3,
  "hostname": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "ipsec": {
    "enabled": true,
    "psk": "string123"
  },
  "is_static": true,
  "modified_time": 0,
  "mtu": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "peers": [
    "string"
  ],
  "router_id": "string",
  "secret": "string",
  "sessions": [
    {
      "ap_as_session_id": "string",
      "comment": "string",
      "enable_cookie": true,
      "ethertype": "ethernet",
      "local_session_id": 1,
      "pseudo_802-1ad_enabled": true,
      "remote_id": "string",
      "remote_session_id": 1,
      "use_ap_as_session_ids": true
    }
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "udp_port": 0,
  "use_udp": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtunnels401ErrorException`](../../doc/models/api-v1-sites-wxtunnels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtunnels403ErrorException`](../../doc/models/api-v1-sites-wxtunnels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtunnels404ErrorException`](../../doc/models/api-v1-sites-wxtunnels-404-error-exception.md) |

