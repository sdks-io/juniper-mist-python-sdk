
# Events Fastroam

## Structure

`EventsFastroam`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | the link to query next set of results. value is null if no next page exists. |
| `results` | [`List of Result16`](../../doc/models/result-16.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ap_mac": "ap_mac5",
      "client_mac": "client_mac1",
      "fromap": "fromap9",
      "latency": 59.87,
      "ssid": "ssid9",
      "subtype": "subtype5",
      "timestamp": 63.09,
      "type": "slow"
    }
  ],
  "start": 212,
  "next": "next2"
}
```

