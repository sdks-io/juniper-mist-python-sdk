
# Port Config 2

eth0 is allowed in mesh relay mode, otherwise eth0 is not allowed here.
The property key is the interface(s) name (e.g. "eth1" or"eth1,eth2")

## Structure

`PortConfig2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ae_disable_lacp` | `bool` | Optional | To disable LACP support for the AE interface |
| `ae_idx` | `int` | Optional | Users could force to use the designated AE name |
| `aggregated` | `bool` | Optional | **Default**: `False` |
| `critical` | `bool` | Optional | if want to generate port up/down alarm |
| `description` | `string` | Optional | - |
| `disable_autoneg` | `bool` | Optional | if `speed` and `duplex` are specified, whether to disable autonegotiation<br>**Default**: `False` |
| `duplex` | [`DuplexEnum`](../../doc/models/duplex-enum.md) | Optional | **Default**: `'auto'` |
| `dynamic_usage` | `string` | Optional | Enable dynamic usage for this port. Set to `dynamic` to enable. |
| `esilag` | `bool` | Optional | - |
| `mtu` | `int` | Optional | media maximum transmission unit (MTU) is the largest data unit that can be forwarded without fragmentation<br>**Default**: `1514` |
| `no_local_overwrite` | `bool` | Optional | prevent helpdesk to override the port config |
| `poe_disabled` | `bool` | Optional | **Default**: `False` |
| `speed` | [`SpeedEnum`](../../doc/models/speed-enum.md) | Optional | **Default**: `'auto'` |
| `usage` | [`Usage3Enum`](../../doc/models/usage-3-enum.md) | Required | port usage name.<br><br>If EVPN is used, use `evpn_uplink`or `evpn_downlink` |
| `dsl_config` | [`DslConfig`](../../doc/models/dsl-config.md) | Optional | if `wan_type`==`dsl` |
| `ip_config` | [`JunosIpConfigGateway`](../../doc/models/junos-ip-config-gateway.md) | Optional | Junos IP Config |
| `lte_apn` | `string` | Optional | if `wan_type`==`lte` |
| `lte_auth` | [`LteAuthEnum`](../../doc/models/lte-auth-enum.md) | Optional | if `wan_type`==`lte`<br>**Default**: `'none'` |
| `lte_backup` | `bool` | Optional | - |
| `lte_password` | `string` | Optional | if `wan_type`==`lte` |
| `lte_username` | `string` | Optional | if `wan_type`==`lte` |
| `name` | `string` | Optional | name that we'll use to derive config |
| `networks` | `List of string` | Optional | if `usage`==`lan` |
| `outer_vlan_id` | `int` | Optional | for Q-in-Q |
| `port_network` | `string` | Optional | if `usage`==`lan` |
| `preserve_dscp` | `bool` | Optional | whether to preserve dscp when sending traffic over VPN (SSR-only)<br>**Default**: `True` |
| `redundant` | `bool` | Optional | if HA mode |
| `reth_idx` | `int` | Optional | if HA mode |
| `reth_node` | `string` | Optional | if HA mode |
| `svr_port_range` | `string` | Optional | For 128T only, 16385 - 65353 |
| `traffic_shaping` | [`TrafficShaping`](../../doc/models/traffic-shaping.md) | Optional | - |
| `vlan_id` | `int` | Optional | if WAN interface is on a VLAN |
| `vpn_paths` | [`dict`](../../doc/models/vpn-paths.md) | Optional | - |
| `wan_ext_ip` | `string` | Optional | optional, if spoke should reach this port by a different IP |
| `wan_source_nat` | [`WanSourceNat`](../../doc/models/wan-source-nat.md) | Optional | optional, by default, source-NAT is performed on all WAN Ports using the interface-ip |
| `wan_type` | [`WanTypeEnum`](../../doc/models/wan-type-enum.md) | Optional | if `usage`==`wan`<br>**Default**: `'broadband'` |

## Example (as JSON)

```json
{
  "aggregated": false,
  "disable_autoneg": false,
  "duplex": "full",
  "mtu": 1514,
  "poe_disabled": false,
  "speed": "1g",
  "usage": "ha_data",
  "lte_auth": "none",
  "preserve_dscp": true,
  "svr_port_range": "60000-60005",
  "wan_type": "broadband",
  "ae_disable_lacp": false,
  "ae_idx": 218,
  "critical": false,
  "description": "description0"
}
```

