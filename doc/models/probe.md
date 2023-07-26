
# Probe

Only if:

* `provider`== `custom-ipsec`

## Structure

`Probe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interval` | `int` | Optional | how often to trigger the probe |
| `threshold` | `int` | Optional | number of consecutive misses before declaring the tunnel down |
| `timeout` | `int` | Optional | time within which to complete the connectivity check |
| `mtype` | [`Type20Enum`](../../doc/models/type-20-enum.md) | Optional | **Default**: `'icmp'` |

## Example (as JSON)

```json
{
  "type": "icmp",
  "interval": 92,
  "threshold": 224,
  "timeout": 32
}
```

