# Msps Tickets

```python
msps_tickets_controller = client.msps_tickets
```

## Class Name

`MspsTicketsController`

## Methods

* [List Msp Tickets](../../doc/controllers/msps-tickets.md#list-msp-tickets)
* [Count Msp Tickets](../../doc/controllers/msps-tickets.md#count-msp-tickets)


# List Msp Tickets

Get List of Tickets of a MSP

```python
def list_msp_tickets(self,
                    msp_id,
                    start=0,
                    end=0,
                    duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of Ticket`](../../doc/models/ticket.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

result = msps_tickets_controller.list_msp_tickets(
    msp_id,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "comments": [
      {
        "attachments": [
          {
            "content_type": "string",
            "content_url": "string",
            "size": 0
          }
        ],
        "author": "string",
        "comment": "string",
        "created_at": 0
      }
    ],
    "created_at": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "requester": "string",
    "status": "open",
    "subject": "string",
    "type": "string",
    "updated_at": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsTickets401ErrorException`](../../doc/models/api-v1-msps-tickets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsTickets403ErrorException`](../../doc/models/api-v1-msps-tickets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsTickets404ErrorException`](../../doc/models/api-v1-msps-tickets-404-error-exception.md) |


# Count Msp Tickets

Count tickets

```python
def count_msp_tickets(self,
                     msp_id,
                     distinct='status')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct2Enum`](../../doc/models/distinct-2-enum.md) | Query, Optional | **Default**: `'status'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct2Enum.STATUS

result = msps_tickets_controller.count_msp_tickets(
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
| 401 | Unauthorized | [`ApiV1MspsTicketsCount401ErrorException`](../../doc/models/api-v1-msps-tickets-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsTicketsCount403ErrorException`](../../doc/models/api-v1-msps-tickets-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsTicketsCount404ErrorException`](../../doc/models/api-v1-msps-tickets-count-404-error-exception.md) |

