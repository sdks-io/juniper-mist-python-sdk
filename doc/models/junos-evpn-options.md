
# Junos Evpn Options

EVPN Options

## Structure

`JunosEvpnOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_loopback_subnet` | `string` | Optional | optional, for dhcp_relay, unique loopback IPs are required for ERB or IPClos where we can set option-82 server-id-overrides |
| `auto_router_id_subnet` | `string` | Optional | optional, this generates router_id automatically, if specified, `router_id_prefix` is ignored |
| `core_as_border` | `bool` | Optional | optional, for ERB or CLOS, you can either use esilag to upstream routers or to also be the virtual-gateway<br>when `routed_at` != `core`, whether to do virtual-gateway at core as well<br>**Default**: `False` |
| `overlay` | [`Overlay`](../../doc/models/overlay.md) | Optional | - |
| `per_vlan_vga_v_4_mac` | `bool` | Optional | by default, JUNOS uses 00-00-5e-00-01-01 as the virtual-gateway-address's v4-mac<br>if enabled, 00-00-5e-00-XX-YY will be used (where XX=vlan_id/256, YY=vlan_id%256)<br>**Default**: `False` |
| `routed_at` | [`RoutedAtEnum`](../../doc/models/routed-at-enum.md) | Optional | optional, where virtual-gateway should reside<br>**Default**: `'edge'` |
| `underlay` | [`Underlay`](../../doc/models/underlay.md) | Optional | - |

## Example (as JSON)

```json
{
  "auto_loopback_subnet": "100.101.0.0/16",
  "auto_router_id_subnet": "100.100.0.0/24",
  "core_as_border": false,
  "per_vlan_vga_v4_mac": false,
  "routed_at": "edge",
  "overlay": {
    "as": 98
  }
}
```

