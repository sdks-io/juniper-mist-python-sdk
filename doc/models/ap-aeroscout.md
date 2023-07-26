
# Ap Aeroscout

Aeroscout AP settings

## Structure

`ApAeroscout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether to enable aeroscout config<br>**Default**: `False` |
| `host` | `string` | Optional | required if enabled, aeroscout server host |
| `locate_connected` | `bool` | Optional | whether to enable the feature to allow wireless clients data received and sent to AES server for location calculation |

## Example (as JSON)

```json
{
  "enabled": false,
  "host": "host8",
  "locate_connected": false
}
```

