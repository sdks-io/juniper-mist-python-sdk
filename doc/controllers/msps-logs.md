# Msps Logs

```python
msps_logs_controller = client.msps_logs
```

## Class Name

`MspsLogsController`

## Methods

* [List Msp Logs](../../doc/controllers/msps-logs.md#list-msp-logs)
* [Count Msp Logs](../../doc/controllers/msps-logs.md#count-msp-logs)


# List Msp Logs

Get list of change logs for the current MSP

```python
def list_msp_logs(self,
                 msp_id,
                 site_id=None,
                 admin_name=None,
                 message=None,
                 sort=None,
                 start=0,
                 end=0,
                 limit=100,
                 page=1,
                 duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `site_id` | `string` | Query, Optional | site id |
| `admin_name` | `string` | Query, Optional | admin name or email |
| `message` | `string` | Query, Optional | message |
| `sort` | [`SortEnum`](../../doc/models/sort-enum.md) | Query, Optional | sort order |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`LogsSearch`](../../doc/models/logs-search.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

limit = 100

page = 1

duration = '10m'

result = msps_logs_controller.list_msp_logs(
    msp_id,
    start,
    end,
    limit,
    page,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1428954000,
  "limit": 100,
  "results": [
    {
      "admin_id": "72bfa2bd-e58a-4670-9d20-a1468f7a6f58",
      "admin_name": "test@mistsys.com",
      "id": "c6f9347b-b0a4-4a23-b927-fa9249f2ffb2",
      "message": "TEST AUDIT",
      "org_id": "469f6eca-6276-4993-bfeb-53cbbbba6f58",
      "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
      "timestamp": 1431382121
    }
  ],
  "start": 1428939600,
  "total": 135
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsLogs401ErrorException`](../../doc/models/api-v1-msps-logs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsLogs403ErrorException`](../../doc/models/api-v1-msps-logs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsLogs404ErrorException`](../../doc/models/api-v1-msps-logs-404-error-exception.md) |


# Count Msp Logs

Count by Distinct Attributes of Audit Logs

```python
def count_msp_logs(self,
                  msp_id,
                  distinct='admin_name')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`DistinctEnum`](../../doc/models/distinct-enum.md) | Query, Optional | **Default**: `'admin_name'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = DistinctEnum.ADMIN_NAME

result = msps_logs_controller.count_msp_logs(
    msp_id,
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
| 401 | Unauthorized | [`ApiV1MspsLogsCount401ErrorException`](../../doc/models/api-v1-msps-logs-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsLogsCount403ErrorException`](../../doc/models/api-v1-msps-logs-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsLogsCount404ErrorException`](../../doc/models/api-v1-msps-logs-count-404-error-exception.md) |

