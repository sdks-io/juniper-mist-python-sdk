
# Insight Rogue Clients

## Structure

`InsightRogueClients`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Required | - |
| `results` | [`List of Result20`](../../doc/models/result-20.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "next": "next2",
  "results": [
    {
      "annotation": "annotation3",
      "ap_mac": "ap_mac5",
      "avg_rssi": 236.57,
      "band": "band5",
      "bssid": "bssid3",
      "client_mac": "client_mac1",
      "num_aps": 57
    }
  ],
  "start": 212
}
```

