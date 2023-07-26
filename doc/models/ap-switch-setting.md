
# Ap Switch Setting

## Structure

`ApSwitchSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_vlan_ids` | `List of int` | Optional | additional VLAN IDs, only valid in mesh base mode |
| `enable_vlan` | `bool` | Optional | - |
| `port_vlan_id` | `object` | Optional | native VLAN id, optional |
| `vlan_ids` | `List of int` | Optional | list of VLAN ids this |

## Example (as JSON)

```json
{
  "additional_vlan_ids": [
    209,
    210,
    211
  ],
  "enable_vlan": false,
  "port_vlan_id": {
    "key1": "val1",
    "key2": "val2"
  },
  "vlan_ids": [
    196,
    197,
    198
  ]
}
```

