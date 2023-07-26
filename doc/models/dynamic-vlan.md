
# Dynamic Vlan

optional dynamic vlan

## Structure

`DynamicVlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_vlan_id` | `int` | Optional | - |
| `enabled` | `bool` | Optional | - |
| `mtype` | `string` | Optional | - |
| `vlans` | `dict` | Optional | - |

## Example (as JSON)

```json
{
  "default_vlan_id": 30,
  "enabled": false,
  "type": "type0",
  "vlans": {
    "key0": "vlans5"
  }
}
```

