
# Client Sessions Search

## Structure

`ClientSessionsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result10`](../../doc/models/result-10.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ap": "ap1",
      "band": "band5",
      "client_manufacture": "client_manufacture3",
      "connect": 141.05,
      "disconnect": 63.75,
      "duration": 38.69,
      "mac": "mac7",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "site_id": "00002183-0000-0000-0000-000000000000",
      "ssid": "ssid9",
      "tags": [
        "tags8",
        "tags9"
      ],
      "timestamp": 63.09,
      "wlan_id": "000014a5-0000-0000-0000-000000000000"
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

