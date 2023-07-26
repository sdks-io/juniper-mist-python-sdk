# Sites Clients-Wireless

```python
sites_clients_wireless_controller = client.sites_clients_wireless
```

## Class Name

`SitesClientsWirelessController`

## Methods

* [Count Site Wireless Clients](../../doc/controllers/sites-clients-wireless.md#count-site-wireless-clients)
* [Disconnect Site Multiple Clients](../../doc/controllers/sites-clients-wireless.md#disconnect-site-multiple-clients)
* [Count Site Wireless Clients Events](../../doc/controllers/sites-clients-wireless.md#count-site-wireless-clients-events)
* [Search Site Wireless Clients Events](../../doc/controllers/sites-clients-wireless.md#search-site-wireless-clients-events)
* [Search Site Wireless Clients](../../doc/controllers/sites-clients-wireless.md#search-site-wireless-clients)
* [Count Site Wireless Client Sessions](../../doc/controllers/sites-clients-wireless.md#count-site-wireless-client-sessions)
* [Search Site Wireless Client Sessions](../../doc/controllers/sites-clients-wireless.md#search-site-wireless-client-sessions)
* [Unauthorize Site Multiple Clients](../../doc/controllers/sites-clients-wireless.md#unauthorize-site-multiple-clients)
* [Disconnect Site Wireless Client](../../doc/controllers/sites-clients-wireless.md#disconnect-site-wireless-client)
* [Get Site Events for Client](../../doc/controllers/sites-clients-wireless.md#get-site-events-for-client)
* [Unauthorize Site Wireless Client](../../doc/controllers/sites-clients-wireless.md#unauthorize-site-wireless-client)


# Count Site Wireless Clients

Count by Distinct Attributes of Clients

```python
def count_site_wireless_clients(self,
                               site_id,
                               distinct,
                               ssid=None,
                               ap=None,
                               ip_address=None,
                               vlan=None,
                               hostname=None,
                               os=None,
                               model=None,
                               device=None,
                               page=1,
                               limit=100,
                               start=0,
                               end=0,
                               duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct5Enum`](../../doc/models/distinct-5-enum.md) | Query, Required | - |
| `ssid` | `string` | Query, Optional | - |
| `ap` | `string` | Query, Optional | - |
| `ip_address` | `string` | Query, Optional | - |
| `vlan` | `string` | Query, Optional | - |
| `hostname` | `string` | Query, Optional | - |
| `os` | `string` | Query, Optional | - |
| `model` | `string` | Query, Optional | - |
| `device` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct5Enum.HOSTNAME

ip_address = '192.168.1.1'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.count_site_wireless_clients(
    site_id,
    distinct,
    ip_address,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsCount401ErrorException`](../../doc/models/api-v1-sites-clients-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsCount403ErrorException`](../../doc/models/api-v1-sites-clients-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsCount404ErrorException`](../../doc/models/api-v1-sites-clients-count-404-error-exception.md) |


# Disconnect Site Multiple Clients

To unauthorize multiple clients

```python
def disconnect_site_multiple_clients(self,
                                    site_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | `List of string` | Body, Optional | Request Body<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = [
    '683b679ac024'
]

result = sites_clients_wireless_controller.disconnect_site_multiple_clients(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsDisconnect401ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsDisconnect403ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsDisconnect404ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-404-error-exception.md) |


# Count Site Wireless Clients Events

Count by Distinct Attributes of Client-Events

```python
def count_site_wireless_clients_events(self,
                                      site_id,
                                      distinct=None,
                                      mtype=None,
                                      reason_code=None,
                                      ssid=None,
                                      ap=None,
                                      proto=None,
                                      band=None,
                                      wlan_id=None,
                                      page=1,
                                      limit=100,
                                      start=0,
                                      end=0,
                                      duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct6Enum`](../../doc/models/distinct-6-enum.md) | Query, Optional | type / proto / band / channel / wlan_id / ssid |
| `mtype` | `string` | Query, Optional | event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE |
| `reason_code` | `int` | Query, Optional | for assoc/disassoc events |
| `ssid` | `string` | Query, Optional | SSID Name |
| `ap` | `string` | Query, Optional | AP MAC |
| `proto` | [`Proto1Enum`](../../doc/models/proto-1-enum.md) | Query, Optional | 802.11 standard |
| `band` | [`Band7Enum`](../../doc/models/band-7-enum.md) | Query, Optional | 24 / 5 |
| `wlan_id` | `string` | Query, Optional | wlan_id |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct6Enum.ENUM_TYPE

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.count_site_wireless_clients_events(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsEventsCount401ErrorException`](../../doc/models/api-v1-sites-clients-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsEventsCount403ErrorException`](../../doc/models/api-v1-sites-clients-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsEventsCount404ErrorException`](../../doc/models/api-v1-sites-clients-events-count-404-error-exception.md) |


# Search Site Wireless Clients Events

Get Site Clients Events

```python
def search_site_wireless_clients_events(self,
                                       site_id,
                                       mtype=None,
                                       reason_code=None,
                                       ssid=None,
                                       ap=None,
                                       proto=None,
                                       band=None,
                                       wlan_id=None,
                                       limit=100,
                                       start=0,
                                       end=0,
                                       duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | `string` | Query, Optional | event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE |
| `reason_code` | `int` | Query, Optional | for assoc/disassoc events |
| `ssid` | `string` | Query, Optional | SSID Name |
| `ap` | `string` | Query, Optional | AP MAC |
| `proto` | [`Proto1Enum`](../../doc/models/proto-1-enum.md) | Query, Optional | 802.11 standard |
| `band` | [`Band7Enum`](../../doc/models/band-7-enum.md) | Query, Optional | 24 / 5 |
| `wlan_id` | `string` | Query, Optional | wlan_id |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`EventsSearch`](../../doc/models/events-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.search_site_wireless_clients_events(
    site_id,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "limit": 0,
  "results": [
    {
      "ap": "string",
      "band": "24",
      "bssid": "string",
      "channel": 0,
      "proto": "a",
      "ssid": "string",
      "text": "string",
      "timestamp": 0,
      "type": "string",
      "type_code": 0,
      "wlan_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsEventsSearch401ErrorException`](../../doc/models/api-v1-sites-clients-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsEventsSearch403ErrorException`](../../doc/models/api-v1-sites-clients-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsEventsSearch404ErrorException`](../../doc/models/api-v1-sites-clients-events-search-404-error-exception.md) |


# Search Site Wireless Clients

Search Wireless Clients

**NOTE**: fuzzy logic can be used with ‘*’, supported filters: mac, hostname, device, os, model. E.g. /clients/search?device=Mac*&hostname=jerry

```python
def search_site_wireless_clients(self,
                                site_id,
                                mac=None,
                                ip_address=None,
                                hostname=None,
                                device=None,
                                os=None,
                                model=None,
                                ap=None,
                                ssid=None,
                                text=None,
                                limit=100,
                                start=0,
                                end=0,
                                duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mac` | `string` | Query, Optional | partial / full MAC address |
| `ip_address` | `string` | Query, Optional | - |
| `hostname` | `string` | Query, Optional | partial / full hostname |
| `device` | `string` | Query, Optional | device type, e.g. Mac, Nvidia, iPhone |
| `os` | `string` | Query, Optional | os, e.g. Sierra, Yosemite, Windows 10 |
| `model` | `string` | Query, Optional | model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM” |
| `ap` | `string` | Query, Optional | AP mac where the client has connected to |
| `ssid` | `string` | Query, Optional | - |
| `text` | `string` | Query, Optional | partial / full MAC address, hostname, username or ip |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ClientsSearch`](../../doc/models/clients-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

ip_address = '192.168.1.1'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.search_site_wireless_clients(
    site_id,
    ip_address,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "limit": 0,
  "results": [
    {
      "ap": "string",
      "band": "24",
      "bssid": "string",
      "channel": 0,
      "proto": "a",
      "ssid": "string",
      "text": "string",
      "timestamp": 0,
      "type": "string",
      "type_code": 0,
      "wlan_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsSearch401ErrorException`](../../doc/models/api-v1-sites-clients-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsSearch403ErrorException`](../../doc/models/api-v1-sites-clients-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsSearch404ErrorException`](../../doc/models/api-v1-sites-clients-search-404-error-exception.md) |


# Count Site Wireless Client Sessions

Count by Distinct Attributes of Client Sessions

```python
def count_site_wireless_client_sessions(self,
                                       site_id,
                                       distinct='mac',
                                       ap=None,
                                       band=None,
                                       client_family=None,
                                       client_manufacture=None,
                                       client_model=None,
                                       client_os=None,
                                       ssid=None,
                                       wlan_id=None,
                                       page=1,
                                       limit=100,
                                       start=0,
                                       end=0,
                                       duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct7Enum`](../../doc/models/distinct-7-enum.md) | Query, Optional | **Default**: `'mac'` |
| `ap` | `string` | Query, Optional | AP MAC |
| `band` | `string` | Query, Optional | 24 /5 |
| `client_family` | `string` | Query, Optional | E.g. “Mac”, “iPhone”, “Apple watch” |
| `client_manufacture` | `string` | Query, Optional | E.g. “Apple” |
| `client_model` | `string` | Query, Optional | E.g. “8+”, “XS” |
| `client_os` | `string` | Query, Optional | E.g. “Mojave”, “Windows 10”, “Linux” |
| `ssid` | `string` | Query, Optional | SSID |
| `wlan_id` | `string` | Query, Optional | wlan_id |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct7Enum.MAC

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.count_site_wireless_client_sessions(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsSessionsCount401ErrorException`](../../doc/models/api-v1-sites-clients-sessions-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsSessionsCount403ErrorException`](../../doc/models/api-v1-sites-clients-sessions-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsSessionsCount404ErrorException`](../../doc/models/api-v1-sites-clients-sessions-count-404-error-exception.md) |


# Search Site Wireless Client Sessions

Search Client Sessions

```python
def search_site_wireless_client_sessions(self,
                                        site_id,
                                        ap=None,
                                        band=None,
                                        client_family=None,
                                        client_manufacture=None,
                                        client_model=None,
                                        client_username=None,
                                        client_os=None,
                                        ssid=None,
                                        wlan_id=None,
                                        psk_id=None,
                                        psk_name=None,
                                        limit=100,
                                        start=0,
                                        end=0,
                                        duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `ap` | `string` | Query, Optional | AP MAC |
| `band` | [`Band7Enum`](../../doc/models/band-7-enum.md) | Query, Optional | 5 / 24 |
| `client_family` | `string` | Query, Optional | E.g. “Mac”, “iPhone”, “Apple watch” |
| `client_manufacture` | `string` | Query, Optional | E.g. “Apple” |
| `client_model` | `string` | Query, Optional | E.g. “8+”, “XS” |
| `client_username` | `string` | Query, Optional | Username |
| `client_os` | `string` | Query, Optional | E.g. “Mojave”, “Windows 10”, “Linux” |
| `ssid` | `string` | Query, Optional | SSID |
| `wlan_id` | `string` | Query, Optional | wlan_id |
| `psk_id` | `uuid\|string` | Query, Optional | PSK ID |
| `psk_name` | `string` | Query, Optional | PSK Name |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ClientSessionsSearch`](../../doc/models/client-sessions-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

psk_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wireless_controller.search_site_wireless_client_sessions(
    site_id,
    psk_id,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1513177200,
  "limit": 10,
  "results": [
    {
      "ap": "5c5b350e0262",
      "band": "5",
      "client_manufacture": "Apple",
      "connect": 1565208388,
      "disconnect": 1565208448,
      "duration": 60.09423865,
      "mac": "b019c66c8348",
      "org_id": "3139f2c2-fac6-11e5-8156-0242ac110006",
      "site_id": "70e0f468-fc13-11e5-85ad-0242ac110008",
      "ssid": "Dummy WLAN 2",
      "tags": [
        "disassociate"
      ],
      "timestamp": 1565208448.662,
      "wlan_id": "99bb4c74-f954-4f36-b844-6b030faffabc"
    }
  ],
  "start": 1511967600,
  "total": 100
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsSessionsSearch401ErrorException`](../../doc/models/api-v1-sites-clients-sessions-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsSessionsSearch403ErrorException`](../../doc/models/api-v1-sites-clients-sessions-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsSessionsSearch404ErrorException`](../../doc/models/api-v1-sites-clients-sessions-search-404-error-exception.md) |


# Unauthorize Site Multiple Clients

This unauthorize clients (if they are guest) and disconnect them. From the guest’s perspective, they will see the splash page again and go through the flow (e.g. Terms of Use) again.

```python
def unauthorize_site_multiple_clients(self,
                                     site_id,
                                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | `List of string` | Body, Optional | Request Body<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = [
    '683b679ac024'
]

result = sites_clients_wireless_controller.unauthorize_site_multiple_clients(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsUnauthorize401ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsUnauthorize403ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsUnauthorize404ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-404-error-exception.md) |


# Disconnect Site Wireless Client

This disconnect a client (and it’s likely to connect back)

```python
def disconnect_site_wireless_client(self,
                                   site_id,
                                   client_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

result = sites_clients_wireless_controller.disconnect_site_wireless_client(
    site_id,
    client_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsDisconnect401ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsDisconnect403ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsDisconnect404ErrorException`](../../doc/models/api-v1-sites-clients-disconnect-404-error-exception.md) |


# Get Site Events for Client

Get the list of events for a specific client

```python
def get_site_events_for_client(self,
                              site_id,
                              client_mac,
                              mtype=None,
                              proto=None,
                              band=None,
                              channel=None,
                              wlan_id=None,
                              ssid=None,
                              start=0,
                              end=0,
                              page=1,
                              limit=100,
                              duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `mtype` | [`Type46Enum`](../../doc/models/type-46-enum.md) | Query, Optional | e.g. MARVIS_EVENT_CLIENT_DHCP_STUCK |
| `proto` | [`Proto1Enum`](../../doc/models/proto-1-enum.md) | Query, Optional | a / b / g / n / ac / ax |
| `band` | `string` | Query, Optional | 24 / 5 |
| `channel` | `string` | Query, Optional | - |
| `wlan_id` | `string` | Query, Optional | - |
| `ssid` | `string` | Query, Optional | - |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ClientEventsSearch`](../../doc/models/client-events-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

start = 0

end = 0

page = 1

limit = 100

duration = '10m'

result = sites_clients_wireless_controller.get_site_events_for_client(
    site_id,
    client_mac,
    start,
    end,
    page,
    limit,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1513176951,
  "limit": 10,
  "results": [
    {
      "ap": "5c5b350eb31b",
      "band": "5",
      "bssid": "5c5b350918f1",
      "channel": 149,
      "proto": "ac",
      "ssid": "Guest",
      "text": "Status code 0 \"Successful\" ",
      "timestamp": 1513358874.667,
      "type": "CLIENT_DNS_OK",
      "type_code": 15,
      "wlan_id": "be22bba7-8e22-e1cf-5185-b880816fe2cf"
    }
  ],
  "start": 1512572151,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsEvents401ErrorException`](../../doc/models/api-v1-sites-clients-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsEvents403ErrorException`](../../doc/models/api-v1-sites-clients-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsEvents404ErrorException`](../../doc/models/api-v1-sites-clients-events-404-error-exception.md) |


# Unauthorize Site Wireless Client

This unauthorize a client (if it’s a guest) and disconnect it. From the guest’s perspective, s/he will see the splash page again and go through the flow (e.g. Terms of Use) again.

```python
def unauthorize_site_wireless_client(self,
                                    site_id,
                                    client_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

result = sites_clients_wireless_controller.unauthorize_site_wireless_client(
    site_id,
    client_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesClientsUnauthorize401ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesClientsUnauthorize403ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesClientsUnauthorize404ErrorException`](../../doc/models/api-v1-sites-clients-unauthorize-404-error-exception.md) |

