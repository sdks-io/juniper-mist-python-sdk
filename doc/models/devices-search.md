
# Devices Search

## Structure

`DevicesSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result15`](../../doc/models/result-15.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "band_24_bandwith": "band_24_bandwith7",
      "band_24_channel": 79,
      "band_24_power": 19,
      "band_5_bandwith": "band_5_bandwith7",
      "band_5_channel": 11
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

