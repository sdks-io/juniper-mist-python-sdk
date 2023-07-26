
# Result 10

## Structure

`Result10`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Required | - |
| `band` | `string` | Required | - |
| `client_manufacture` | `string` | Required | - |
| `connect` | `float` | Required | - |
| `disconnect` | `float` | Required | - |
| `duration` | `float` | Required | - |
| `mac` | `string` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `ssid` | `string` | Required | - |
| `tags` | `List of string` | Optional | - |
| `timestamp` | `float` | Required | - |
| `wlan_id` | `uuid\|string` | Required | - |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "band": "band2",
  "client_manufacture": "client_manufacture6",
  "connect": 75.32,
  "disconnect": 254.02,
  "duration": 228.96,
  "mac": "mac4",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "ssid": "ssid2",
  "tags": [
    "tags5",
    "tags6"
  ],
  "timestamp": 128.82,
  "wlan_id": "00002208-0000-0000-0000-000000000000"
}
```

