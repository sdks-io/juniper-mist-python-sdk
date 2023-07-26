
# Junos Port Config Gateway

Gateway port config

## Structure

`JunosPortConfigGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Optional | - |
| `disable_autoneg` | `bool` | Optional | **Default**: `False` |
| `dsl_config` | [`DslConfig`](../../doc/models/dsl-config.md) | Optional | if `wan_type`==`dsl` |
| `duplex` | [`DuplexEnum`](../../doc/models/duplex-enum.md) | Optional | **Default**: `'auto'` |
| `ip_config` | [`JunosIpConfigGateway`](../../doc/models/junos-ip-config-gateway.md) | Optional | Junos IP Config |
| `lte_apn` | `string` | Optional | if `wan_type`==`lte` |
| `lte_auth` | [`LteAuthEnum`](../../doc/models/lte-auth-enum.md) | Optional | if `wan_type`==`lte`<br>**Default**: `'none'` |
| `lte_backup` | `bool` | Optional | - |
| `lte_password` | `string` | Optional | if `wan_type`==`lte` |
| `lte_username` | `string` | Optional | if `wan_type`==`lte` |
| `mtu` | `int` | Optional | - |
| `name` | `string` | Optional | name that we'll use to derive config |
| `networks` | `List of string` | Optional | if `usage`==`lan` |
| `outer_vlan_id` | `int` | Optional | for Q-in-Q |
| `poe_disabled` | `bool` | Optional | **Default**: `False` |
| `port_network` | `string` | Optional | if `usage`==`lan` |
| `preserve_dscp` | `bool` | Optional | whether to preserve dscp when sending traffic over VPN (SSR-only)<br>**Default**: `True` |
| `redundant` | `bool` | Optional | if HA mode |
| `reth_idx` | `int` | Optional | if HA mode |
| `reth_node` | `string` | Optional | if HA mode |
| `speed` | `string` | Optional | **Default**: `'auto'` |
| `svr_port_range` | `string` | Optional | For 128T only, 16385 - 65353 |
| `traffic_shaping` | [`TrafficShaping`](../../doc/models/traffic-shaping.md) | Optional | - |
| `usage` | [`Usage1Enum`](../../doc/models/usage-1-enum.md) | Required | port usage name |
| `vlan_id` | `int` | Optional | if WAN interface is on a VLAN |
| `vpn_paths` | [`dict`](../../doc/models/vpn-paths.md) | Optional | - |
| `wan_ext_ip` | `string` | Optional | optional, if spoke should reach this port by a different IP |
| `wan_source_nat` | [`WanSourceNat`](../../doc/models/wan-source-nat.md) | Optional | optional, by default, source-NAT is performed on all WAN Ports using the interface-ip |
| `wan_type` | [`WanTypeEnum`](../../doc/models/wan-type-enum.md) | Optional | if `usage`==`wan`<br>**Default**: `'broadband'` |

## Example (as JSON)

```json
{
  "disable_autoneg": false,
  "duplex": "full",
  "lte_auth": "none",
  "poe_disabled": false,
  "preserve_dscp": true,
  "speed": "1g",
  "svr_port_range": "60000-60005",
  "usage": "ha_data",
  "wan_type": "broadband",
  "description": "description0",
  "dsl_config": {
    "ppoe_auth": "pap",
    "ppoe_password": "ppoe_password4",
    "ppoe_username": "ppoe_username6"
  },
  "ip_config": {
    "dns": [
      "dns3",
      "dns2",
      "dns1"
    ],
    "dns_suffix": [
      "dns_suffix9",
      "dns_suffix0",
      "dns_suffix1"
    ],
    "gateway": "gateway0",
    "ip": "ip4",
    "netmask": "netmask0"
  }
}
```

