# Msps Marvis

```python
msps_marvis_controller = client.msps_marvis
```

## Class Name

`MspsMarvisController`


# Count Msps Marvis Actions

Count Marvis actions

```python
def count_msps_marvis_actions(self,
                             msp_id,
                             distinct='org_id',
                             limit=100,
                             page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct1Enum`](../../doc/models/distinct-1-enum.md) | Query, Optional | **Default**: `'org_id'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |

## Response Type

[`ApiV1MspsSuggestionCountResponse`](../../doc/models/api-v1-msps-suggestion-count-response.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct1Enum.ORG_ID

limit = 100

page = 1

result = msps_marvis_controller.count_msps_marvis_actions(
    msp_id,
    distinct,
    limit,
    page
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "status",
  "limit": 1000,
  "results": [
    {
      "count": 24,
      "status": "002e176a-0000-000-1111-002e208b20e1"
    },
    {
      "count": 12,
      "status": "2d3f176a-0000-000-2222-002e208f176a"
    },
    {
      "count": 15,
      "status": "08b2176a-0000-000-3333-002e208b2d3f"
    }
  ],
  "total": 3
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSuggestionCount401ErrorException`](../../doc/models/api-v1-msps-suggestion-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSuggestionCount403ErrorException`](../../doc/models/api-v1-msps-suggestion-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSuggestionCount404ErrorException`](../../doc/models/api-v1-msps-suggestion-count-404-error-exception.md) |

