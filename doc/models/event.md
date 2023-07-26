
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aps` | `List of string` | Optional | - |
| `bssids` | `List of string` | Optional | - |
| `count` | `int` | Optional | If present, represents number of events of given type occurred in current interval, default=1 |
| `event_id` | `uuid\|string` | Optional | event id |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Required | - |
| `last_seen` | `float` | Required | - |
| `org_id` | `uuid\|string` | Required | org id |
| `site_id` | `uuid\|string` | Required | site id |
| `ssids` | `List of string` | Optional | - |
| `timestamp` | `int` | Required | - |
| `mtype` | `string` | Required | event type |
| `update` | `bool` | Optional | If presents, represents that this is an update to event with given id sent earlier. default=false |

## Example (as JSON)

```json
{
  "aps": [
    "aps1",
    "aps2"
  ],
  "bssids": [
    "bssids4"
  ],
  "count": 60,
  "event_id": "00002068-0000-0000-0000-000000000000",
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "last_seen": 33.7,
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 82,
  "type": "type0"
}
```

