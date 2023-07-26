
# Device Search Ap

## Structure

`DeviceSearchAp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24_bandwith` | `string` | Optional | Bandwith of band_24 |
| `band_24_channel` | `int` | Optional | Channel of band_24 |
| `band_24_power` | `int` | Optional | - |
| `band_5_bandwith` | `string` | Optional | Bandwith of band_5 |
| `band_5_channel` | `int` | Optional | Channel of band_5 |
| `band_5_power` | `int` | Optional | - |
| `band_6_bandwith` | `string` | Optional | - |
| `band_6_channel` | `int` | Optional | Channel of band_6 |
| `band_6_power` | `int` | Optional | - |
| `eth_0_port_speed` | `int` | Optional | Port speed of eth0 |
| `ext_ip` | `string` | Optional | - |
| `hostname` | `List of string` | Optional | partial / full hostname |
| `ip` | `string` | Optional | ip address |
| `lldp_mgmt_addr` | `string` | Optional | LLDP management ip address |
| `lldp_port_desc` | `string` | Optional | - |
| `lldp_port_id` | `string` | Optional | LLDP port id |
| `lldp_power_allocated` | `int` | Optional | - |
| `lldp_power_draw` | `int` | Optional | - |
| `lldp_system_desc` | `string` | Optional | LLDP system description |
| `lldp_system_name` | `string` | Optional | LLDP system name |
| `mac` | `string` | Optional | device model |
| `model` | `string` | Optional | - |
| `mxedge_id` | `string` | Optional | Mist Edge id, if AP is connecting to a Mist Edge |
| `mxtunnel_status` | `string` | Optional | MxTunnel status |
| `org_id` | `string` | Optional | - |
| `power_constrained` | `bool` | Optional | - |
| `site_id` | `string` | Optional | site id |
| `sku` | `string` | Optional | - |
| `timestamp` | `float` | Optional | - |
| `uptime` | `int` | Optional | - |
| `version` | `string` | Optional | version |

## Example (as JSON)

```json
{
  "band_24_bandwith": "band_24_bandwith4",
  "band_24_channel": 162,
  "band_24_power": 192,
  "band_5_bandwith": "band_5_bandwith0",
  "band_5_channel": 94
}
```

