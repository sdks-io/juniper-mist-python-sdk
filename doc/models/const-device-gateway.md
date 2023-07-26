
# Const Device Gateway

## Structure

`ConstDeviceGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defaults` | `dict` | Optional | Object Key is the interface type name (e.g. "lan_ports", "wan_ports", ...) |
| `description` | `string` | Optional | - |
| `experimental` | `bool` | Optional | **Default**: `False` |
| `fans_pluggable` | `bool` | Optional | **Default**: `True` |
| `ha_node_0_fpc` | `int` | Optional | - |
| `ha_node_1_fpc` | `int` | Optional | - |
| `has_bgp` | `bool` | Optional | **Default**: `False` |
| `has_fxp_0` | `bool` | Optional | **Default**: `True` |
| `has_ha_control` | `bool` | Optional | **Default**: `False` |
| `has_ha_data` | `bool` | Optional | **Default**: `False` |
| `has_irb` | `bool` | Optional | **Default**: `False` |
| `has_poe_out` | `bool` | Optional | **Default**: `True` |
| `has_snapshot` | `bool` | Optional | **Default**: `True` |
| `irb_disabled_by_default` | `bool` | Optional | **Default**: `False` |
| `model` | `string` | Optional | - |
| `number_fans` | `int` | Optional | - |
| `oc_device` | `bool` | Optional | **Default**: `False` |
| `pic` | `dict` | Optional | Object Key is the PIC number |
| `ports` | [`Ports1`](../../doc/models/ports-1.md) | Optional | Object Key is the interface name (e.g. "ge-0/0/1", ...) |
| `sub_required` | `string` | Optional | - |
| `t_128_device` | `bool` | Optional | **Default**: `False` |
| `mtype` | [`Type9Enum`](../../doc/models/type-9-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "experimental": false,
  "fans_pluggable": true,
  "has_bgp": false,
  "has_fxp0": true,
  "has_ha_control": false,
  "has_ha_data": false,
  "has_irb": false,
  "has_poe_out": true,
  "has_snapshot": true,
  "irb_disabled_by_default": false,
  "oc_device": false,
  "t128_device": false,
  "defaults": {
    "key0": "defaults8",
    "key1": "defaults9",
    "key2": "defaults0"
  },
  "description": "description0",
  "ha_node0_fpc": 146
}
```

