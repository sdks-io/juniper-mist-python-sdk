
# Lldp Stat

LLDP Stat (neighbor information, power negotiations)

## Structure

`LldpStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chassis_id` | `string` | Optional | - |
| `lldp_med_supported` | `bool` | Optional | whether it support LLDP-MED |
| `mgmt_addr` | `string` | Optional | switch’s management address (if advertised), can be IPv4, IPv6, or MAC |
| `port_desc` | `string` | Optional | port description, e.g. “2/20”, “Port 2 on Switch0” |
| `power_allocated` | `float` | Optional | in mW, provided/allocated by PSE |
| `power_draw` | `float` | Optional | in mW, total power needed by PD |
| `power_request_count` | `int` | Optional | number of negotiations, if it keeps increasing, we don’t have a stable power |
| `power_requested` | `float` | Optional | in mW, the current power requested by PD |
| `system_desc` | `string` | Optional | description provided by switch, e.g. “HP J9729A 2920-48G-POE+ Switch” |
| `system_name` | `string` | Optional | name of the switch, e.g. “TC2-OWL-Stack-01” |

## Example (as JSON)

```json
{
  "chassis_id": "chassis_id6",
  "lldp_med_supported": false,
  "mgmt_addr": "mgmt_addr4",
  "port_desc": "port_desc0",
  "power_allocated": 16.6
}
```

