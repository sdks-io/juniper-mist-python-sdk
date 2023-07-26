
# Rrm Band

## Structure

`RrmBand`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bandwidth` | [`Bandwidth1Enum`](../../doc/models/bandwidth-1-enum.md) | Optional | proposed bandwidth |
| `channel` | `int` | Optional | proposed channel |
| `curr_bandwidht` | [`CurrBandwidhtEnum`](../../doc/models/curr-bandwidht-enum.md) | Optional | current bandwidth |
| `curr_channel` | `int` | Optional | current channel |
| `curr_power` | `int` | Optional | current tx power |
| `curr_usage` | `string` | Optional | current radio band<br>**Constraints**: *Minimum Length*: `1` |
| `power` | `int` | Optional | proposed tx power |
| `usage` | `string` | Optional | proposed radio band<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "bandwidth": 20,
  "channel": 120,
  "curr_bandwidht": 80,
  "curr_channel": 240,
  "curr_power": 76
}
```

