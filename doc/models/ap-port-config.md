
# Ap Port Config

## Structure

`ApPortConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_vlan_ids` | `List of int` | Optional | additional VLAN IDs, only valid in mesh base mode |
| `authentication_protocol` | [`AuthenticationProtocolEnum`](../../doc/models/authentication-protocol-enum.md) | Optional | if `enable_mac_auth`==`true`, allows user to select an authentication protocol<br>**Default**: `'pap'` |
| `disabled` | `bool` | Optional | - |
| `dynamic_vlan` | [`DynamicVlan`](../../doc/models/dynamic-vlan.md) | Optional | optional dynamic vlan |
| `enable_mac_auth` | `bool` | Optional | - |
| `forwarding` | [`ForwardingEnum`](../../doc/models/forwarding-enum.md) | Optional | **Default**: `'all'` |
| `mx_tunnel_id` | `uuid\|string` | Optional | if `forwarding`==`mxtunnel`, vlan_ids comes from mxtunnel |
| `mxtunnel_name` | `string` | Optional | if `forwarding`==`site_mxedge`, vlan_ids comes from site_mxedge (`mxtunnels` under site setting) |
| `port_auth` | [`PortAuthEnum`](../../doc/models/port-auth-enum.md) | Optional | When doing port auth<br>**Default**: `'none'` |
| `port_vlan_id` | `int` | Optional | if `forwrding`==`limited` |
| `radius_config` | [`JunosRadiusConfig`](../../doc/models/junos-radius-config.md) | Optional | Junos Radius config |
| `radsec` | [`Radsec`](../../doc/models/radsec.md) | Optional | Radsec settings |
| `vlan_id` | `int` | Optional | optional to specify the vlan id for a tunnel if forwarding is for `wxtunnel`, `mxtunnel` or `site_mxedge`.<br><br>* if vlan_id is not specified then it will use first one in vlan_ids[] of the mxtunnel.<br>* if forwarding == site_mxedge, vlan_ids comes from site_mxedge (`mxtunnels` under site setting) |
| `vland_ids` | `List of int` | Optional | if `forwrding`==`limited` |
| `wxtunnel_id` | `string` | Optional | if `forwarding`==`wxtunnel`, the port is bridged to the vlan of the session |
| `wxtunnel_remote_id` | `string` | Optional | if `forwarding`==`wxtunnel`, the port is bridged to the vlan of the session |

## Example (as JSON)

```json
{
  "authentication_protocol": "pap",
  "forwarding": "all",
  "port_auth": "none",
  "additional_vlan_ids": [
    209,
    210,
    211
  ],
  "disabled": false,
  "dynamic_vlan": {
    "default_vlan_id": 34,
    "enabled": false,
    "type": "type6",
    "vlans": {
      "key0": "vlans1"
    }
  },
  "enable_mac_auth": false
}
```

