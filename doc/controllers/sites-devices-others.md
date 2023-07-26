# Sites Devices Others

```python
sites_devices_others_controller = client.sites_devices_others
```

## Class Name

`SitesDevicesOthersController`

## Methods

* [List Site Other Devices](../../doc/controllers/sites-devices-others.md#list-site-other-devices)
* [Count Site Other Devices Events](../../doc/controllers/sites-devices-others.md#count-site-other-devices-events)
* [Search Site Other Devices Events](../../doc/controllers/sites-devices-others.md#search-site-other-devices-events)


# List Site Other Devices

Get List of Site other devices (3rd party devices)

```python
def list_site_other_devices(self,
                           site_id,
                           vendor=None,
                           mac=None,
                           serial=None,
                           model=None,
                           name=None,
                           page=1,
                           limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `vendor` | `string` | Query, Optional | - |
| `mac` | `string` | Query, Optional | - |
| `serial` | `string` | Query, Optional | - |
| `model` | `string` | Query, Optional | - |
| `name` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List of DeviceOther`](../../doc/models/device-other.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

result = sites_devices_others_controller.list_site_other_devices(
    site_id,
    page,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 1676983730,
    "device_mac": "001122334455",
    "id": "ae9dee49-69e7-4710-a114-5b827a777738",
    "mac": "5c5b35000018",
    "model": "AP41",
    "modified_time": 1676983730,
    "name": "hallway",
    "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
    "serial": "FXLH2015150025",
    "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
    "vendor": "cradlepoint"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesOtherdevices401ErrorException`](../../doc/models/api-v1-sites-otherdevices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesOtherdevices403ErrorException`](../../doc/models/api-v1-sites-otherdevices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesOtherdevices404ErrorException`](../../doc/models/api-v1-sites-otherdevices-404-error-exception.md) |


# Count Site Other Devices Events

Count Site OtherDevices Events

```python
def count_site_other_devices_events(self,
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
| `distinct` | [`Distinct13Enum`](../../doc/models/distinct-13-enum.md) | Query, Optional | **Default**: `'mac'` |
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

distinct = Distinct13Enum.MAC

start = 0

end = 0

duration = '10m'

limit = 100

page = 1

result = sites_devices_others_controller.count_site_other_devices_events(
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
| 401 | Unauthorized | [`ApiV1SitesOtherdevicesEventsCount401ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesOtherdevicesEventsCount403ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesOtherdevicesEventsCount404ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-count-404-error-exception.md) |


# Search Site Other Devices Events

Search Site OtherDevices Events

```python
def search_site_other_devices_events(self,
                                    site_id,
                                    mac=None,
                                    device_mac=None,
                                    vendor=None,
                                    mtype=None,
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
| `mac` | `string` | Query, Optional | mac |
| `device_mac` | `string` | Query, Optional | mac of attached device |
| `vendor` | `string` | Query, Optional | vendor name |
| `mtype` | `string` | Query, Optional | event type |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`EventsOtherDevicesSearch`](../../doc/models/events-other-devices-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

limit = 100

page = 1

result = sites_devices_others_controller.search_site_other_devices_events(
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
    "device_mac": "string",
    "mac": "5c5b351e13b5",
    "org_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862a",
    "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
    "text": "Plugged: The Internal 5GB (SIM1) has been inserted into Internal 1.",
    "timestamp": 547235620.89,
    "type": "CELLULAR_EDGE_MODEM_WAN_PLUGGED",
    "vendor": "cradlepoint"
  },
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesOtherdevicesEventsSearch401ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesOtherdevicesEventsSearch403ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesOtherdevicesEventsSearch404ErrorException`](../../doc/models/api-v1-sites-otherdevices-events-search-404-error-exception.md) |

