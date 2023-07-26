
# Ipsec 1

IPSec-related configurations; requires DMVPN be enabled

## Structure

`Ipsec1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether ipsec is enabled, requires DMVPN be enabled<br>**Default**: `False` |
| `psk` | `string` | Required | ipsec pre-shared key |

## Example (as JSON)

```json
{
  "enabled": false,
  "psk": "psk8"
}
```

