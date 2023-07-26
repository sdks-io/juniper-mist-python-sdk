# Sites Clients-Wired

```python
sites_clients_wired_controller = client.sites_clients_wired
```

## Class Name

`SitesClientsWiredController`

## Methods

* [Count Site Wired Clients](../../doc/controllers/sites-clients-wired.md#count-site-wired-clients)
* [Search Site Wired Clients](../../doc/controllers/sites-clients-wired.md#search-site-wired-clients)


# Count Site Wired Clients

Count by Distinct Attributes of Clients

```python
def count_site_wired_clients(self,
                            site_id,
                            distinct='mac',
                            mac=None,
                            device_mac=None,
                            port_id=None,
                            vlan=None,
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
| `distinct` | [`Distinct23Enum`](../../doc/models/distinct-23-enum.md) | Query, Optional | **Default**: `'mac'` |
| `mac` | `string` | Query, Optional | client mac |
| `device_mac` | `string` | Query, Optional | device mac |
| `port_id` | `string` | Query, Optional | port id |
| `vlan` | `string` | Query, Optional | vlan |
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

distinct = Distinct23Enum.MAC

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wired_controller.count_site_wired_clients(
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
| 401 | Unauthorized | [`ApiV1SitesWiredClientsCount401ErrorException`](../../doc/models/api-v1-sites-wired-clients-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWiredClientsCount403ErrorException`](../../doc/models/api-v1-sites-wired-clients-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWiredClientsCount404ErrorException`](../../doc/models/api-v1-sites-wired-clients-count-404-error-exception.md) |


# Search Site Wired Clients

Search Wired Clients

```python
def search_site_wired_clients(self,
                             site_id,
                             device_mac=None,
                             mac=None,
                             ip=None,
                             port_id=None,
                             vlan=None,
                             ip_address=None,
                             manufacture=None,
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
| `device_mac` | `string` | Query, Optional | device mac |
| `mac` | `string` | Query, Optional | client mac |
| `ip` | `string` | Query, Optional | client ip |
| `port_id` | `string` | Query, Optional | port id |
| `vlan` | `string` | Query, Optional | vlan |
| `ip_address` | `string` | Query, Optional | - |
| `manufacture` | `string` | Query, Optional | manufacture |
| `text` | `string` | Query, Optional | single entry of hostname/mac |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`WiredClientsSearch`](../../doc/models/wired-clients-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

ip_address = '192.168.1.1'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_clients_wired_controller.search_site_wired_clients(
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
  "end": 1648529800.8221116,
  "limit": 1000,
  "results": [
    {
      "device_mac": [
        "001122334455"
      ],
      "device_mac_port": [
        {
          "device_mac": "001122334455",
          "ip": "",
          "port_id": "et-0/0/1",
          "port_parent": "",
          "start": "2020-12-10T00:07:36.262+0000",
          "vlan": 1,
          "when": "2022-03-29T04:56:05.172+0000"
        }
      ],
      "ip": [
        "11.216.202.61"
      ],
      "mac": "112233445566",
      "org_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "port_id": [
        "et-0/0/1"
      ],
      "site_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "timestamp": 1571174567.807,
      "vlan": [
        0,
        1001
      ]
    }
  ],
  "start": 1648443400.8221116,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWiredClientsSearch401ErrorException`](../../doc/models/api-v1-sites-wired-clients-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWiredClientsSearch403ErrorException`](../../doc/models/api-v1-sites-wired-clients-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWiredClientsSearch404ErrorException`](../../doc/models/api-v1-sites-wired-clients-search-404-error-exception.md) |

