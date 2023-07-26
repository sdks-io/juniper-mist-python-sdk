
# Pcaps Search

## Structure

`PcapsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Required | - |
| `results` | [`List of Result21`](../../doc/models/result-21.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "next": "next2",
  "results": [
    {
      "ap_macs": [
        "ap_macs4",
        "ap_macs5"
      ],
      "timestamp": 63.09,
      "type": "type7",
      "url": "url7"
    }
  ],
  "start": 212,
  "total": 10
}
```

