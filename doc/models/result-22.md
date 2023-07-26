
# Result 22

## Structure

`Result22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel` | `int` | Required | - |
| `noise` | `float` | Required | - |
| `other_rssi` | `float` | Optional | the avg RSSI heard from other APs (that does NOT belongs to the same site) |
| `other_ssid` | `string` | Optional | SSID from other AP that we heard from with the max RSSI |
| `util_score` | `float` | Required | utilization score, 0-1, lower means less utilization (cleaner RF) |
| `util_score_non_wifi` | `float` | Required | non-wifi utilization score, 0-1, lower means less utilization (cleaner RF) |
| `util_score_other` | `float` | Required | other utilization score, 0-1, lower means less utilization (cleaner RF) |

## Example (as JSON)

```json
{
  "channel": 120,
  "noise": 175.8,
  "other_rssi": 157.9,
  "other_ssid": "other_ssid0",
  "util_score": 54.68,
  "util_score_non_wifi": 206.34,
  "util_score_other": 232.94
}
```

