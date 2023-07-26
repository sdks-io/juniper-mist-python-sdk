# Sites Alarms

```python
sites_alarms_controller = client.sites_alarms
```

## Class Name

`SitesAlarmsController`

## Methods

* [Multi Ack Site Alarms](../../doc/controllers/sites-alarms.md#multi-ack-site-alarms)
* [Ack Site All Alarms](../../doc/controllers/sites-alarms.md#ack-site-all-alarms)
* [Count Site Alarms](../../doc/controllers/sites-alarms.md#count-site-alarms)
* [Search Site Alarms](../../doc/controllers/sites-alarms.md#search-site-alarms)
* [Multi Unack Site Alarms](../../doc/controllers/sites-alarms.md#multi-unack-site-alarms)
* [Unack Site All Arlarms](../../doc/controllers/sites-alarms.md#unack-site-all-arlarms)
* [Ack Site Alarm](../../doc/controllers/sites-alarms.md#ack-site-alarm)
* [Unack Site Alarm](../../doc/controllers/sites-alarms.md#unack-site-alarm)


# Multi Ack Site Alarms

Ack multiple Site Alarms

```python
def multi_ack_site_alarms(self,
                         site_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesAlarmsAckRequest`](../../doc/models/api-v1-sites-alarms-ack-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesAlarmsAckRequest(
    alarm_ids=[
        'ccb8c94d-ca56-4075-932f-1f2ab444ff2c',
        '98ff4a3d-ec9b-4138-a42e-54fc3335179d'
    ],
    note='maintenance window'
)

result = sites_alarms_controller.multi_ack_site_alarms(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsAck401ErrorException`](../../doc/models/api-v1-sites-alarms-ack-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsAck403ErrorException`](../../doc/models/api-v1-sites-alarms-ack-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsAck404ErrorException`](../../doc/models/api-v1-sites-alarms-ack-404-error-exception.md) |


# Ack Site All Alarms

Ack all Site Alarms

**N.B.**: Batch size for multiple alarm ack and unack has to be less or or equal to 1000.

```python
def ack_site_all_alarms(self,
                       site_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Note`](../../doc/models/note.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Note(
    note='string'
)

result = sites_alarms_controller.ack_site_all_alarms(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsAckAll401ErrorException`](../../doc/models/api-v1-sites-alarms-ack-all-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsAckAll403ErrorException`](../../doc/models/api-v1-sites-alarms-ack-all-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsAckAll404ErrorException`](../../doc/models/api-v1-sites-alarms-ack-all-404-error-exception.md) |


# Count Site Alarms

Count Site Alarms

```python
def count_site_alarms(self,
                     site_id,
                     distinct='type',
                     ack_admin_name=None,
                     acked=None,
                     mtype=None,
                     severity=None,
                     group=None,
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
| `distinct` | [`Distinct3Enum`](../../doc/models/distinct-3-enum.md) | Query, Optional | Group by and count the alarms by some distinct field<br>**Default**: `'type'` |
| `ack_admin_name` | `string` | Query, Optional | Name of the admins who have acked the alarms; accepts multiple values separated by comma |
| `acked` | `bool` | Query, Optional | - |
| `mtype` | `string` | Query, Optional | Key-name of the alarms; accepts multiple values separated by comma |
| `severity` | `string` | Query, Optional | Alarm severity; accepts multiple values separated by comma |
| `group` | `string` | Query, Optional | Alarm group name; accepts multiple values separated by comma |
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

distinct = Distinct3Enum.ENUM_TYPE

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_alarms_controller.count_site_alarms(
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
| 401 | Unauthorized | [`ApiV1SitesAlarmsCount401ErrorException`](../../doc/models/api-v1-sites-alarms-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsCount403ErrorException`](../../doc/models/api-v1-sites-alarms-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsCount404ErrorException`](../../doc/models/api-v1-sites-alarms-count-404-error-exception.md) |


# Search Site Alarms

Search Site Alarms

```python
def search_site_alarms(self,
                      site_id,
                      mtype=None,
                      ack_admin_name=None,
                      acked=None,
                      severity=None,
                      group=None,
                      limit=100,
                      start=0,
                      end=0,
                      duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | `string` | Query, Optional | Key-name of the alarms; accepts multiple values separated by comma |
| `ack_admin_name` | `string` | Query, Optional | Name of the admins who have acked the alarms; accepts multiple values separated by comma |
| `acked` | `bool` | Query, Optional | - |
| `severity` | `string` | Query, Optional | Alarm severity; accepts multiple values separated by comma |
| `group` | `string` | Query, Optional | Alarm group name; accepts multiple values separated by comma |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`AlarmsSearch`](../../doc/models/alarms-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_alarms_controller.search_site_alarms(
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
  "next": "string",
  "results": [
    {
      "ack_admin_id": "6603c94c-eaf9-4014-9edf-b9f8eed6b183",
      "ack_admin_name": "string",
      "acked": true,
      "acked_time": 0,
      "aps": [
        "string"
      ],
      "bssids": [
        "string"
      ],
      "count": 0,
      "gateways": [
        "string"
      ],
      "group": "string",
      "hostnames": [
        "string"
      ],
      "id": "483f6eca-6276-4993-bfeb-56cbbbba6f08",
      "last_seen": 0,
      "note": "string",
      "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
      "severity": "string",
      "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
      "ssids": [
        "string"
      ],
      "switches": [
        "string"
      ],
      "timestamp": 0,
      "type": "string"
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
| 401 | Unauthorized | [`ApiV1SitesAlarmsSearch401ErrorException`](../../doc/models/api-v1-sites-alarms-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsSearch403ErrorException`](../../doc/models/api-v1-sites-alarms-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsSearch404ErrorException`](../../doc/models/api-v1-sites-alarms-search-404-error-exception.md) |


# Multi Unack Site Alarms

Unack multiple Site Alarms

```python
def multi_unack_site_alarms(self,
                           site_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesAlarmsUnackRequest`](../../doc/models/api-v1-sites-alarms-unack-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesAlarmsUnackRequest(
    alarm_ids=[
        'ccb8c94d-ca56-4075-932f-1f2ab444ff2c',
        '98ff4a3d-ec9b-4138-a42e-54fc3335179d'
    ],
    note='maintenance window'
)

result = sites_alarms_controller.multi_unack_site_alarms(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsUnack401ErrorException`](../../doc/models/api-v1-sites-alarms-unack-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsUnack403ErrorException`](../../doc/models/api-v1-sites-alarms-unack-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsUnack404ErrorException`](../../doc/models/api-v1-sites-alarms-unack-404-error-exception.md) |


# Unack Site All Arlarms

Unack all Site Alarms

**N.B.**: Batch size for multiple alarm ack and unack has to be less or or equal to 1000.

```python
def unack_site_all_arlarms(self,
                          site_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Note`](../../doc/models/note.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Note(
    note='maintenance window'
)

result = sites_alarms_controller.unack_site_all_arlarms(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsUnackAll401ErrorException`](../../doc/models/api-v1-sites-alarms-unack-all-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsUnackAll403ErrorException`](../../doc/models/api-v1-sites-alarms-unack-all-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsUnackAll404ErrorException`](../../doc/models/api-v1-sites-alarms-unack-all-404-error-exception.md) |


# Ack Site Alarm

Ack Site Alarm

```python
def ack_site_alarm(self,
                  site_id,
                  alarm_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `alarm_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Note`](../../doc/models/note.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

alarm_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Note(
    note='maintenance window'
)

result = sites_alarms_controller.ack_site_alarm(
    site_id,
    alarm_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsAck401ErrorException`](../../doc/models/api-v1-sites-alarms-ack-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsAck403ErrorException`](../../doc/models/api-v1-sites-alarms-ack-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsAck404ErrorException`](../../doc/models/api-v1-sites-alarms-ack-404-error-exception.md) |


# Unack Site Alarm

Unack Site Alarm

```python
def unack_site_alarm(self,
                    site_id,
                    alarm_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `alarm_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Note`](../../doc/models/note.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

alarm_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Note(
    note='maintenance window'
)

result = sites_alarms_controller.unack_site_alarm(
    site_id,
    alarm_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAlarmsUnack401ErrorException`](../../doc/models/api-v1-sites-alarms-unack-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAlarmsUnack403ErrorException`](../../doc/models/api-v1-sites-alarms-unack-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAlarmsUnack404ErrorException`](../../doc/models/api-v1-sites-alarms-unack-404-error-exception.md) |

