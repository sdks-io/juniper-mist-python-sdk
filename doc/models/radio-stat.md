
# Radio Stat

a map of radio stats, key can be band_24 / band_5

## Structure

`RadioStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24` | [`Band242`](../../doc/models/band-242.md) | Optional | radio stat of 2.4G radio |
| `band_5` | [`Band53`](../../doc/models/band-53.md) | Optional | radio stat of 5G radio |
| `band_6` | [`Band62`](../../doc/models/band-62.md) | Optional | radio stat of 6G radio |

## Example (as JSON)

```json
{
  "band_24": {
    "bandwidth": 20,
    "channel": 80,
    "dynamic_chaining_enalbed": false,
    "mac": "mac4",
    "num_clients": 190
  },
  "band_5": {
    "bandwidth": 40,
    "channel": 132,
    "dynamic_chaining_enalbed": false,
    "mac": "mac6",
    "num_clients": 139.62
  },
  "band_6": {
    "bandwidth": 20,
    "channel": 200,
    "dynamic_chaining_enalbed": false,
    "mac": "mac8",
    "num_clients": 254.14
  }
}
```

