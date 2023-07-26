
# Junos Vrrp Config

Junos VRRP config

## Structure

`JunosVrrpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `groups` | [`Groups`](../../doc/models/groups.md) | Optional | - |

## Example (as JSON)

```json
{
  "enabled": false,
  "groups": {
    "{vrrp_group}": {
      "priority": 8
    }
  }
}
```

