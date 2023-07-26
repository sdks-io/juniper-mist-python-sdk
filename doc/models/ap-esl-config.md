
# Ap Esl Config

## Structure

`ApEslConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cacert` | `string` | Optional | Only if `type`==`imagotag` or `type`==`native` |
| `channel` | `int` | Optional | Only if `type`==`imagotag` or `type`==`native` |
| `enabled` | `bool` | Optional | usb_config is ignored if esl_config enabled<br>**Default**: `False` |
| `host` | `string` | Optional | Only if `type`==`imagotag` or `type`==`native` |
| `port` | `int` | Optional | Only if `type`==`imagotag` or `type`==`native` |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Optional | note: ble_config will be ingored if esl_config is enabled and with native mode. |
| `verify_cert` | `bool` | Optional | Only if `type`==`imagotag` or `type`==`native` |
| `vlan_id` | `int` | Optional | Only if `type`==`solum` or `type`==`hansho`<br>**Default**: `1` |

## Example (as JSON)

```json
{
  "channel": 3,
  "enabled": false,
  "port": 0,
  "type": "imagotag",
  "vlan_id": 1,
  "cacert": "cacert8",
  "host": "host8"
}
```

