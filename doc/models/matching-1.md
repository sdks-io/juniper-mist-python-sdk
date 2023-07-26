
# Matching 1

zero or more criteria/filter can be specified to match the term, all criteria have to be met

## Structure

`Matching1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `as_path` | `List of string` | Optional | takes regular expression |
| `community` | `List of string` | Optional | - |
| `network` | `List of string` | Optional | - |
| `prefix` | `List of string` | Optional | zero or more criteria/filter can be specified to match the term, all criteria have to be met |
| `protocol` | `List of string` | Optional | `direct`, `bgp`, `osp`, ... |
| `route_exists` | [`RouteExists`](../../doc/models/route-exists.md) | Optional | - |
| `vpn_neighbor_mac` | `List of string` | Optional | overlay-facing criteria (used for bgp_config where via=vpn) |
| `vpn_path` | `List of string` | Optional | overlay-facing criteria (used for bgp_config where via=vpn)<br>ordered- |
| `vpn_path_sla` | [`VpnPathSla`](../../doc/models/vpn-path-sla.md) | Optional | - |

## Example (as JSON)

```json
{
  "as_path": [
    "as_path0",
    "as_path1"
  ],
  "community": [
    "community8",
    "community9"
  ],
  "network": [
    "network7",
    "network8",
    "network9"
  ],
  "prefix": [
    "prefix7",
    "prefix8"
  ],
  "protocol": [
    "protocol7"
  ]
}
```

