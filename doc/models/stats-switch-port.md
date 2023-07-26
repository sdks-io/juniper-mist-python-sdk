
# Stats Switch Port

Switch port statistics

## Structure

`StatsSwitchPort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `for_site` | `bool` | Optional | - |
| `mac` | `string` | Required | - |
| `neighbor_mac` | `string` | Required | chassis identifier of the chassis type listed |
| `neighbor_port_desc` | `string` | Optional | description supplied by the system on the interface E.g. “GigabitEthernet2/0/39” |
| `neighbor_system_name` | `string` | Optional | name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local” |
| `org_id` | `uuid\|string` | Required | - |
| `poe_disabled` | `bool` | Optional | is the POE configured not be disabled. |
| `port_id` | `string` | Required | - |
| `port_mac` | `string` | Required | interface mac address |
| `rx_bytes` | `int` | Required | rx bytes |
| `rx_pkts` | `int` | Required | rx packets |
| `site_id` | `uuid\|string` | Required | - |
| `speed` | `int` | Optional | port speed |
| `tx_bytes` | `int` | Required | tx bytes |
| `tx_pkts` | `int` | Required | tx packets |
| `up` | `bool` | Optional | indicates if interface is up |
| `xcvr_part_number` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "for_site": false,
  "mac": "mac4",
  "neighbor_mac": "neighbor_mac0",
  "neighbor_port_desc": "neighbor_port_desc0",
  "neighbor_system_name": "neighbor_system_name2",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "poe_disabled": false,
  "port_id": "port_id0",
  "port_mac": "port_mac0",
  "rx_bytes": 214,
  "rx_pkts": 16,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "speed": 156,
  "tx_bytes": 96,
  "tx_pkts": 214
}
```

