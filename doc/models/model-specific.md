
# Model Specific

## Structure

`ModelSpecific`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |
| `band_5` | [`ApRadioBand`](../../doc/models/ap-radio-band.md) | Optional | Radio Band AP settings |

## Example (as JSON)

```json
{
  "band_24": {
    "allow_rrm_disable": false,
    "ant_gain": 0,
    "antenna_mode": "default",
    "bandwidth": 20,
    "channel": 80
  },
  "band_5": {
    "allow_rrm_disable": false,
    "ant_gain": 52,
    "antenna_mode": "2x2",
    "bandwidth": 40,
    "channel": 132
  }
}
```

