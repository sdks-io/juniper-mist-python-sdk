
# Junos Dhcp Snooping

## Structure

`JunosDhcpSnooping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all_networks` | `bool` | Optional | - |
| `enable_arp_spoof_check` | `bool` | Optional | Enable for dynamic ARP inspection check |
| `enable_ip_source_guard` | `bool` | Optional | Enable for check for forging source IP address |
| `enabled` | `bool` | Optional | - |
| `networks` | `List of string` | Optional | if `all_networks`==`false`, list of network with DHCP snooping enabled |

## Example (as JSON)

```json
{
  "all_networks": false,
  "enable_arp_spoof_check": false,
  "enable_ip_source_guard": false,
  "enabled": false,
  "networks": [
    "networks2",
    "networks3",
    "networks4"
  ]
}
```

