
# Tunterm Igmp Snooping Config

## Structure

`TuntermIgmpSnoopingConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `querier` | [`Querier`](../../doc/models/querier.md) | Optional | - |
| `vlan_ids` | `List of int` | Optional | the list of vlans on which tunterm performs IGMP snooping |

## Example (as JSON)

```json
{
  "enabled": false,
  "querier": {
    "max_response_time": 136,
    "mtu": 120,
    "query_interval": 156,
    "robustness": 80,
    "version": 0
  },
  "vlan_ids": [
    196,
    197,
    198
  ]
}
```

