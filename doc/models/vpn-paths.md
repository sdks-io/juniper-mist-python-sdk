
# Vpn Paths

## Structure

`VpnPaths`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bfd_profile` | [`BfdProfileEnum`](../../doc/models/bfd-profile-enum.md) | Optional | **Default**: `'broadband'` |
| `bfd_use_tunnel_mode` | `bool` | Optional | whether to use tunnel mode. SSR only<br>**Default**: `False` |
| `role` | [`Role2Enum`](../../doc/models/role-2-enum.md) | Optional | **Default**: `'spoke'` |
| `traffic_shaping` | [`TrafficShaping1`](../../doc/models/traffic-shaping-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "bfd_profile": "broadband",
  "bfd_use_tunnel_mode": false,
  "role": "spoke",
  "traffic_shaping": {
    "class_percentage": [
      173,
      172
    ],
    "enabled": false,
    "max_tx_kbps": 212
  }
}
```

