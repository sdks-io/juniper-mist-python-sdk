
# Const Device Switch

## Structure

`ConstDeviceSwitch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alias` | `string` | Optional | - |
| `defaults` | [`Defaults`](../../doc/models/defaults.md) | Optional | - |
| `description` | `string` | Optional | - |
| `display` | `string` | Optional | - |
| `evolved_os` | `bool` | Optional | **Default**: `False` |
| `evpn_ri_type` | `string` | Optional | - |
| `experimental` | `bool` | Optional | **Default**: `False` |
| `fans_pluggable` | `bool` | Optional | **Default**: `False` |
| `has_bgp` | `bool` | Optional | **Default**: `False` |
| `has_ets` | `bool` | Optional | **Default**: `False` |
| `has_evpn` | `bool` | Optional | **Default**: `False` |
| `has_irb` | `bool` | Optional | **Default**: `False` |
| `has_poe_out` | `bool` | Optional | **Default**: `False` |
| `has_snapshot` | `bool` | Optional | **Default**: `True` |
| `has_vc` | `bool` | Optional | **Default**: `True` |
| `model` | `string` | Optional | - |
| `modular` | `bool` | Optional | **Default**: `False` |
| `no_shaping_rate` | `bool` | Optional | **Default**: `False` |
| `number_fans` | `int` | Optional | - |
| `oc_device` | `bool` | Optional | **Default**: `False` |
| `oob_interface` | `string` | Optional | - |
| `packet_action_drop_only` | `bool` | Optional | **Default**: `False` |
| `pic` | `dict` | Optional | Object Key is the PIC number |
| `sub_required` | `string` | Optional | - |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "evolved_os": false,
  "experimental": false,
  "fans_pluggable": false,
  "has_bgp": false,
  "has_ets": false,
  "has_evpn": false,
  "has_irb": false,
  "has_poe_out": false,
  "has_snapshot": true,
  "has_vc": true,
  "modular": false,
  "no_shaping_rate": false,
  "oc_device": false,
  "packet_action_drop_only": false,
  "alias": "alias2",
  "defaults": {
    "_ports": "_ports6"
  },
  "description": "description0",
  "display": "display8"
}
```

