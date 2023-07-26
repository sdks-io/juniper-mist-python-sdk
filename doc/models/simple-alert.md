
# Simple Alert

Set of heuristic rules will be enabled when marvis subscription is not available.
It triggers when, in a Z minute window, there are more than Y distinct client encountring over X failures

## Structure

`SimpleAlert`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `arp_failure` | [`ArpFailure`](../../doc/models/arp-failure.md) | Optional | - |
| `dhcp_failure` | [`DhcpFailure`](../../doc/models/dhcp-failure.md) | Optional | - |
| `dns_failure` | [`DnsFailure`](../../doc/models/dns-failure.md) | Optional | - |

## Example (as JSON)

```json
{
  "arp_failure": {
    "client_count": 26,
    "duration": 130,
    "incident_count": 226
  },
  "dhcp_failure": {
    "client_count": 246,
    "duration": 94,
    "incident_count": 6
  },
  "dns_failure": {
    "client_count": 252,
    "duration": 100,
    "incident_count": 0
  }
}
```

