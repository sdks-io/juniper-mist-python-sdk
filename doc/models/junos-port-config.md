
# Junos Port Config

Switch port config

## Structure

`JunosPortConfig`

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
| `usage` | `string` | Required | port usage name.<br><br>If EVPN is used, use `evpn_uplink`or `evpn_downlink` |

## Example (as JSON)

```json
{
  "aggregated": false,
  "disable_autoneg": false,
  "duplex": "auto",
  "mtu": 1514,
  "poe_disabled": false,
  "speed": "auto",
  "usage": "usage8",
  "ae_disable_lacp": false,
  "ae_idx": 218,
  "critical": false,
  "description": "description0"
}
```

