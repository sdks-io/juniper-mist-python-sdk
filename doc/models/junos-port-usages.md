
# Junos Port Usages

Junos port usages

## Structure

`JunosPortUsages`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all_networks` | `bool` | Optional | if `mode`==`trunk`, whether to trunk all network/vlans<br>**Default**: `False` |
| `allow_dhcpd` | `bool` | Optional | if DHCP snooping is enabled, whether DHCP server is allowed on the interfaces with. All the interfaces from port configs using this port usage are effected. Please notice that allow_dhcpd is a tri-state.<br><br>When it is not defined, it means using the system’s default setting which depends on whether the port is a access or trunk port. |
| `authentication_protocol` | [`AuthenticationProtocol1Enum`](../../doc/models/authentication-protocol-1-enum.md) | Optional | can be set for non-mist-nac config when `enable_mac_auth`==`true`<br>**Default**: `'pap'` |
| `bypass_auth_when_server_down` | `bool` | Optional | if `port_auth`==`dot1x`, whether to allow the device to connect if RADIUS server is down |
| `description` | `string` | Optional | description |
| `disable_autoneg` | `bool` | Optional | if speed and duplex are specified, whether to disable autonegotiation<br>**Default**: `False` |
| `disabled` | `bool` | Optional | whether the port is disabled<br>**Default**: `False` |
| `duplex` | [`Duplex2Enum`](../../doc/models/duplex-2-enum.md) | Optional | link connection mode, choices are auto (default), full, and half<br>**Default**: `'auto'` |
| `enable_mac_auth` | `bool` | Optional | if `port_auth`==`dot1x`, whether to enable MAC Auth |
| `enable_qos` | `bool` | Optional | - |
| `guest_network` | `string` | Optional | if `port_auth`==`dot1x`, which network to put the device into if the device cannot do dot1x. default is null (i.e. not allowed) |
| `mac_auth_only` | `bool` | Optional | only effect once `enable_mac_auth`==`true` |
| `mac_limit` | `int` | Optional | max number of mac addresses, default is 0 for unlimited, otherwise range is 1 or higher, with upper bound constrained by platform<br>**Default**: `0`<br>**Constraints**: `>= 0` |
| `mode` | [`Mode1Enum`](../../doc/models/mode-1-enum.md) | Optional | access (default) / trunk |
| `mtu` | `int` | Optional | media maximum transmission unit (MTU) is the largest data unit that can be forwarded without fragmentation. The default value is 1514. |
| `networks` | `List of string` | Optional | if `mode`==`trunk`, the list of network/vlans |
| `persist_mac` | `bool` | Optional | if `mode`==`access` and `port_auth`!=`dot1x`, whether the port should retain dynamically learned MAC addresses<br>**Default**: `False` |
| `poe_disabled` | `bool` | Optional | whether PoE capabilities are disabled for a port<br>**Default**: `False` |
| `port_auth` | `string` | Optional | if dot1x is desired, set to dot1x |
| `port_network` | `string` | Optional | native network/vlan for untagged traffic |
| `rejected_network` | `bool` | Optional | if `port_auth`==`dot1x`, when radius server reject / fails |
| `speed` | `string` | Optional | speed, default is auto to automatically negotiate speed |
| `storm_control` | [`JunosStormControl`](../../doc/models/junos-storm-control.md) | Optional | Switch storm control |
| `stp_edge` | `bool` | Optional | when enabled, the port is not expected to receive BPDU frames |
| `voip_network` | `string` | Optional | network/vlan for voip traffic, must also set port_network. to authenticate device, set port_auth |

## Example (as JSON)

```json
{
  "all_networks": false,
  "authentication_protocol": "pap",
  "disable_autoneg": false,
  "disabled": false,
  "duplex": "auto",
  "mac_limit": 0,
  "persist_mac": false,
  "poe_disabled": false,
  "allow_dhcpd": false,
  "bypass_auth_when_server_down": false,
  "description": "description0"
}
```

