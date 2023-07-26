
# Dynamic Vlan 1

for 802.1x

## Structure

`DynamicVlan1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_vlan_id` | `int` | Optional | vlan_id to use when there’s no match from RADIUS<br>**Default**: `999`<br>**Constraints**: `>= 1`, `<= 4094` |
| `enabled` | `bool` | Optional | whether to enable dynamic vlan<br>**Default**: `False` |
| `local_vlan_ids` | `List of int` | Optional | vlan_ids to be locally bridged<br>**Constraints**: `>= 1`, `<= 4094` |
| `mtype` | [`Type39Enum`](../../doc/models/type-39-enum.md) | Optional | standard (using Tunnel-Private-Group-ID, widely supported), airespace-interface-name (Airespace/Cisco) |
| `vlans` | `dict` | Optional | map between vlan_id (as string) to airespace interface names (comma-separated) or null for stndard mapping |

## Example (as JSON)

```json
{
  "default_vlan_id": 999,
  "enabled": false,
  "local_vlan_ids": [
    123,
    124,
    125
  ],
  "type": "standard",
  "vlans": {
    "key0": "vlans5"
  }
}
```

