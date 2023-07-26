# Sites Clients-Wan

```python
sites_clients_wan_controller = client.sites_clients_wan
```

## Class Name

`SitesClientsWanController`

## Methods

* [Count Site Wan Client Events](../../doc/controllers/sites-clients-wan.md#count-site-wan-client-events)
* [Count Site Wan Clients](../../doc/controllers/sites-clients-wan.md#count-site-wan-clients)
* [Search Site Wan Clients Events](../../doc/controllers/sites-clients-wan.md#search-site-wan-clients-events)
* [Search Site Wan Clients](../../doc/controllers/sites-clients-wan.md#search-site-wan-clients)


# Count Site Wan Client Events

Count by Distinct Attributes of Site WAN Client-Events

```python
def count_site_wan_client_events(self,
                                site_id,
                                distinct='type')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct21Enum`](../../doc/models/distinct-21-enum.md) | Query, Optional | **Default**: `'type'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct21Enum.ENUM_TYPE

result = sites_clients_wan_controller.count_site_wan_client_events(
    site_id,
    distinct
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
| 401 | Unauthorized | [`ApiV1SitesWanClientEventsCount401ErrorException`](../../doc/models/api-v1-sites-wan-client-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWanClientEventsCount403ErrorException`](../../doc/models/api-v1-sites-wan-client-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWanClientEventsCount404ErrorException`](../../doc/models/api-v1-sites-wan-client-events-count-404-error-exception.md) |


# Count Site Wan Clients

Count Site WAN Clients

```python
def count_site_wan_clients(self,
                          site_id,
                          distinct='mac',
                          start=0,
                          end=0,
                          duration='1d',
                          limit=100,
                          page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct22Enum`](../../doc/models/distinct-22-enum.md) | Query, Optional | **Default**: `'mac'` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct22Enum.MAC

start = 0

end = 0

duration = '10m'

limit = 100

page = 1

result = sites_clients_wan_controller.count_site_wan_clients(
    site_id,
    distinct,
    start,
    end,
    duration,
    limit,
    page
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
| 401 | Unauthorized | [`ApiV1SitesWanClientsCount401ErrorException`](../../doc/models/api-v1-sites-wan-clients-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWanClientsCount403ErrorException`](../../doc/models/api-v1-sites-wan-clients-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWanClientsCount404ErrorException`](../../doc/models/api-v1-sites-wan-clients-count-404-error-exception.md) |


# Search Site Wan Clients Events

Search Site WAN Client Events

```python
def search_site_wan_clients_events(self,
                                  site_id,
                                  mtype=None,
                                  mac=None,
                                  hostname=None,
                                  ip=None,
                                  mfg=None,
                                  start=0,
                                  end=0,
                                  duration='1d',
                                  limit=100,
                                  page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | `string` | Query, Optional | Event type, e.g. CLIENT_IP_ASSIGNED, CLIENT_IP_RENEWED, CLIENT_IP_EXPIRED |
| `mac` | `string` | Query, Optional | partial / full MAC address |
| `hostname` | `string` | Query, Optional | partial / full hostname |
| `ip` | `string` | Query, Optional | client IP |
| `mfg` | `string` | Query, Optional | Manufacture |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`WanClientEventsSearch`](../../doc/models/wan-client-events-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

limit = 100

page = 1

result = sites_clients_wan_controller.search_site_wan_clients_events(
    site_id,
    start,
    end,
    duration,
    limit,
    page
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "limit": 0,
  "results": {
    "When": "2022-12-31T23:59:59.293Z",
    "ev_type": "CLIENT_IP_ASSIGNED",
    "metadata": {},
    "org_id": "b0b9f142-aaba-11e6-aafc-0242ac110002",
    "random_mac": true,
    "site_id": "fc656275-b157-43fd-b922-5f4f341c19bf",
    "text": "DHCP Ack IP 192.168.88.216",
    "wcid": "62bbfb75-10d8-49d1-dec7-d2df91624287"
  },
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWanClientsEventsSearch401ErrorException`](../../doc/models/api-v1-sites-wan-clients-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWanClientsEventsSearch403ErrorException`](../../doc/models/api-v1-sites-wan-clients-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWanClientsEventsSearch404ErrorException`](../../doc/models/api-v1-sites-wan-clients-events-search-404-error-exception.md) |


# Search Site Wan Clients

Search Site WAN Clients

```python
def search_site_wan_clients(self,
                           site_id,
                           mac=None,
                           hostname=None,
                           ip=None,
                           mfg=None,
                           start=0,
                           end=0,
                           duration='1d',
                           limit=100,
                           page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mac` | `string` | Query, Optional | partial / full MAC address |
| `hostname` | `string` | Query, Optional | partial / full hostname |
| `ip` | `string` | Query, Optional | client IP |
| `mfg` | `string` | Query, Optional | Manufacture |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`WanClientsSearch`](../../doc/models/wan-clients-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

limit = 100

page = 1

result = sites_clients_wan_controller.search_site_wan_clients(
    site_id,
    start,
    end,
    duration,
    limit,
    page
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "limit": 0,
  "results": {
    "When": "2022-12-31T23:59:43.497+0000",
    "hostname": [
      "sonoszp"
    ],
    "ip": [
      "192.168.1.139"
    ],
    "last_hostname": "sonoszp",
    "last_ip": "192.168.1.139",
    "mfg": "Sonos",
    "org_id": "b4e16c72-d50e-4c03-a952-a3217e231e2c",
    "site_id": "f688779c-e335-4f88-8d7c-9c5e9964528b",
    "wcid": "8bbe7389-212b-c65d-2208-00fab2017936"
  },
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWanClientsSearch401ErrorException`](../../doc/models/api-v1-sites-wan-clients-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWanClientsSearch403ErrorException`](../../doc/models/api-v1-sites-wan-clients-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWanClientsSearch404ErrorException`](../../doc/models/api-v1-sites-wan-clients-search-404-error-exception.md) |

