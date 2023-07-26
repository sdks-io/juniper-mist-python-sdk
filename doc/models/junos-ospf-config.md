
# Junos Ospf Config

Junos OSPF config

## Structure

`JunosOspfConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `areas` | [`dict`](../../doc/models/areas.md) | Optional | OSPF areas to run on this device and the corresponding per-area-specific configs. The property key is the area |
| `enabled` | `bool` | Optional | whether to rung OSPF on this device |
| `reference_bandwidth` | `string` | Optional | Bandwidth for calculating metric defaults (9600..4000000000000)<br>**Default**: `'100M'` |

## Example (as JSON)

```json
{
  "reference_bandwidth": "100M",
  "areas": {
    "key0": {
      "no_summary": true
    },
    "key1": {
      "no_summary": false
    }
  },
  "enabled": false
}
```

