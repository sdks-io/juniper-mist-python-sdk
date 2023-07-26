
# Radio Config

## Structure

`RadioConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24` | [`Band52`](../../doc/models/band-52.md) | Optional | - |
| `band_5` | [`Band52`](../../doc/models/band-52.md) | Optional | - |
| `band_6` | [`Band52`](../../doc/models/band-52.md) | Optional | - |
| `scanning_enabled` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "band_24": {
    "bandwidth": 4.04,
    "channel": 80,
    "dynamic_chaining_enabled": false,
    "power": 240.44,
    "rx_chain": 8
  },
  "band_5": {
    "bandwidth": 218.56,
    "channel": 132,
    "dynamic_chaining_enabled": false,
    "power": 198.96,
    "rx_chain": 212
  },
  "band_6": {
    "bandwidth": 77.08,
    "channel": 200,
    "dynamic_chaining_enabled": false,
    "power": 198.52,
    "rx_chain": 144
  },
  "scanning_enabled": false
}
```

