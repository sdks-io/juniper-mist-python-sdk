
# Ap Usb

USB AP settings
Note: if native imagotag is enabled, BLE will be disabled automatically
Note: legacy, new config moved to ESL Config.

## Structure

`ApUsb`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cacert` | `string` | Optional | only if `type`==`imagotag` |
| `channel` | `int` | Optional | only if `type`==`imagotag`<br>channel selection, not needed by default, required for manual channel override only |
| `enabled` | `bool` | Optional | whether to enable any usb config |
| `host` | `string` | Optional | only if `type`==`imagotag` |
| `port` | `int` | Optional | only if `type`==`imagotag`<br>**Default**: `0` |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Optional | usb config type |
| `verify_cert` | `bool` | Optional | only if `type`==`imagotag`, whether to turn on SSL verification |
| `vlan_id` | `int` | Optional | only if `type`==`solum` or `type`==`hanshow`<br>**Default**: `1` |

## Example (as JSON)

```json
{
  "port": 0,
  "vlan_id": 1,
  "cacert": "cacert8",
  "channel": 120,
  "enabled": false,
  "host": "host8"
}
```

