
# Ap Client Bridge

## Structure

`ApClientBridge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth` | [`Auth`](../../doc/models/auth.md) | Optional | - |
| `enabled` | `bool` | Optional | when acted as client bridge:<br><br>* only 5G radio can be used<br>* will not serve as AP on any radios |
| `ssid` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "auth": {
    "psk": "psk4",
    "type": "open"
  },
  "enabled": false,
  "ssid": "ssid2"
}
```

